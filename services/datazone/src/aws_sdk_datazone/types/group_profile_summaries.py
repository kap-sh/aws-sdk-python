"""Generated from Smithy shape ``com.amazonaws.datazone#GroupProfileSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.group_profile_summary

GroupProfileSummaries: TypeAlias = list[
    "aws_sdk_datazone.types.group_profile_summary.GroupProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupProfileSummaries) -> list:
    import aws_sdk_datazone.types.group_profile_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.group_profile_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupProfileSummaries:
    import aws_sdk_datazone.types.group_profile_summary

    out: GroupProfileSummaries = []
    for item in data:
        out.append(aws_sdk_datazone.types.group_profile_summary.deserialize_json(item))
    return out
