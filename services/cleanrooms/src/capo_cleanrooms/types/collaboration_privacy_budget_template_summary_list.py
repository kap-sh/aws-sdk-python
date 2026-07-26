"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationPrivacyBudgetTemplateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_privacy_budget_template_summary

CollaborationPrivacyBudgetTemplateSummaryList: TypeAlias = list[
    "capo_cleanrooms.types.collaboration_privacy_budget_template_summary.CollaborationPrivacyBudgetTemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationPrivacyBudgetTemplateSummaryList) -> list:
    import capo_cleanrooms.types.collaboration_privacy_budget_template_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.collaboration_privacy_budget_template_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CollaborationPrivacyBudgetTemplateSummaryList:
    import capo_cleanrooms.types.collaboration_privacy_budget_template_summary

    out: CollaborationPrivacyBudgetTemplateSummaryList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.collaboration_privacy_budget_template_summary.deserialize_json(
                item
            )
        )
    return out
