"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ProjectSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecatalyst.types.project_summary

ProjectSummaries: TypeAlias = list[
    "capo_codecatalyst.types.project_summary.ProjectSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectSummaries) -> list:
    import capo_codecatalyst.types.project_summary

    out: list = []
    for item in value:
        out.append(capo_codecatalyst.types.project_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProjectSummaries:
    import capo_codecatalyst.types.project_summary

    out: ProjectSummaries = []
    for item in data:
        out.append(capo_codecatalyst.types.project_summary.deserialize_json(item))
    return out
