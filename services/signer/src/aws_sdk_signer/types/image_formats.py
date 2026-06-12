"""Generated from Smithy shape ``com.amazonaws.signer#ImageFormats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_signer.types.image_format

ImageFormats: TypeAlias = list["aws_sdk_signer.types.image_format.ImageFormat"]


# --- restJson1 ser/de ---
def serialize_json(value: ImageFormats) -> list:
    import aws_sdk_signer.types.image_format

    out: list = []
    for item in value:
        out.append(aws_sdk_signer.types.image_format.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImageFormats:
    import aws_sdk_signer.types.image_format

    out: ImageFormats = []
    for item in data:
        out.append(aws_sdk_signer.types.image_format.deserialize_json(item))
    return out
