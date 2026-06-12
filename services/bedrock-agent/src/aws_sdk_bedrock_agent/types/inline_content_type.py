"""Generated from Smithy shape ``com.amazonaws.bedrockagent#InlineContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

InlineContentType: TypeAlias = Literal[
    "BYTE",
    "TEXT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BYTE",
        "TEXT",
    )
)


def serialize_json(value: InlineContentType) -> str:
    return value


def deserialize_json(data: str) -> InlineContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InlineContentType value: {data!r}")
    return cast(InlineContentType, data)
