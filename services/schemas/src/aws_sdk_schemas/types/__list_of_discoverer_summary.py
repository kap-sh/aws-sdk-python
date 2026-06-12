"""Generated from Smithy shape ``com.amazonaws.schemas#__listOfDiscovererSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_schemas.types.discoverer_summary

__listOfDiscovererSummary: TypeAlias = list[
    "aws_sdk_schemas.types.discoverer_summary.DiscovererSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDiscovererSummary) -> list:
    import aws_sdk_schemas.types.discoverer_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_schemas.types.discoverer_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDiscovererSummary:
    import aws_sdk_schemas.types.discoverer_summary

    out: __listOfDiscovererSummary = []
    for item in data:
        out.append(aws_sdk_schemas.types.discoverer_summary.deserialize_json(item))
    return out
