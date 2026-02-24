from pynput import keyboard

class Piano:
    """ 
    A Simple 'Piano' that, in turn, represents 
    the keyboard of the machine that's using
    this Project. 
    """

    def __init__(self):
        """ 
        Default Constructor
        
        :param self: Piano Object
        """
        # Initializes the Keyboard Thread
        self.keyboard = keyboard.Listener(on_press=self.on_press)

    def start_listening(self):
        """ 
        Method to Start Listening. 

        :param self: Piano Object
        """
        # Declares a Keyboard Thread and starts it
        self.keyboard = keyboard.Listener(on_press=self.on_press) 
        self.keyboard.start()

    def stop_listening(self):
        """ 
        Method to Stop Listening. 

        :param self: Piano Object
        """
        # Checks if there's a Keyboard Thread alive
        if (self.keyboard is not None):
            self.keyboard.stop()

    def on_press(self, key) -> None:
        """
        On Press Keyboard Method. 

        :param self: Piano Object
        :param key: Pressed Key
        """
        # Checks if last pressed key is the same as the new one
        if (key != self.old_key): 
            # Checks if Music is playing
            # TODO: Check if the Track is Playing and act on it 
            self.old_key = key 
        pass