class MediaPlayer:
    """ 
    Media Player to Play and Control
    All Kinds of Media Playing Operations 
    needed by this Project. 
    """

    def __init__(self, delay:int=500):
        """ 
        Parametrized Constructor. 

        :param self: MediaPlayer Object
        :param delay: Desired Delay
        """
        pass

    def load_track(self, track: str) -> None:
        """
        Method to Load a Track In.
        
        :param self: MediaPlayer Object
        :param track: Name of the Track
        :type track: str
        """
        pass

    def unload_track(self) -> None:
        """
        Method to Unload a Track.
        
        :param self: MediaPlayer Object
        """
        pass

    def start(self) -> None:
        """
        Method to Start a Song.
        
        :param self: MediaPlayer Object
        """
        pass

    def stop(self) -> None:
        """
        Method to Stop a Song.
        
        :param self: MediaPlayer Object
        """
        pass

    def resume(self) -> None:
        """
        Method to Resume a Song.
        
        :param self: MediaPlayer Object
        """
        pass

    def change_volume(self, volume:float) -> None:
        """
        Method to Change Volume of the Song.
        
        :param self: MediaPlayer Object
        :param volume: Desired Volume
        :type volume: float
        """
        pass

    def change_delay(self, delay:int) -> None:
        """
        Method to Change the Delay 
        Applied to the Track.
        
        :param self: MediaPlayer Object
        :param delay: Desired Delay
        :type delay: int
        """
        pass

    def get_track_state(self) -> bool:
        """
        Method to Obtain the Track's State.

        :param self: MediaPlayer Object
        :return: Current State of The Track
        :rtype: bool 
        """
        pass

    def get_track_time(self) -> None | int:
        """
        Method to Obtain the Track's Duration. 
        
        :param self: MediaPlayer Object
        :return: Track's duration in seconds
        :rtype: int | None
        """
        pass