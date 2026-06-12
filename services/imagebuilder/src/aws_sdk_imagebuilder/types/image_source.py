"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

ImageSource: TypeAlias = Literal[
    "AMAZON_MANAGED",
    "AWS_MARKETPLACE",
    "IMPORTED",
    "CUSTOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AMAZON_MANAGED",
        "AWS_MARKETPLACE",
        "IMPORTED",
        "CUSTOM",
    )
)


def serialize_json(value: ImageSource) -> str:
    return value


def deserialize_json(data: str) -> ImageSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageSource value: {data!r}")
    return cast(ImageSource, data)
