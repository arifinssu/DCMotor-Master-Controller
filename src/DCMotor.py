import minimalmodbus

class DCMotor:
    def __init__(self, address, baud, port):
        self.device = minimalmodbus.Instrument(port, address)
        self.device.serial.baudrate = baud
        self.device.close_port_after_each_call = False

    def set_pool(self, address, state):
        try:
            self.device.write_register(address, int(state), 0)
            return True

        except:
            return False

    def start(self):
        self.set_pool(0, 1)

    def stop(self):
        self.set_pool(0, 0)

    def set_direction(self, val):
        self.set_pool(1, val)

    def set_speed(self, val):
        self.set_pool(2, val)

    def set_accel(self, val):
        self.set_pool(3, val)

    def close_port(self, device):
        self.close_port = True
        return