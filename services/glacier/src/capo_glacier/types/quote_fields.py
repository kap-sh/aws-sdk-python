"""Generated from Smithy shape ``com.amazonaws.glacier#QuoteFields``."""

from typing import Literal, TypeAlias, cast

QuoteFields: TypeAlias = Literal[
    "ALWAYS",
    "ASNEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuoteFields) -> str:
    return value


def deserialize_json(data: str) -> QuoteFields:
    return cast(QuoteFields, data)
