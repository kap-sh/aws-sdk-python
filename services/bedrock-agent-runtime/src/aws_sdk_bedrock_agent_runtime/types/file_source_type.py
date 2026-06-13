"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FileSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

FileSourceType: TypeAlias = Literal[
    "S3",
    "BYTE_CONTENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S3",
        "BYTE_CONTENT",
    )
)


def serialize_json(value: FileSourceType) -> str:
    return value


def deserialize_json(data: str) -> FileSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileSourceType value: {data!r}")
    return cast(FileSourceType, data)
