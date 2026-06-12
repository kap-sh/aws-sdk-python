"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#ConversationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_v2.errors import DeserializationError

ConversationMode: TypeAlias = Literal[
    "AUDIO",
    "TEXT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUDIO",
        "TEXT",
    )
)


def serialize_json(value: ConversationMode) -> str:
    return value


def deserialize_json(data: str) -> ConversationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConversationMode value: {data!r}")
    return cast(ConversationMode, data)
