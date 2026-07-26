"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_version

ImageVersionList: TypeAlias = list["capo_imagebuilder.types.image_version.ImageVersion"]


# --- restJson1 ser/de ---
def serialize_json(value: ImageVersionList) -> list:
    import capo_imagebuilder.types.image_version

    out: list = []
    for item in value:
        out.append(capo_imagebuilder.types.image_version.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImageVersionList:
    import capo_imagebuilder.types.image_version

    out: ImageVersionList = []
    for item in data:
        out.append(capo_imagebuilder.types.image_version.deserialize_json(item))
    return out
