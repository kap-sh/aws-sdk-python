"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImagePackageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_package

ImagePackageList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.image_package.ImagePackage"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImagePackageList) -> list:
    import aws_sdk_imagebuilder.types.image_package

    out: list = []
    for item in value:
        out.append(aws_sdk_imagebuilder.types.image_package.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImagePackageList:
    import aws_sdk_imagebuilder.types.image_package

    out: ImagePackageList = []
    for item in data:
        out.append(aws_sdk_imagebuilder.types.image_package.deserialize_json(item))
    return out
