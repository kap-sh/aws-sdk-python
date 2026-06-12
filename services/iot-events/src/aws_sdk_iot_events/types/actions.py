"""Generated from Smithy shape ``com.amazonaws.iotevents#Actions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.action

Actions: TypeAlias = list["aws_sdk_iot_events.types.action.Action"]


# --- restJson1 ser/de ---
def serialize_json(value: Actions) -> list:
    import aws_sdk_iot_events.types.action

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_events.types.action.serialize_json(item))
    return out


def deserialize_json(data: list) -> Actions:
    import aws_sdk_iot_events.types.action

    out: Actions = []
    for item in data:
        out.append(aws_sdk_iot_events.types.action.deserialize_json(item))
    return out
