"""Generated from Smithy shape ``com.amazonaws.iotwireless#AssistPosition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.coordinate

AssistPosition: TypeAlias = list["aws_sdk_iot_wireless.types.coordinate.Coordinate"]


# --- restJson1 ser/de ---
def serialize_json(value: AssistPosition) -> list:
    return list(value)


def deserialize_json(data: list) -> AssistPosition:
    return list(data)
