#!/usr/bin/python
import gobject

def main():
    # Initialize mainloop
    gobject.threads_init()
    mainloop = gobject.MainLoop()  

    # Run mainloop
    mainloop.run()                


if __name__ == '__main__':
    main()        
