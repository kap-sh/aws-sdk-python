"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageType``."""

from typing import Literal, TypeAlias, cast

ImageType: TypeAlias = Literal[
    "AMI",
    "DOCKER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageType) -> str:
    return value


def deserialize_json(data: str) -> ImageType:
    return cast(ImageType, data)
