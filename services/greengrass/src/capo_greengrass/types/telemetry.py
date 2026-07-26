"""Generated from Smithy shape ``com.amazonaws.greengrass#Telemetry``."""

from typing import Literal, TypeAlias, cast

Telemetry: TypeAlias = Literal[
    "On",
    "Off",
]


# --- restJson1 ser/de ---
def serialize_json(value: Telemetry) -> str:
    return value


def deserialize_json(data: str) -> Telemetry:
    return cast(Telemetry, data)
