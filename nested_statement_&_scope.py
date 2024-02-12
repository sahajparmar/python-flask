# Global vs Local Variable in Function


x = "outside"


def report():
    x = "inside"
    return x


print(report())
print(x)


# LEGB  RULE

# LEGB Rule Demonstration - Local Scope


def report():
    x = "local"
    print(x)

    # LEGB Rule Demonstration - Enclosing Scope


x = "THIS IS GLOBAL LEVEL"


def enclosing():
    x = "enclosing level"

    def inside():
        # LEGB
        x = "local"
        print(x)

    inside()


enclosing()

# Global Variable Access and Modification

x = "outside"


def report():
    # grab the global level x variable!
    #    global x
    # reassign global
    x = "inside"
    return x


print(report())
print(x)
