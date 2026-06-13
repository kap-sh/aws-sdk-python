"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.project_id

ProjectIds: TypeAlias = list["aws_sdk_datazone.types.project_id.ProjectId"]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectIds) -> list:
    return list(value)


def deserialize_json(data: list) -> ProjectIds:
    return list(data)
