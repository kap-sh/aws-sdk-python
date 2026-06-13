"""Generated from Smithy shape ``com.amazonaws.quicksight#RefreshFailureAlertStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

RefreshFailureAlertStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: RefreshFailureAlertStatus) -> str:
    return value


def deserialize_json(data: str) -> RefreshFailureAlertStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RefreshFailureAlertStatus value: {data!r}")
    return cast(RefreshFailureAlertStatus, data)
