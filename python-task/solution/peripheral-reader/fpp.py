
'''

FPP (Fake Policumbent Peripheral)

Library to interface with the peripheral

'''


from abc import abstractmethod




class Peripheral:

    def __init__(self, device_path):
        """
        Construct a new fpp.Peripheral object

        :param device_path: the path corresponding to the peripheral
        :return: nothing
        """

        self.peripheral = self._open_peripheral(device_path)
        return



class Notifier:
    def __init__(self, peripheral, listeners):
        self.peripheral = peripheral
        self.listeners = listeners



class Listener:

    @abstractmethod
    def on_message_received(self, msg) -> None:
        """
        This method is called to handle the given message.
        :param msg: the delivered message
        """
        pass