"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InputImageFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

InputImageFormat: TypeAlias = Literal[
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


def serialize_json(value: InputImageFormat) -> str:
    return value


def deserialize_json(data: str) -> InputImageFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputImageFormat value: {data!r}")
    return cast(InputImageFormat, data)
