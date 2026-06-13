"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AccessBudgetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

AccessBudgetType: TypeAlias = Literal[
    "CALENDAR_DAY",
    "CALENDAR_MONTH",
    "CALENDAR_WEEK",
    "LIFETIME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CALENDAR_DAY",
        "CALENDAR_MONTH",
        "CALENDAR_WEEK",
        "LIFETIME",
    )
)


def serialize_json(value: AccessBudgetType) -> str:
    return value


def deserialize_json(data: str) -> AccessBudgetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessBudgetType value: {data!r}")
    return cast(AccessBudgetType, data)
