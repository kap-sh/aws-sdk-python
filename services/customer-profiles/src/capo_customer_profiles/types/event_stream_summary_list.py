"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventStreamSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.event_stream_summary

EventStreamSummaryList: TypeAlias = list[
    "capo_customer_profiles.types.event_stream_summary.EventStreamSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventStreamSummaryList) -> list:
    import capo_customer_profiles.types.event_stream_summary

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.event_stream_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EventStreamSummaryList:
    import capo_customer_profiles.types.event_stream_summary

    out: EventStreamSummaryList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.event_stream_summary.deserialize_json(item)
        )
    return out
