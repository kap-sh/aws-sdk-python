"""Generated from Smithy shape ``com.amazonaws.outposts#LineItemStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

LineItemStatus: TypeAlias = Literal[
    "PREPARING",
    "BUILDING",
    "SHIPPED",
    "DELIVERED",
    "INSTALLING",
    "INSTALLED",
    "ERROR",
    "CANCELLED",
    "REPLACED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PREPARING",
        "BUILDING",
        "SHIPPED",
        "DELIVERED",
        "INSTALLING",
        "INSTALLED",
        "ERROR",
        "CANCELLED",
        "REPLACED",
    )
)


def serialize_json(value: LineItemStatus) -> str:
    return value


def deserialize_json(data: str) -> LineItemStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LineItemStatus value: {data!r}")
    return cast(LineItemStatus, data)
