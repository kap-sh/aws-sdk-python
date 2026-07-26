"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#CallAnalyticsEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.call_analytics_entity

CallAnalyticsEntityList: TypeAlias = list[
    "capo_transcribe_streaming.types.call_analytics_entity.CallAnalyticsEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: CallAnalyticsEntityList) -> list:
    import capo_transcribe_streaming.types.call_analytics_entity

    out: list = []
    for item in value:
        out.append(
            capo_transcribe_streaming.types.call_analytics_entity.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CallAnalyticsEntityList:
    import capo_transcribe_streaming.types.call_analytics_entity

    out: CallAnalyticsEntityList = []
    for item in data:
        out.append(
            capo_transcribe_streaming.types.call_analytics_entity.deserialize_json(item)
        )
    return out
