"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericSeparatorSymbol``."""

from typing import Literal, TypeAlias, cast

NumericSeparatorSymbol: TypeAlias = Literal[
    "COMMA",
    "DOT",
    "SPACE",
]


# --- restJson1 ser/de ---
def serialize_json(value: NumericSeparatorSymbol) -> str:
    return value


def deserialize_json(data: str) -> NumericSeparatorSymbol:
    return cast(NumericSeparatorSymbol, data)
