"""Generated from Smithy shape ``com.amazonaws.quicksight#IdentityStore``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

IdentityStore: TypeAlias = Literal["QUICKSIGHT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("QUICKSIGHT",))


def serialize_json(value: IdentityStore) -> str:
    return value


def deserialize_json(data: str) -> IdentityStore:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdentityStore value: {data!r}")
    return cast(IdentityStore, data)
