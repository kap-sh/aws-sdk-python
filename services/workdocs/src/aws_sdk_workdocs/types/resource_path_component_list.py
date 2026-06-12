"""Generated from Smithy shape ``com.amazonaws.workdocs#ResourcePathComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.resource_path_component

ResourcePathComponentList: TypeAlias = list[
    "aws_sdk_workdocs.types.resource_path_component.ResourcePathComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePathComponentList) -> list:
    import aws_sdk_workdocs.types.resource_path_component

    out: list = []
    for item in value:
        out.append(aws_sdk_workdocs.types.resource_path_component.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourcePathComponentList:
    import aws_sdk_workdocs.types.resource_path_component

    out: ResourcePathComponentList = []
    for item in data:
        out.append(
            aws_sdk_workdocs.types.resource_path_component.deserialize_json(item)
        )
    return out
