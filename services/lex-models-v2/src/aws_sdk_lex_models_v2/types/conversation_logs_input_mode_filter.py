"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLogsInputModeFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

ConversationLogsInputModeFilter: TypeAlias = Literal[
    "Speech",
    "Text",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Speech",
        "Text",
    )
)


def serialize_json(value: ConversationLogsInputModeFilter) -> str:
    return value


def deserialize_json(data: str) -> ConversationLogsInputModeFilter:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConversationLogsInputModeFilter value: {data!r}"
        )
    return cast(ConversationLogsInputModeFilter, data)
