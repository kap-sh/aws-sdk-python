"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteSpecificationType``."""

from typing import Literal, TypeAlias, cast

QuoteSpecificationType: TypeAlias = Literal[
    "UPDATED_RACK",
    "NEW_RACK",
    "EXISTING_RACK",
    "SERVER",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuoteSpecificationType) -> str:
    return value


def deserialize_json(data: str) -> QuoteSpecificationType:
    return cast(QuoteSpecificationType, data)
