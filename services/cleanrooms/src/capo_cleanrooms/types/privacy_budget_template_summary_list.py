"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudgetTemplateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.privacy_budget_template_summary

PrivacyBudgetTemplateSummaryList: TypeAlias = list[
    "capo_cleanrooms.types.privacy_budget_template_summary.PrivacyBudgetTemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudgetTemplateSummaryList) -> list:
    import capo_cleanrooms.types.privacy_budget_template_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.privacy_budget_template_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PrivacyBudgetTemplateSummaryList:
    import capo_cleanrooms.types.privacy_budget_template_summary

    out: PrivacyBudgetTemplateSummaryList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.privacy_budget_template_summary.deserialize_json(item)
        )
    return out
