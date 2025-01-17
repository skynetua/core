"""Constants for the Balboa Spa Client integration."""
import logging

from homeassistant.components.climate.const import (
    FAN_HIGH,
    FAN_LOW,
    FAN_MEDIUM,
    FAN_OFF,
    HVAC_MODE_AUTO,
    HVAC_MODE_HEAT,
    HVAC_MODE_OFF,
)
from homeassistant.components.fan import SPEED_HIGH, SPEED_LOW, SPEED_OFF

_LOGGER = logging.getLogger(__name__)

DOMAIN = "balboa"

CLIMATE_SUPPORTED_FANSTATES = [FAN_OFF, FAN_LOW, FAN_MEDIUM, FAN_HIGH]
CLIMATE_SUPPORTED_MODES = [HVAC_MODE_AUTO, HVAC_MODE_HEAT, HVAC_MODE_OFF]
CONF_SYNC_TIME = "sync_time"
DEFAULT_SYNC_TIME = False
FAN_SUPPORTED_SPEEDS = [SPEED_OFF, SPEED_LOW, SPEED_HIGH]
PLATFORMS = ["binary_sensor", "climate"]

AUX = "Aux"
CIRC_PUMP = "Circ Pump"
CLIMATE = "Climate"
FILTER = "Filter"
LIGHT = "Light"
MISTER = "Mister"
PUMP = "Pump"
TEMP_RANGE = "Temp Range"

SIGNAL_UPDATE = "balboa_update_{}"
