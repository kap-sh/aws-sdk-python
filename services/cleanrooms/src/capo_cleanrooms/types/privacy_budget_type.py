"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudgetType``."""

from typing import Literal, TypeAlias, cast

PrivacyBudgetType: TypeAlias = Literal[
    "DIFFERENTIAL_PRIVACY",
    "ACCESS_BUDGET",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudgetType) -> str:
    return value


def deserialize_json(data: str) -> PrivacyBudgetType:
    return cast(PrivacyBudgetType, data)
