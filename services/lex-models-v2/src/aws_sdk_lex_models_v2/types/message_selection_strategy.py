"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#MessageSelectionStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

MessageSelectionStrategy: TypeAlias = Literal[
    "Random",
    "Ordered",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Random",
        "Ordered",
    )
)


def serialize_json(value: MessageSelectionStrategy) -> str:
    return value


def deserialize_json(data: str) -> MessageSelectionStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageSelectionStrategy value: {data!r}")
    return cast(MessageSelectionStrategy, data)
