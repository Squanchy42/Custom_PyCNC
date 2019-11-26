# -----------------------------------------------------------------------------
# Hardware config.

import math

# neue Parameter fuer Delta-Logik
distance_pivot_carriage_mm = dict()
radius_heatbed = 200
height_pivot_tool_mm = 50
height_carriage_mm = dict()
length_arm = {'a': 300, 'b': 300, 'c': 300}
distance_pivot_tool_mm = 50


# Startwerte der carriage high (tx, ty, tz = 0)
distance_pivot_carriage_mm.a = math.sqrt((radius_heatbed - (0 + distance_pivot_tool_mm)) ** + (0 - 0) ** 2)
height_carriage_mm.a = 0 + height_pivot_tool_mm + math.sqrt(length_arm.a ** 2 - distance_pivot_carriage_mm.a ** 2)
distance_pivot_carriage_mm.b = math.sqrt((radius_heatbed * math.cos(120)
                                    - (0 + distance_pivot_tool_mm * math.cos(120))) ** 2
                                    + (radius_heatbed * math.sin(120) - (0 + distance_pivot_tool_mm
                                    * math.sin(120))) ** 2)
height_carriage_mm.b = 0 + height_pivot_tool_mm + math.sqrt(length_arm.b ** 2 - distance_pivot_carriage_mm.b ** 2)
distance_pivot_carriage_mm.c = math.sqrt((radius_heatbed * math.cos(240)
                                    - (0 + distance_pivot_tool_mm * math.cos(240))) ** 2
                                    + (radius_heatbed * math.sin(240) - (0 + distance_pivot_tool_mm
                                    * math.sin(240))) ** 2)
height_carriage_mm.c = 0 + height_pivot_tool_mm + math.sqrt(length_arm.c ** 2 - distance_pivot_carriage_mm.c ** 2)

distance_mm = dict()
height_carriage_mm_old = dict()

# Maximum velocity for each axis in millimeter per minute.
MAX_VELOCITY_MM_PER_MIN_X = 24000
MAX_VELOCITY_MM_PER_MIN_Y = 12000
MAX_VELOCITY_MM_PER_MIN_Z = 600
MAX_VELOCITY_MM_PER_MIN_E = 1500
MIN_VELOCITY_MM_PER_MIN = 1
# Average velocity for endstop calibration procedure
CALIBRATION_VELOCITY_MM_PER_MIN = 300

# Stepper motors steps per millimeter for each axis.
STEPPER_PULSES_PER_MM_X = 100
STEPPER_PULSES_PER_MM_Y = 100
STEPPER_PULSES_PER_MM_Z = 400
STEPPER_PULSES_PER_MM_E = 150

# Invert axises direction, by default(False) high level means increase of
# position. For inverted(True) axis, high level means decrease of position.
STEPPER_INVERTED_X = True
STEPPER_INVERTED_Y = False
STEPPER_INVERTED_Z = False
STEPPER_INVERTED_E = True

# Invert zero end stops switches. By default(False) low level on input pin
# means that axis in zero position. For inverted(True) end stops, high level
# means zero position.
ENDSTOP_INVERTED_X = True
ENDSTOP_INVERTED_Y = True
ENDSTOP_INVERTED_Z = False  # Auto leveler

# Workplace physical size.
TABLE_SIZE_X_MM = 200
TABLE_SIZE_Y_MM = 200
TABLE_SIZE_Z_MM = 220

# Mixed settings.
STEPPER_PULSE_LENGTH_US = 2
STEPPER_MAX_ACCELERATION_MM_PER_S2 = 3000  # for all axis, mm per sec^2
SPINDLE_MAX_RPM = 10000
EXTRUDER_MAX_TEMPERATURE = 250
BED_MAX_TEMPERATURE = 100
MIN_TEMPERATURE = 40
EXTRUDER_PID = {"P": 0.059161177519,
                "I": 0.00206217171374,
                "D": 0.206217171374}
BED_PID = {"P": 0.226740848076,
           "I": 0.00323956215053,
           "D": 0.323956215053}

# -----------------------------------------------------------------------------
# Pins configuration.

# Enable pin for all steppers, low level is enabled.
STEPPERS_ENABLE_PIN = 26
STEPPER_STEP_PIN_X = 21
STEPPER_STEP_PIN_Y = 16
STEPPER_STEP_PIN_Z = 12
STEPPER_STEP_PIN_E = 8

STEPPER_DIR_PIN_X = 20
STEPPER_DIR_PIN_Y = 19
STEPPER_DIR_PIN_Z = 13
STEPPER_DIR_PIN_E = 7

SPINDLE_PWM_PIN = 4
FAN_PIN = 27
EXTRUDER_HEATER_PIN = 18
BED_HEATER_PIN = 22
EXTRUDER_TEMPERATURE_SENSOR_CHANNEL = 2
BED_TEMPERATURE_SENSOR_CHANNEL = 1

ENDSTOP_PIN_X = 23
ENDSTOP_PIN_Y = 10
ENDSTOP_PIN_Z = 25

# -----------------------------------------------------------------------------
#  Behavior config

# Run command immediately after receiving and stream new pulses, otherwise
# buffer will be prepared firstly and then command will run.
# Before enabling this feature, please make sure that board performance is
# enough for streaming pulses(faster then real time).
INSTANT_RUN = True

# If this parameter is False, error will be raised on command with velocity
# more than maximum velocity specified here. If this parameter is True,
# velocity would be decreased(proportional for all axises) to fit the maximum
# velocity.
AUTO_VELOCITY_ADJUSTMENT = True

# Automatically turn on fan when extruder is heating, boolean value.
AUTO_FAN_ON = True
