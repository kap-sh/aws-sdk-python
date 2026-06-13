"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#SubjectSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.subject_summary

SubjectSummaries: TypeAlias = list[
    "aws_sdk_rolesanywhere.types.subject_summary.SubjectSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubjectSummaries) -> list:
    import aws_sdk_rolesanywhere.types.subject_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_rolesanywhere.types.subject_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubjectSummaries:
    import aws_sdk_rolesanywhere.types.subject_summary

    out: SubjectSummaries = []
    for item in data:
        out.append(aws_sdk_rolesanywhere.types.subject_summary.deserialize_json(item))
    return out
