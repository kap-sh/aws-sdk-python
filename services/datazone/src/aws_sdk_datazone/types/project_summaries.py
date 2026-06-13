"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.project_summary

ProjectSummaries: TypeAlias = list[
    "aws_sdk_datazone.types.project_summary.ProjectSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectSummaries) -> list:
    import aws_sdk_datazone.types.project_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.project_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProjectSummaries:
    import aws_sdk_datazone.types.project_summary

    out: ProjectSummaries = []
    for item in data:
        out.append(aws_sdk_datazone.types.project_summary.deserialize_json(item))
    return out
