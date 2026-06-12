"""Generated from Smithy shape ``com.amazonaws.managedblockchain#VoteValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_managedblockchain.errors import DeserializationError

VoteValue: TypeAlias = Literal[
    "YES",
    "NO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "YES",
        "NO",
    )
)


def serialize_json(value: VoteValue) -> str:
    return value


def deserialize_json(data: str) -> VoteValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VoteValue value: {data!r}")
    return cast(VoteValue, data)
