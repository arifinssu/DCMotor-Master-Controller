DCMotor-Master-Controller
> Modbus master controller for Driver motor dc (DRV8870) module

### Basic Usage
```py
# init calling
motor = DCMotor(address, baud, port)

# functions
motor.start()
motor.stop()
motor.set_direction(val)
motor.set_speed(val)
motor.set_accel(val)
motor.close_port()
```