"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ImageInputFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

ImageInputFormat: TypeAlias = Literal[
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


def serialize_json(value: ImageInputFormat) -> str:
    return value


def deserialize_json(data: str) -> ImageInputFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageInputFormat value: {data!r}")
    return cast(ImageInputFormat, data)
