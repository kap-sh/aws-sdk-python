"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ImageFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

ImageFormat: TypeAlias = Literal[
    "png",
    "jpeg",
    "gif",
    "webp",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "png",
        "jpeg",
        "gif",
        "webp",
    )
)


def serialize_json(value: ImageFormat) -> str:
    return value


def deserialize_json(data: str) -> ImageFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageFormat value: {data!r}")
    return cast(ImageFormat, data)
