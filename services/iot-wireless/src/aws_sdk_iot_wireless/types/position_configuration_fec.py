"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionConfigurationFec``."""

from typing import Literal, TypeAlias, cast

PositionConfigurationFec: TypeAlias = Literal[
    "ROSE",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PositionConfigurationFec) -> str:
    return value


def deserialize_json(data: str) -> PositionConfigurationFec:
    return cast(PositionConfigurationFec, data)
