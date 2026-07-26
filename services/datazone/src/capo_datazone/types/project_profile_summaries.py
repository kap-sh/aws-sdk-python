"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectProfileSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.project_profile_summary

ProjectProfileSummaries: TypeAlias = list[
    "capo_datazone.types.project_profile_summary.ProjectProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectProfileSummaries) -> list:
    import capo_datazone.types.project_profile_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.project_profile_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProjectProfileSummaries:
    import capo_datazone.types.project_profile_summary

    out: ProjectProfileSummaries = []
    for item in data:
        out.append(capo_datazone.types.project_profile_summary.deserialize_json(item))
    return out
