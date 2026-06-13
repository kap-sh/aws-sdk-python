"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultContentColumnType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

RetrievalResultContentColumnType: TypeAlias = Literal[
    "BLOB",
    "BOOLEAN",
    "DOUBLE",
    "NULL",
    "LONG",
    "STRING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLOB",
        "BOOLEAN",
        "DOUBLE",
        "NULL",
        "LONG",
        "STRING",
    )
)


def serialize_json(value: RetrievalResultContentColumnType) -> str:
    return value


def deserialize_json(data: str) -> RetrievalResultContentColumnType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RetrievalResultContentColumnType value: {data!r}"
        )
    return cast(RetrievalResultContentColumnType, data)
