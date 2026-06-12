"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#EventTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.event_type

EventTypes: TypeAlias = list["aws_sdk_pinpoint_sms_voice.types.event_type.EventType"]


# --- restJson1 ser/de ---
def serialize_json(value: EventTypes) -> list:
    import aws_sdk_pinpoint_sms_voice.types.event_type

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint_sms_voice.types.event_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventTypes:
    import aws_sdk_pinpoint_sms_voice.types.event_type

    out: EventTypes = []
    for item in data:
        out.append(aws_sdk_pinpoint_sms_voice.types.event_type.deserialize_json(item))
    return out
