"""Generated from Smithy shape ``com.amazonaws.managedblockchain#AccessorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_managedblockchain.errors import DeserializationError

AccessorType: TypeAlias = Literal["BILLING_TOKEN",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BILLING_TOKEN",))


def serialize_json(value: AccessorType) -> str:
    return value


def deserialize_json(data: str) -> AccessorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessorType value: {data!r}")
    return cast(AccessorType, data)
