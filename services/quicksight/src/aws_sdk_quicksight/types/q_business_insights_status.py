"""Generated from Smithy shape ``com.amazonaws.quicksight#QBusinessInsightsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

QBusinessInsightsStatus: TypeAlias = Literal[
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


def serialize_json(value: QBusinessInsightsStatus) -> str:
    return value


def deserialize_json(data: str) -> QBusinessInsightsStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QBusinessInsightsStatus value: {data!r}")
    return cast(QBusinessInsightsStatus, data)
