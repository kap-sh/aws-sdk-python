"""Generated from Smithy shape ``com.amazonaws.appmesh#SubjectAlternativeNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.subject_alternative_name

SubjectAlternativeNameList: TypeAlias = list[
    "capo_app_mesh.types.subject_alternative_name.SubjectAlternativeName"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubjectAlternativeNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> SubjectAlternativeNameList:
    return list(data)
