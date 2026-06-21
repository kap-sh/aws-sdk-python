"""Generated from Smithy shape ``com.amazonaws.managedblockchain#StateDBType``."""

from typing import Literal, TypeAlias, cast

StateDBType: TypeAlias = Literal[
    "LevelDB",
    "CouchDB",
]


# --- restJson1 ser/de ---
def serialize_json(value: StateDBType) -> str:
    return value


def deserialize_json(data: str) -> StateDBType:
    return cast(StateDBType, data)
