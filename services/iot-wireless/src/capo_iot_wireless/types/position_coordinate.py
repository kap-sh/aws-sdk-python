"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionCoordinate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.position_coordinate_value

PositionCoordinate: TypeAlias = list[
    "capo_iot_wireless.types.position_coordinate_value.PositionCoordinateValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: PositionCoordinate) -> list:
    return list(value)


def deserialize_json(data: list) -> PositionCoordinate:
    return list(data)
