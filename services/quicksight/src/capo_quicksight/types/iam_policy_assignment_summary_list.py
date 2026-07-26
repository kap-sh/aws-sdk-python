"""Generated from Smithy shape ``com.amazonaws.quicksight#IAMPolicyAssignmentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.iam_policy_assignment_summary

IAMPolicyAssignmentSummaryList: TypeAlias = list[
    "capo_quicksight.types.iam_policy_assignment_summary.IAMPolicyAssignmentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IAMPolicyAssignmentSummaryList) -> list:
    import capo_quicksight.types.iam_policy_assignment_summary

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.iam_policy_assignment_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IAMPolicyAssignmentSummaryList:
    import capo_quicksight.types.iam_policy_assignment_summary

    out: IAMPolicyAssignmentSummaryList = []
    for item in data:
        out.append(
            capo_quicksight.types.iam_policy_assignment_summary.deserialize_json(item)
        )
    return out
