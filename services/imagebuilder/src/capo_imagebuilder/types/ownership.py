"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Ownership``."""

from typing import Literal, TypeAlias, cast

Ownership: TypeAlias = Literal[
    "Self",
    "Shared",
    "Amazon",
    "ThirdParty",
    "AWSMarketplace",
]


# --- restJson1 ser/de ---
def serialize_json(value: Ownership) -> str:
    return value


def deserialize_json(data: str) -> Ownership:
    return cast(Ownership, data)
