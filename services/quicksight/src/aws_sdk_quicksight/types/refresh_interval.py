"""Generated from Smithy shape ``com.amazonaws.quicksight#RefreshInterval``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

RefreshInterval: TypeAlias = Literal[
    "MINUTE15",
    "MINUTE30",
    "HOURLY",
    "DAILY",
    "WEEKLY",
    "MONTHLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MINUTE15",
        "MINUTE30",
        "HOURLY",
        "DAILY",
        "WEEKLY",
        "MONTHLY",
    )
)


def serialize_json(value: RefreshInterval) -> str:
    return value


def deserialize_json(data: str) -> RefreshInterval:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RefreshInterval value: {data!r}")
    return cast(RefreshInterval, data)
