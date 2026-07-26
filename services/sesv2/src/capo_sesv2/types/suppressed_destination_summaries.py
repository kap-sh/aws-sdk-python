"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressedDestinationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.suppressed_destination_summary

SuppressedDestinationSummaries: TypeAlias = list[
    "capo_sesv2.types.suppressed_destination_summary.SuppressedDestinationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuppressedDestinationSummaries) -> list:
    import capo_sesv2.types.suppressed_destination_summary

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.suppressed_destination_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SuppressedDestinationSummaries:
    import capo_sesv2.types.suppressed_destination_summary

    out: SuppressedDestinationSummaries = []
    for item in data:
        out.append(
            capo_sesv2.types.suppressed_destination_summary.deserialize_json(item)
        )
    return out
