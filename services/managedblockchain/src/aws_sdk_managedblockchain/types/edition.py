"""Generated from Smithy shape ``com.amazonaws.managedblockchain#Edition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_managedblockchain.errors import DeserializationError

Edition: TypeAlias = Literal[
    "STARTER",
    "STANDARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTER",
        "STANDARD",
    )
)


def serialize_json(value: Edition) -> str:
    return value


def deserialize_json(data: str) -> Edition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Edition value: {data!r}")
    return cast(Edition, data)
