"""Generated from Smithy shape ``com.amazonaws.datazone#LineageEventSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.lineage_event_summary

LineageEventSummaries: TypeAlias = list[
    "aws_sdk_datazone.types.lineage_event_summary.LineageEventSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LineageEventSummaries) -> list:
    import aws_sdk_datazone.types.lineage_event_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.lineage_event_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> LineageEventSummaries:
    import aws_sdk_datazone.types.lineage_event_summary

    out: LineageEventSummaries = []
    for item in data:
        out.append(aws_sdk_datazone.types.lineage_event_summary.deserialize_json(item))
    return out
