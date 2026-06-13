"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectMembers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.project_member

ProjectMembers: TypeAlias = list["aws_sdk_datazone.types.project_member.ProjectMember"]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectMembers) -> list:
    import aws_sdk_datazone.types.project_member

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.project_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProjectMembers:
    import aws_sdk_datazone.types.project_member

    out: ProjectMembers = []
    for item in data:
        out.append(aws_sdk_datazone.types.project_member.deserialize_json(item))
    return out
