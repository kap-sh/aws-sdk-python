"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ImageStandardGenerativeFieldType``."""

from typing import Literal, TypeAlias, cast

ImageStandardGenerativeFieldType: TypeAlias = Literal[
    "IMAGE_SUMMARY",
    "IAB",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageStandardGenerativeFieldType) -> str:
    return value


def deserialize_json(data: str) -> ImageStandardGenerativeFieldType:
    return cast(ImageStandardGenerativeFieldType, data)
