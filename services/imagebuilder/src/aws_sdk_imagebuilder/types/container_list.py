"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ContainerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.container

ContainerList: TypeAlias = list["aws_sdk_imagebuilder.types.container.Container"]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerList) -> list:
    import aws_sdk_imagebuilder.types.container

    out: list = []
    for item in value:
        out.append(aws_sdk_imagebuilder.types.container.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContainerList:
    import aws_sdk_imagebuilder.types.container

    out: ContainerList = []
    for item in data:
        out.append(aws_sdk_imagebuilder.types.container.deserialize_json(item))
    return out
