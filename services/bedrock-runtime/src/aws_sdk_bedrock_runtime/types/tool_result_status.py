"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolResultStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

ToolResultStatus: TypeAlias = Literal[
    "success",
    "error",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "success",
        "error",
    )
)


def serialize_json(value: ToolResultStatus) -> str:
    return value


def deserialize_json(data: str) -> ToolResultStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ToolResultStatus value: {data!r}")
    return cast(ToolResultStatus, data)
