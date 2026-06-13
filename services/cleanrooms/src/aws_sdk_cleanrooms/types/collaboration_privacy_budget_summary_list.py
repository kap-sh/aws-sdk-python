"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationPrivacyBudgetSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_privacy_budget_summary

CollaborationPrivacyBudgetSummaryList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.collaboration_privacy_budget_summary.CollaborationPrivacyBudgetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationPrivacyBudgetSummaryList) -> list:
    import aws_sdk_cleanrooms.types.collaboration_privacy_budget_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.collaboration_privacy_budget_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CollaborationPrivacyBudgetSummaryList:
    import aws_sdk_cleanrooms.types.collaboration_privacy_budget_summary

    out: CollaborationPrivacyBudgetSummaryList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.collaboration_privacy_budget_summary.deserialize_json(
                item
            )
        )
    return out
