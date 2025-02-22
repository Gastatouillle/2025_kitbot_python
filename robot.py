import wpilib
import rev
import wpilib.drive

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        #declare controller
        self.controller = wpilib.XboxController(0)

        #declare all drive motors
        self.FLDrive = rev.SparkMax(1, rev.SparkLowLevel.MotorType.kBrushed)
        self.FRDrive = rev.SparkMax(2, rev.SparkLowLevel.MotorType.kBrushed)
        self.RRDrive = rev.SparkMax(3, rev.SparkLowLevel.MotorType.kBrushed)
        self.RLDrive = rev.SparkMax(4, rev.SparkLowLevel.MotorType.kBrushed)

        #create groups for left and right drivetrains
        self.LeftDrive = wpilib.MotorControllerGroup(self.FLDrive, self.FRDrive)
        self.RightDrive = wpilib.MotorControllerGroup(self.RLDrive, self.RRDrive)

        #set up drivetrain
        self.drive = wpilib.drive.DifferentialDrive(
            self.LeftDrive,
            self.RightDrive
        )

    def driveRobot(self, speed, rot):
        #drive robot with supplied values
        self.drive.arcadeDrive(speed, rot)

    def teleopPeriodic(self):
        # Get the x speed. We are inverting this because Xbox controllers return
        # negative values when we push forward.
        xSpeed = (
            -self.controller.getLeftY()
        )

        rot = (
            self.controller.getRightX()
        )

        self.driveRobot(xSpeed, rot)