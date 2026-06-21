"""Generated from Smithy shape ``com.amazonaws.managedblockchain#VoteValue``."""

from typing import Literal, TypeAlias, cast

VoteValue: TypeAlias = Literal[
    "YES",
    "NO",
]


# --- restJson1 ser/de ---
def serialize_json(value: VoteValue) -> str:
    return value


def deserialize_json(data: str) -> VoteValue:
    return cast(VoteValue, data)
