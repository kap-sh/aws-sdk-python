"""Generated from Smithy shape ``com.amazonaws.databrew#ProjectList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.project

ProjectList: TypeAlias = list["capo_databrew.types.project.Project"]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectList) -> list:
    import capo_databrew.types.project

    out: list = []
    for item in value:
        out.append(capo_databrew.types.project.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProjectList:
    import capo_databrew.types.project

    out: ProjectList = []
    for item in data:
        out.append(capo_databrew.types.project.deserialize_json(item))
    return out
