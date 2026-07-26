"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#EventDestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.event_destination

EventDestinationList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.event_destination.EventDestination"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventDestinationList) -> list:
    import capo_pinpoint_sms_voice_v2.types.event_destination

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.event_destination.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EventDestinationList:
    import capo_pinpoint_sms_voice_v2.types.event_destination

    out: EventDestinationList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.event_destination.deserialize_aws_json_1_0(
                item
            )
        )
    return out
