"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ContainerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.container

ContainerList: TypeAlias = list["capo_imagebuilder.types.container.Container"]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerList) -> list:
    import capo_imagebuilder.types.container

    out: list = []
    for item in value:
        out.append(capo_imagebuilder.types.container.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContainerList:
    import capo_imagebuilder.types.container

    out: ContainerList = []
    for item in data:
        out.append(capo_imagebuilder.types.container.deserialize_json(item))
    return out
