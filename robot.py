import wpilib
import rev
import wpilib.drive

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.controller = wpilib.XboxController(0)


        self.FLDrive = rev.SparkMax(1, rev.SparkLowLevel.MotorType.kBrushed)
        self.FRDrive = rev.SparkMax(2, rev.SparkLowLevel.MotorType.kBrushed)
        self.RRDrive = rev.SparkMax(3, rev.SparkLowLevel.MotorType.kBrushed)
        self.RLDrive = rev.SparkMax(4, rev.SparkLowLevel.MotorType.kBrushed)

        self.LeftDrive = wpilib.MotorControllerGroup(self.FLDrive, self.FRDrive)
        self.RightDrive = wpilib.MotorControllerGroup(self.RLDrive, self.RRDrive)

        self.drive = wpilib.drive.DifferentialDrive(
            self.LeftDrive,
            self.RightDrive
        )

    def driveRobot(self, speed, rot):
        self.drive.arcadeDrive(speed, rot)

    def teleopPeriodic(self):
        # Get the x speed. We are inverting this because Xbox controllers return
        # negative values when we push forward.
        xSpeed = (
            -self.controller.getLeftY()
        )

        # Get the rate of angular rotation. We are inverting this because we want a
        # positive value when we pull to the left (remember, CCW is positive in
        # mathematics). Xbox controllers return positive values when you pull to
        # the right by default.
        rot = (
            self.controller.getRightX()
        )

        self.driveRobot(xSpeed, rot)