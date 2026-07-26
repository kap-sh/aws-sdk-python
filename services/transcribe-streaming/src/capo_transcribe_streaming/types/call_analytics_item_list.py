"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#CallAnalyticsItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.call_analytics_item

CallAnalyticsItemList: TypeAlias = list[
    "capo_transcribe_streaming.types.call_analytics_item.CallAnalyticsItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CallAnalyticsItemList) -> list:
    import capo_transcribe_streaming.types.call_analytics_item

    out: list = []
    for item in value:
        out.append(
            capo_transcribe_streaming.types.call_analytics_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CallAnalyticsItemList:
    import capo_transcribe_streaming.types.call_analytics_item

    out: CallAnalyticsItemList = []
    for item in data:
        out.append(
            capo_transcribe_streaming.types.call_analytics_item.deserialize_json(item)
        )
    return out
