"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Include``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

Include: TypeAlias = Literal[
    "ALL",
    "ANY",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "ANY",
        "NONE",
    )
)


def serialize_json(value: Include) -> str:
    return value


def deserialize_json(data: str) -> Include:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Include value: {data!r}")
    return cast(Include, data)
