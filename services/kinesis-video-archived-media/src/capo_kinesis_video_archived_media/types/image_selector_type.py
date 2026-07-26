"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#ImageSelectorType``."""

from typing import Literal, TypeAlias, cast

ImageSelectorType: TypeAlias = Literal[
    "PRODUCER_TIMESTAMP",
    "SERVER_TIMESTAMP",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageSelectorType) -> str:
    return value


def deserialize_json(data: str) -> ImageSelectorType:
    return cast(ImageSelectorType, data)
