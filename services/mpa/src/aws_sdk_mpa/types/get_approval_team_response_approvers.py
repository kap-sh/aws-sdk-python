"""Generated from Smithy shape ``com.amazonaws.mpa#GetApprovalTeamResponseApprovers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mpa.types.get_approval_team_response_approver

GetApprovalTeamResponseApprovers: TypeAlias = list[
    "aws_sdk_mpa.types.get_approval_team_response_approver.GetApprovalTeamResponseApprover"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetApprovalTeamResponseApprovers) -> list:
    import aws_sdk_mpa.types.get_approval_team_response_approver

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mpa.types.get_approval_team_response_approver.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GetApprovalTeamResponseApprovers:
    import aws_sdk_mpa.types.get_approval_team_response_approver

    out: GetApprovalTeamResponseApprovers = []
    for item in data:
        out.append(
            aws_sdk_mpa.types.get_approval_team_response_approver.deserialize_json(item)
        )
    return out
