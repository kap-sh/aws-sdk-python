"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#MessageSelectionStrategy``."""

from typing import Literal, TypeAlias, cast

MessageSelectionStrategy: TypeAlias = Literal[
    "Random",
    "Ordered",
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageSelectionStrategy) -> str:
    return value


def deserialize_json(data: str) -> MessageSelectionStrategy:
    return cast(MessageSelectionStrategy, data)
