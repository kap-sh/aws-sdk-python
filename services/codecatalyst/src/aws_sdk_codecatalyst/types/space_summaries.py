"""Generated from Smithy shape ``com.amazonaws.codecatalyst#SpaceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.space_summary

SpaceSummaries: TypeAlias = list[
    "aws_sdk_codecatalyst.types.space_summary.SpaceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SpaceSummaries) -> list:
    import aws_sdk_codecatalyst.types.space_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_codecatalyst.types.space_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpaceSummaries:
    import aws_sdk_codecatalyst.types.space_summary

    out: SpaceSummaries = []
    for item in data:
        out.append(aws_sdk_codecatalyst.types.space_summary.deserialize_json(item))
    return out
