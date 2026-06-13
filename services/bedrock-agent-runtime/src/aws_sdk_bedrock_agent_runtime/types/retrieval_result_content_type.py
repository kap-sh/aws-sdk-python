"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

RetrievalResultContentType: TypeAlias = Literal[
    "TEXT",
    "IMAGE",
    "ROW",
    "AUDIO",
    "VIDEO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXT",
        "IMAGE",
        "ROW",
        "AUDIO",
        "VIDEO",
    )
)


def serialize_json(value: RetrievalResultContentType) -> str:
    return value


def deserialize_json(data: str) -> RetrievalResultContentType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RetrievalResultContentType value: {data!r}"
        )
    return cast(RetrievalResultContentType, data)
