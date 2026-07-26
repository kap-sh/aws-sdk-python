"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudgetTemplateAutoRefresh``."""

from typing import Literal, TypeAlias, cast

PrivacyBudgetTemplateAutoRefresh: TypeAlias = Literal[
    "CALENDAR_MONTH",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudgetTemplateAutoRefresh) -> str:
    return value


def deserialize_json(data: str) -> PrivacyBudgetTemplateAutoRefresh:
    return cast(PrivacyBudgetTemplateAutoRefresh, data)
