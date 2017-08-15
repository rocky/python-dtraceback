import sys, dtraceback

def lumberjack():
    bright_side_of_death()

def bright_side_of_death():
    return tuple()[0]

try:
    lumberjack()
except IndexError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    # print("*** print_tb:")
    # dtraceback.print_tb(exc_traceback, file=sys.stdout)
    print("*** print_tb verbose 1:")
    dtraceback.print_tb(exc_traceback, file=sys.stdout, verbosity=1)
    print("*** print_tb verbose 2:")
    dtraceback.print_tb(exc_traceback, file=sys.stdout, verbosity=2)
    print("*** print_exception:")
