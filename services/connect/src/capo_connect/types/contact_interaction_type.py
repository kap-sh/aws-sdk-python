"""Generated from Smithy shape ``com.amazonaws.connect#ContactInteractionType``."""

from typing import Literal, TypeAlias, cast

ContactInteractionType: TypeAlias = Literal[
    "AGENT",
    "AUTOMATED",
    "CUSTOMER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactInteractionType) -> str:
    return value


def deserialize_json(data: str) -> ContactInteractionType:
    return cast(ContactInteractionType, data)
