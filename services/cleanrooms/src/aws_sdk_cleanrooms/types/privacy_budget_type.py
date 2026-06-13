"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudgetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

PrivacyBudgetType: TypeAlias = Literal[
    "DIFFERENTIAL_PRIVACY",
    "ACCESS_BUDGET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIFFERENTIAL_PRIVACY",
        "ACCESS_BUDGET",
    )
)


def serialize_json(value: PrivacyBudgetType) -> str:
    return value


def deserialize_json(data: str) -> PrivacyBudgetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrivacyBudgetType value: {data!r}")
    return cast(PrivacyBudgetType, data)
