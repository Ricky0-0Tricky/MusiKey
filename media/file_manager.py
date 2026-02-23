class FileManager:
    """ 
    File Manager to Manage and Control
    All Kinds of File Operations
    needed by this Project.
    """

    def __init__(self):
        """ 
        Default Constructor

        :param self: FileManager Object 
        """
        pass

    def run(self, file) -> bool:
        """
        Method to run the File Manager.
        
        :return: Success of the Operation
        :rtype: bool
        """
        pass

    def save_file(self, file: str) -> None:
        """
        Method to Save a Given File in
        the Tracks Directory.

        :param self: FileManager Object
        :param file: Path to the File
        """
        pass

    def is_valid(self, file) -> bool:
        """
        Method to Check if the File is valid
        to be saved.

        :param self: FileManager Object
        :param file: Path to the File
        :return: If the File is valid to save
        :rtype: bool
        """
        pass

    def is_valid_format(self, type: str) -> bool:
        """
        Method to Check if the File is in
        the expected format.

        :param self: FileManager Object
        :param type: File Type of the given File
        :return: If the File is in the correct format
        :rtype: bool
        """
        pass

    def is_valid_length(self, length: float) -> bool:
        """
        Method to Check if the File is Valid
        in terms of length.

        :param self: FileManager Object
        :param length: Length of the File
        :return: If the File is long enough to be saved
        :rtype: bool
        """
        pass

    def get_file_details(self, file) -> dict:
        """ 
        Method to Obtain All Relevant Bits of Info
        about a File.

        :param self: FileManager Object
        :param file: Path to the File
        :return: Dictionaire with File Info
        :rtype: dict
        """
        pass