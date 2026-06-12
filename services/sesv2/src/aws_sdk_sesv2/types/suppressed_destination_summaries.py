"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressedDestinationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.suppressed_destination_summary

SuppressedDestinationSummaries: TypeAlias = list[
    "aws_sdk_sesv2.types.suppressed_destination_summary.SuppressedDestinationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuppressedDestinationSummaries) -> list:
    import aws_sdk_sesv2.types.suppressed_destination_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sesv2.types.suppressed_destination_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SuppressedDestinationSummaries:
    import aws_sdk_sesv2.types.suppressed_destination_summary

    out: SuppressedDestinationSummaries = []
    for item in data:
        out.append(
            aws_sdk_sesv2.types.suppressed_destination_summary.deserialize_json(item)
        )
    return out
