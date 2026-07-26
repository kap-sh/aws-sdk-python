"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#SubjectSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rolesanywhere.types.subject_summary

SubjectSummaries: TypeAlias = list[
    "capo_rolesanywhere.types.subject_summary.SubjectSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubjectSummaries) -> list:
    import capo_rolesanywhere.types.subject_summary

    out: list = []
    for item in value:
        out.append(capo_rolesanywhere.types.subject_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubjectSummaries:
    import capo_rolesanywhere.types.subject_summary

    out: SubjectSummaries = []
    for item in data:
        out.append(capo_rolesanywhere.types.subject_summary.deserialize_json(item))
    return out
