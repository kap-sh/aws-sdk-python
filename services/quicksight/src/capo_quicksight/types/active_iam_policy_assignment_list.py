"""Generated from Smithy shape ``com.amazonaws.quicksight#ActiveIAMPolicyAssignmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.active_iam_policy_assignment

ActiveIAMPolicyAssignmentList: TypeAlias = list[
    "capo_quicksight.types.active_iam_policy_assignment.ActiveIAMPolicyAssignment"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActiveIAMPolicyAssignmentList) -> list:
    import capo_quicksight.types.active_iam_policy_assignment

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.active_iam_policy_assignment.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ActiveIAMPolicyAssignmentList:
    import capo_quicksight.types.active_iam_policy_assignment

    out: ActiveIAMPolicyAssignmentList = []
    for item in data:
        out.append(
            capo_quicksight.types.active_iam_policy_assignment.deserialize_json(item)
        )
    return out
