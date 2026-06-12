"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.property_summary

PropertySummaries: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.property_summary.PropertySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PropertySummaries) -> list:
    import aws_sdk_iottwinmaker.types.property_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iottwinmaker.types.property_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PropertySummaries:
    import aws_sdk_iottwinmaker.types.property_summary

    out: PropertySummaries = []
    for item in data:
        out.append(aws_sdk_iottwinmaker.types.property_summary.deserialize_json(item))
    return out
