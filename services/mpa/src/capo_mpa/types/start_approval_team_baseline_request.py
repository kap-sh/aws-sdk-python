"""Generated from Smithy shape ``com.amazonaws.mpa#StartApprovalTeamBaselineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.approval_team_arn
    import capo_mpa.types.start_approval_team_baseline_approver_ids


class StartApprovalTeamBaselineRequest(TypedDict, closed=True):
    arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn"
    """<p>Amazon Resource Name (ARN) for the approval team.</p>"""
    approver_ids: NotRequired[
        "capo_mpa.types.start_approval_team_baseline_approver_ids.StartApprovalTeamBaselineApproverIds"
    ]
    """<p>Array of approver IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartApprovalTeamBaselineRequest) -> dict:
    out: dict = {}
    if "approver_ids" in value:
        import capo_mpa.types.start_approval_team_baseline_approver_ids

        out["ApproverIds"] = (
            capo_mpa.types.start_approval_team_baseline_approver_ids.serialize_json(
                value["approver_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartApprovalTeamBaselineRequest:
    out: StartApprovalTeamBaselineRequest = {}  # type: ignore[typeddict-item]
    if "ApproverIds" in data:
        import capo_mpa.types.start_approval_team_baseline_approver_ids

        out["approver_ids"] = (
            capo_mpa.types.start_approval_team_baseline_approver_ids.deserialize_json(
                data["ApproverIds"]
            )
        )
    return out
