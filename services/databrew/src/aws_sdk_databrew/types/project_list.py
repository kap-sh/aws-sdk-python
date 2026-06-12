"""Generated from Smithy shape ``com.amazonaws.databrew#ProjectList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_databrew.types.project

ProjectList: TypeAlias = list["aws_sdk_databrew.types.project.Project"]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectList) -> list:
    import aws_sdk_databrew.types.project

    out: list = []
    for item in value:
        out.append(aws_sdk_databrew.types.project.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProjectList:
    import aws_sdk_databrew.types.project

    out: ProjectList = []
    for item in data:
        out.append(aws_sdk_databrew.types.project.deserialize_json(item))
    return out
