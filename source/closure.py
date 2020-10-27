def create_printer(msg):

    def printer():
        print(msg)

    return printer

anne = create_printer("I like games.")
mike = create_printer("I like books.")

anne()
mike()
