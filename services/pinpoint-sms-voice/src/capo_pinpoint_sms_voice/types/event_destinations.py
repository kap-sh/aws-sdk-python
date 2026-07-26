"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#EventDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice.types.event_destination

EventDestinations: TypeAlias = list[
    "capo_pinpoint_sms_voice.types.event_destination.EventDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventDestinations) -> list:
    import capo_pinpoint_sms_voice.types.event_destination

    out: list = []
    for item in value:
        out.append(capo_pinpoint_sms_voice.types.event_destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventDestinations:
    import capo_pinpoint_sms_voice.types.event_destination

    out: EventDestinations = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice.types.event_destination.deserialize_json(item)
        )
    return out
