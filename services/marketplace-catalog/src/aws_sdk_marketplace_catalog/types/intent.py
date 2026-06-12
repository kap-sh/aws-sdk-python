"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#Intent``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

Intent: TypeAlias = Literal[
    "VALIDATE",
    "APPLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALIDATE",
        "APPLY",
    )
)


def serialize_json(value: Intent) -> str:
    return value


def deserialize_json(data: str) -> Intent:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Intent value: {data!r}")
    return cast(Intent, data)
