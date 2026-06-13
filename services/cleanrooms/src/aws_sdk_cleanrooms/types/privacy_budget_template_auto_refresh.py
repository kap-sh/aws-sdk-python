"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudgetTemplateAutoRefresh``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

PrivacyBudgetTemplateAutoRefresh: TypeAlias = Literal[
    "CALENDAR_MONTH",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CALENDAR_MONTH",
        "NONE",
    )
)


def serialize_json(value: PrivacyBudgetTemplateAutoRefresh) -> str:
    return value


def deserialize_json(data: str) -> PrivacyBudgetTemplateAutoRefresh:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PrivacyBudgetTemplateAutoRefresh value: {data!r}"
        )
    return cast(PrivacyBudgetTemplateAutoRefresh, data)
