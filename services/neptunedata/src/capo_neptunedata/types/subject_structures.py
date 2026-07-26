"""Generated from Smithy shape ``com.amazonaws.neptunedata#SubjectStructures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_neptunedata.types.subject_structure

SubjectStructures: TypeAlias = list[
    "capo_neptunedata.types.subject_structure.SubjectStructure"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubjectStructures) -> list:
    import capo_neptunedata.types.subject_structure

    out: list = []
    for item in value:
        out.append(capo_neptunedata.types.subject_structure.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubjectStructures:
    import capo_neptunedata.types.subject_structure

    out: SubjectStructures = []
    for item in data:
        out.append(capo_neptunedata.types.subject_structure.deserialize_json(item))
    return out
