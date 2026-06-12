"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#Variables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.variable

Variables: TypeAlias = list["aws_sdk_iot_events_data.types.variable.Variable"]


# --- restJson1 ser/de ---
def serialize_json(value: Variables) -> list:
    import aws_sdk_iot_events_data.types.variable

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_events_data.types.variable.serialize_json(item))
    return out


def deserialize_json(data: list) -> Variables:
    import aws_sdk_iot_events_data.types.variable

    out: Variables = []
    for item in data:
        out.append(aws_sdk_iot_events_data.types.variable.deserialize_json(item))
    return out
