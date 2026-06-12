"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventStreamSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.event_stream_summary

EventStreamSummaryList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.event_stream_summary.EventStreamSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventStreamSummaryList) -> list:
    import aws_sdk_customer_profiles.types.event_stream_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.event_stream_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EventStreamSummaryList:
    import aws_sdk_customer_profiles.types.event_stream_summary

    out: EventStreamSummaryList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.event_stream_summary.deserialize_json(item)
        )
    return out
