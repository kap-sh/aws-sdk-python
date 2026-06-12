"""Generated from Smithy shape ``com.amazonaws.connect#AccessType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

AccessType: TypeAlias = Literal["ALLOW",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ALLOW",))


def serialize_json(value: AccessType) -> str:
    return value


def deserialize_json(data: str) -> AccessType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessType value: {data!r}")
    return cast(AccessType, data)
