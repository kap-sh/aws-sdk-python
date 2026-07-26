"""Generated from Smithy shape ``com.amazonaws.iotwireless#BatteryLevel``."""

from typing import Literal, TypeAlias, cast

"""<p>Sidewalk device battery level.</p>"""
BatteryLevel: TypeAlias = Literal[
    "normal",
    "low",
    "critical",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatteryLevel) -> str:
    return value


def deserialize_json(data: str) -> BatteryLevel:
    return cast(BatteryLevel, data)
