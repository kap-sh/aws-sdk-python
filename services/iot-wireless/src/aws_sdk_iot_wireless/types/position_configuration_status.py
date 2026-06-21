"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

PositionConfigurationStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: PositionConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> PositionConfigurationStatus:
    return cast(PositionConfigurationStatus, data)
