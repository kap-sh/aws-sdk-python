"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

ImageType: TypeAlias = Literal[
    "AMI",
    "DOCKER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AMI",
        "DOCKER",
    )
)


def serialize_json(value: ImageType) -> str:
    return value


def deserialize_json(data: str) -> ImageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageType value: {data!r}")
    return cast(ImageType, data)
