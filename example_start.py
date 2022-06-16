from src.DCMotor import DCMotor
conveyor = DCMotor(11, 9600, "COM4")

if __name__ == "__main__":
    try:
        conveyor.start()

    except Exception as e:
        conveyor.stop()
        conveyor.close_port()
        print(e)
        

    except KeyboardInterrupt:
        print("exit")
        conveyor.stop()
        conveyor.close_port()