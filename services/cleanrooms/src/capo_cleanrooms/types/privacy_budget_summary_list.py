"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudgetSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.privacy_budget_summary

PrivacyBudgetSummaryList: TypeAlias = list[
    "capo_cleanrooms.types.privacy_budget_summary.PrivacyBudgetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudgetSummaryList) -> list:
    import capo_cleanrooms.types.privacy_budget_summary

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.privacy_budget_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PrivacyBudgetSummaryList:
    import capo_cleanrooms.types.privacy_budget_summary

    out: PrivacyBudgetSummaryList = []
    for item in data:
        out.append(capo_cleanrooms.types.privacy_budget_summary.deserialize_json(item))
    return out
