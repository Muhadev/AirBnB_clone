#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Set a custom prompt for the command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter using EOF (Ctrl-D)"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def help_quit(self):
        """Print help message for quit command"""
        print("Quit command to exit the program")

if __name__ == '__main__':
    """Instantiate HBNBCommand and start the command loop"""
    HBNBCommand().cmdloop()
