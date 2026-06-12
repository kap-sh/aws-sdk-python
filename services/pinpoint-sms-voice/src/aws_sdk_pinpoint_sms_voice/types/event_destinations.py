"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#EventDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.event_destination

EventDestinations: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice.types.event_destination.EventDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventDestinations) -> list:
    import aws_sdk_pinpoint_sms_voice.types.event_destination

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice.types.event_destination.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EventDestinations:
    import aws_sdk_pinpoint_sms_voice.types.event_destination

    out: EventDestinations = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice.types.event_destination.deserialize_json(item)
        )
    return out
