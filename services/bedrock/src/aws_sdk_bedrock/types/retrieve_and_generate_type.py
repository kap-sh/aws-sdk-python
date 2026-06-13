"""Generated from Smithy shape ``com.amazonaws.bedrock#RetrieveAndGenerateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

RetrieveAndGenerateType: TypeAlias = Literal[
    "KNOWLEDGE_BASE",
    "EXTERNAL_SOURCES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KNOWLEDGE_BASE",
        "EXTERNAL_SOURCES",
    )
)


def serialize_json(value: RetrieveAndGenerateType) -> str:
    return value


def deserialize_json(data: str) -> RetrieveAndGenerateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetrieveAndGenerateType value: {data!r}")
    return cast(RetrieveAndGenerateType, data)
