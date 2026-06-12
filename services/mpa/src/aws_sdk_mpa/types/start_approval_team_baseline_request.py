"""Generated from Smithy shape ``com.amazonaws.mpa#StartApprovalTeamBaselineRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mpa.types.approval_team_arn
    import aws_sdk_mpa.types.start_approval_team_baseline_approver_ids


class StartApprovalTeamBaselineRequest(TypedDict):
    arn: "aws_sdk_mpa.types.approval_team_arn.ApprovalTeamArn"
    """<p>Amazon Resource Name (ARN) for the approval team.</p>"""
    approver_ids: NotRequired[
        "aws_sdk_mpa.types.start_approval_team_baseline_approver_ids.StartApprovalTeamBaselineApproverIds"
    ]
    """<p>Array of approver IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartApprovalTeamBaselineRequest) -> dict:
    out: dict = {}
    if "approver_ids" in value:
        import aws_sdk_mpa.types.start_approval_team_baseline_approver_ids

        out["ApproverIds"] = (
            aws_sdk_mpa.types.start_approval_team_baseline_approver_ids.serialize_json(
                value["approver_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartApprovalTeamBaselineRequest:
    out: StartApprovalTeamBaselineRequest = {}  # type: ignore[typeddict-item]
    if "ApproverIds" in data:
        import aws_sdk_mpa.types.start_approval_team_baseline_approver_ids

        out["approver_ids"] = (
            aws_sdk_mpa.types.start_approval_team_baseline_approver_ids.deserialize_json(
                data["ApproverIds"]
            )
        )
    return out
