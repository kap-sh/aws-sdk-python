"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ChangeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

ChangeStatus: TypeAlias = Literal[
    "PREPARING",
    "APPLYING",
    "SUCCEEDED",
    "CANCELLED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PREPARING",
        "APPLYING",
        "SUCCEEDED",
        "CANCELLED",
        "FAILED",
    )
)


def serialize_json(value: ChangeStatus) -> str:
    return value


def deserialize_json(data: str) -> ChangeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeStatus value: {data!r}")
    return cast(ChangeStatus, data)
