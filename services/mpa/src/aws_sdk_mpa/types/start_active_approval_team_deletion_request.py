"""Generated from Smithy shape ``com.amazonaws.mpa#StartActiveApprovalTeamDeletionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mpa.types.approval_team_arn


class StartActiveApprovalTeamDeletionRequest(TypedDict, closed=True):
    pending_window_days: NotRequired["int"]
    """<p>Number of days between when the team approves the delete request and when the team is deleted.</p>"""
    arn: "aws_sdk_mpa.types.approval_team_arn.ApprovalTeamArn"
    """<p>Amazon Resource Name (ARN) for the team.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartActiveApprovalTeamDeletionRequest) -> dict:
    out: dict = {}
    if "pending_window_days" in value:
        out["PendingWindowDays"] = value["pending_window_days"]
    return out


def deserialize_json(data: dict) -> StartActiveApprovalTeamDeletionRequest:
    out: StartActiveApprovalTeamDeletionRequest = {}  # type: ignore[typeddict-item]
    if "PendingWindowDays" in data:
        out["pending_window_days"] = data["PendingWindowDays"]
    return out
