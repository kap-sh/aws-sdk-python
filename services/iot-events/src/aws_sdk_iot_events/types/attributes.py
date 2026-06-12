"""Generated from Smithy shape ``com.amazonaws.iotevents#Attributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.attribute

Attributes: TypeAlias = list["aws_sdk_iot_events.types.attribute.Attribute"]


# --- restJson1 ser/de ---
def serialize_json(value: Attributes) -> list:
    import aws_sdk_iot_events.types.attribute

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_events.types.attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> Attributes:
    import aws_sdk_iot_events.types.attribute

    out: Attributes = []
    for item in data:
        out.append(aws_sdk_iot_events.types.attribute.deserialize_json(item))
    return out
