"""Generated from Smithy shape ``com.amazonaws.managedblockchain#StateDBType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_managedblockchain.errors import DeserializationError

StateDBType: TypeAlias = Literal[
    "LevelDB",
    "CouchDB",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LevelDB",
        "CouchDB",
    )
)


def serialize_json(value: StateDBType) -> str:
    return value


def deserialize_json(data: str) -> StateDBType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StateDBType value: {data!r}")
    return cast(StateDBType, data)
