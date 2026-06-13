"""Generated from Smithy shape ``com.amazonaws.omics#ImageMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.image_mapping

ImageMappingsList: TypeAlias = list["aws_sdk_omics.types.image_mapping.ImageMapping"]


# --- restJson1 ser/de ---
def serialize_json(value: ImageMappingsList) -> list:
    import aws_sdk_omics.types.image_mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.image_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImageMappingsList:
    import aws_sdk_omics.types.image_mapping

    out: ImageMappingsList = []
    for item in data:
        out.append(aws_sdk_omics.types.image_mapping.deserialize_json(item))
    return out
