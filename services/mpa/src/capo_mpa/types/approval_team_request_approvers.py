"""Generated from Smithy shape ``com.amazonaws.mpa#ApprovalTeamRequestApprovers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mpa.types.approval_team_request_approver

ApprovalTeamRequestApprovers: TypeAlias = list[
    "capo_mpa.types.approval_team_request_approver.ApprovalTeamRequestApprover"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalTeamRequestApprovers) -> list:
    import capo_mpa.types.approval_team_request_approver

    out: list = []
    for item in value:
        out.append(capo_mpa.types.approval_team_request_approver.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApprovalTeamRequestApprovers:
    import capo_mpa.types.approval_team_request_approver

    out: ApprovalTeamRequestApprovers = []
    for item in data:
        out.append(capo_mpa.types.approval_team_request_approver.deserialize_json(item))
    return out
