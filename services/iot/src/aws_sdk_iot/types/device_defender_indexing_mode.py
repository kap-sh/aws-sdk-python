"""Generated from Smithy shape ``com.amazonaws.iot#DeviceDefenderIndexingMode``."""

from typing import Literal, TypeAlias, cast

DeviceDefenderIndexingMode: TypeAlias = Literal[
    "OFF",
    "VIOLATIONS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceDefenderIndexingMode) -> str:
    return value


def deserialize_json(data: str) -> DeviceDefenderIndexingMode:
    return cast(DeviceDefenderIndexingMode, data)
