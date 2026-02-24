import threading

class StopTimer:
    """
    Stop Timer to Control Any
    Kind of Time Operations that would
    be needed by this Project.
    """ 

    def __init__(self):
        """ 
        Parametrized Constructor 

        :param self: StopTimer Object
        """
        # Declares the StopTimer 
        self.stop_timer = None

    def on_timeout(self) -> None: 
        """ 
        On Timeout Method of the Timer. 
        
        :param self: StopTimer Object
        """
        # Called after 2 seconds of no key presses 
        self.stop_timer = None

    def start_stop_timer(self) -> None: 
        """ 
        Start Method for the Timer. 

        :param self: StopTimer Object
        """
        # Cancel previous timer if it exists 
        if (self.stop_timer is not None): 
            self.stop_timer.cancel() 
        # Always create a new timer 
        self.stop_timer = threading.Timer(2.0, self.on_timeout) 
        self.stop_timer.start()