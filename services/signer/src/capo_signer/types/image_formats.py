"""Generated from Smithy shape ``com.amazonaws.signer#ImageFormats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_signer.types.image_format

ImageFormats: TypeAlias = list["capo_signer.types.image_format.ImageFormat"]


# --- restJson1 ser/de ---
def serialize_json(value: ImageFormats) -> list:
    import capo_signer.types.image_format

    out: list = []
    for item in value:
        out.append(capo_signer.types.image_format.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImageFormats:
    import capo_signer.types.image_format

    out: ImageFormats = []
    for item in data:
        out.append(capo_signer.types.image_format.deserialize_json(item))
    return out
