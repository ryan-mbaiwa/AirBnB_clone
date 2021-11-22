#!/usr/bin/python3
"""
The console for AirBnB clone, hbnb
"""
import cmd
import sys
import shlex
from models import storage
from models.base_model import BaseModel
from datetime import datetime
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Class for command interpreter. This is the entry point """
    prompt = '(hbnb) '

    def emptyline(self):
        """ Handles empty spaces when you press ENTER """
        pass

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        return True

    def do_create(self, arg):
        """ Creates and saves new instance of BaseModel and prints id """
        if len(arg) < 1:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])()
            obj.save()
            print(obj.id)
        except:
            print("** class doesn't exist **")
            return

    def do_show(self, arg):
        """ prints the string representation of the instance based on
        class name and id """
        if len(arg) < 2:
            print("** class name missing **")
            return
        arg_list = shlex.split(arg)
        try:
            obj = eval(arg_list[0])()
        except:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        flag = 0
        for key, value in storage.all().items():
            if key == "{}.{}".format(arg_list[0], arg_list[1]):
                print(value)
                flag = 1
        if flag == 0:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = shlex.split(arg)
        try:
            obj = eval(arg_list[0])()
        except:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        flag = 0
        dict_obj = storage.all()
        for key, value in dict_obj.items():
            if key == "{}.{}".format(arg_list[0], arg_list[1]):
                del dict_obj[key]
                storage.save()
                flag = 1
                break
        if flag == 0:
            print("** no instance found **")
            return

    def do_all(self, arg):
        """ Prints all string representations of all instances based or not
        on the class name """
        if len(arg) == 0:
            for key in storage.all():
                obj_class = storage.all()[key]
                print(obj_class)
            return
        if not arg:
            print("** class doesn't exist **")
            return
        arg_list = shlex.split(arg)
        if arg_list[0] not in ["BaseModel", "User", "State", "City", "Place",
                               "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        else:
            for key in storage.all():
                obj_class = storage.all()[key]
                if arg_list[0] == obj_class.__class__.__name__:
                    print(obj_class)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = shlex.split(arg)
        if arg_list[0] not in ["BaseModel", "User", "State", "City", "Place",
                               "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        flag = 0
        for key, value in storage.all().items():
            if key == "{}.{}".format(arg_list[0], arg_list[1]):
                flag = 1
        if flag == 0:
            print("** no instance found **")
            return
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return
        if len(arg_list) == 3:
            print("** value missing **")
            return
        else:
            model = storage.all()[".".join(arg_list[:2])]
            arg_list[3] = arg_list[3].strip('\"')
            if arg_list[3].isdigit():
                arg_list[3] = int(arg_list[3])
            setattr(model, arg_list[2], arg_list[3])

    def count(self, arg):
        """ Counts number of instances in a class """
        count = 0
        arg_list = arg.split(' ')
        for key in storage.all():
            obj_class = storage.all()[key]
            if arg_list[0] == obj_class.__class__.__name__:
                count += 1
        print(count)

    def do_BaseModel(self, arg):
        """ all, instance count, show, and update functions """
        if arg == '.all()':
            self.do_all('BaseModel')
        if arg == '.count()':
            self.count('BaseModel')
        if arg.startswith('.show(') is True:
            idx_1 = arg.index('"') + 1
            str_pos1 = arg[idx_1:]
            idx_2 = str_pos1.index('"')
            id_str = str_pos1[:idx_2]
            self.do_show("BaseModel {}".format(id_str))
        if arg.startswith('.update(') is True:
            idx_1 = arg.index('"') + 1
            str_pos1 = arg[idx_1:]
            idx_2 = str_pos1.index('"')
            id_str = str_pos1[:idx_2]

            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"')
            key = str_pos1[:idx_1]

            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"')
            value = str_pos1[:idx_1]
            self.do_update("BaseModel {} {} {}".format(id_str, key, value))

    def do_User(self, arg):
        """ all, instance count, show, and update functions """
        if arg == '.all()':
            self.do_all('User')
        if arg == '.count()':
            self.count('User')
        if arg.startswith('.show(') is True:
            idx_1 = arg.index('"') + 1
            str_pos1 = arg[idx_1:]
            idx_2 = str_pos1.index('"')
            id_str = str_pos1[:idx_2]
            self.do_show("User {}".format(id_str))
        if arg.startswith('.update(') is True:
            idx_1 = arg.index('"') + 1
            str_pos1 = arg[idx_1:]
            idx_2 = str_pos1.index('"')
            id_str = str_pos1[:idx_2]

            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"')
            key = str_pos1[:idx_1]

            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"')
            value = str_pos1[:idx_1]
            self.do_update("User {} {} {}".format(id_str, key, value))

    def do_State(self, arg):
        """ all, instance count, show, and update functions """
        if arg == '.all()':
            self.do_all('State')
        if arg == '.count()':
            self.count('State')
        if arg.startswith('.show(') is True:
            idx_1 = arg.index('"') + 1
            str_pos1 = arg[idx_1:]
            idx_2 = str_pos1.index('"')
            id_str = str_pos1[:idx_2]
            self.do_show("State {}".format(id_str))
        if arg.startswith('.update(') is True:
            idx_1 = arg.index('"') + 1
            str_pos1 = arg[idx_1:]
            idx_2 = str_pos1.index('"')
            id_str = str_pos1[:idx_2]

            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"')
            key = str_pos1[:idx_1]

            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"')
            value = str_pos1[:idx_1]
            self.do_update("State {} {} {}".format(id_str, key, value))

    def do_City(self, arg):
        """ all, instance count, show, and update functions """
        if arg == '.all()':
            self.do_all('City')
        if arg == '.count()':
            self.count('City')
        if arg.startswith('.show(') is True:
            idx_1 = arg.index('"') + 1
            str_pos1 = arg[idx_1:]
            idx_2 = str_pos1.index('"')
            id_str = str_pos1[:idx_2]
            self.do_show("City {}".format(id_str))
        if arg.startswith('.update(') is True:
            idx_1 = arg.index('"') + 1
            str_pos1 = arg[idx_1:]
            idx_2 = str_pos1.index('"')
            id_str = str_pos1[:idx_2]

            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"')
            key = str_pos1[:idx_1]

            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"')
            value = str_pos1[:idx_1]
            self.do_update("City {} {} {}".format(id_str, key, value))

    def do_Amenity(self, arg):
        """ all, instance count, show, and update functions """
        if arg == '.all()':
            self.do_all('Amenity')
        if arg == '.count()':
            self.count('Amenity')
        if arg.startswith('.show(') is True:
            idx_1 = arg.index('"') + 1
            str_pos1 = arg[idx_1:]
            idx_2 = str_pos1.index('"')
            id_str = str_pos1[:idx_2]
            self.do_show("Amenity {}".format(id_str))
        if arg.startswith('.update(') is True:
            idx_1 = arg.index('"') + 1
            str_pos1 = arg[idx_1:]
            idx_2 = str_pos1.index('"')
            id_str = str_pos1[:idx_2]

            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"')
            key = str_pos1[:idx_1]

            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"')
            value = str_pos1[:idx_1]
            self.do_update("Amenity {} {} {}".format(id_str, key, value))

    def do_Place(self, arg):
        """ all, instance count, show, and update functions """
        if arg == '.all()':
            self.do_all('Place')
        if arg == '.count()':
            self.count('Place')
        if arg.startswith('.show(') is True:
            idx_1 = arg.index('"') + 1
            str_pos1 = arg[idx_1:]
            idx_2 = str_pos1.index('"')
            id_str = str_pos1[:idx_2]
            self.do_show("Place {}".format(id_str))
        if arg.startswith('.update(') is True:
            idx_1 = arg.index('"') + 1
            str_pos1 = arg[idx_1:]
            idx_2 = str_pos1.index('"')
            id_str = str_pos1[:idx_2]

            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"')
            key = str_pos1[:idx_1]

            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"')
            value = str_pos1[:idx_1]
            self.do_update("Place {} {} {}".format(id_str, key, value))

    def do_Review(self, arg):
        """ all, instance count, show, and update functions """
        if arg == '.all()':
            self.do_all('Review')
        if arg == '.count()':
            self.count('Review')
        if arg.startswith('.show(') is True:
            idx_1 = arg.index('"') + 1
            str_pos1 = arg[idx_1:]
            idx_2 = str_pos1.index('"')
            id_str = str_pos1[:idx_2]
            self.do_show("Review {}".format(id_str))
        if arg.startswith('.update(') is True:
            idx_1 = arg.index('"') + 1
            str_pos1 = arg[idx_1:]
            idx_2 = str_pos1.index('"')
            id_str = str_pos1[:idx_2]

            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"')
            key = str_pos1[:idx_1]

            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"') + 1
            str_pos1 = str_pos1[idx_1:]
            idx_1 = str_pos1.index('"')
            value = str_pos1[:idx_1]
            self.do_update("Review {} {} {}".format(id_str, key, value))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
