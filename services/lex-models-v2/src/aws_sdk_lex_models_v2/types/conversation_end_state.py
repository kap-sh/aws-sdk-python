"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationEndState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

ConversationEndState: TypeAlias = Literal[
    "Success",
    "Failure",
    "Dropped",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Success",
        "Failure",
        "Dropped",
    )
)


def serialize_json(value: ConversationEndState) -> str:
    return value


def deserialize_json(data: str) -> ConversationEndState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConversationEndState value: {data!r}")
    return cast(ConversationEndState, data)
