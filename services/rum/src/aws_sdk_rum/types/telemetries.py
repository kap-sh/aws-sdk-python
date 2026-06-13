"""Generated from Smithy shape ``com.amazonaws.rum#Telemetries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rum.types.telemetry

Telemetries: TypeAlias = list["aws_sdk_rum.types.telemetry.Telemetry"]


# --- restJson1 ser/de ---
def serialize_json(value: Telemetries) -> list:
    return list(value)


def deserialize_json(data: list) -> Telemetries:
    return list(data)
