"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectMembers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.project_member

ProjectMembers: TypeAlias = list["capo_datazone.types.project_member.ProjectMember"]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectMembers) -> list:
    import capo_datazone.types.project_member

    out: list = []
    for item in value:
        out.append(capo_datazone.types.project_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProjectMembers:
    import capo_datazone.types.project_member

    out: ProjectMembers = []
    for item in data:
        out.append(capo_datazone.types.project_member.deserialize_json(item))
    return out
