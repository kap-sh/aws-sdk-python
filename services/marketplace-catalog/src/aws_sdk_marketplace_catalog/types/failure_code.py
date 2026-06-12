"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#FailureCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

FailureCode: TypeAlias = Literal[
    "CLIENT_ERROR",
    "SERVER_FAULT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLIENT_ERROR",
        "SERVER_FAULT",
    )
)


def serialize_json(value: FailureCode) -> str:
    return value


def deserialize_json(data: str) -> FailureCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FailureCode value: {data!r}")
    return cast(FailureCode, data)
