"""Generated from Smithy shape ``com.amazonaws.bedrock#ExternalSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

ExternalSourceType: TypeAlias = Literal[
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


def serialize_json(value: ExternalSourceType) -> str:
    return value


def deserialize_json(data: str) -> ExternalSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExternalSourceType value: {data!r}")
    return cast(ExternalSourceType, data)
