"""Generated from Smithy shape ``com.amazonaws.sesv2#LastEngagementEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.engagement_event_type

LastEngagementEventList: TypeAlias = list[
    "capo_sesv2.types.engagement_event_type.EngagementEventType"
]


# --- restJson1 ser/de ---
def serialize_json(value: LastEngagementEventList) -> list:
    import capo_sesv2.types.engagement_event_type

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.engagement_event_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> LastEngagementEventList:
    import capo_sesv2.types.engagement_event_type

    out: LastEngagementEventList = []
    for item in data:
        out.append(capo_sesv2.types.engagement_event_type.deserialize_json(item))
    return out
