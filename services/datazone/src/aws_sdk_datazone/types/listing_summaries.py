"""Generated from Smithy shape ``com.amazonaws.datazone#ListingSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.listing_summary

ListingSummaries: TypeAlias = list[
    "aws_sdk_datazone.types.listing_summary.ListingSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListingSummaries) -> list:
    import aws_sdk_datazone.types.listing_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.listing_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListingSummaries:
    import aws_sdk_datazone.types.listing_summary

    out: ListingSummaries = []
    for item in data:
        out.append(aws_sdk_datazone.types.listing_summary.deserialize_json(item))
    return out
