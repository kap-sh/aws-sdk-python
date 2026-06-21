"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicNumericSeparatorSymbol``."""

from typing import Literal, TypeAlias, cast

TopicNumericSeparatorSymbol: TypeAlias = Literal[
    "COMMA",
    "DOT",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicNumericSeparatorSymbol) -> str:
    return value


def deserialize_json(data: str) -> TopicNumericSeparatorSymbol:
    return cast(TopicNumericSeparatorSymbol, data)
