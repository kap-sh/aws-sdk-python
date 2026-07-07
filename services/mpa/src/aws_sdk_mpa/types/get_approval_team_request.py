"""Generated from Smithy shape ``com.amazonaws.mpa#GetApprovalTeamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mpa.types.approval_team_arn


class GetApprovalTeamRequest(TypedDict, closed=True):
    arn: "aws_sdk_mpa.types.approval_team_arn.ApprovalTeamArn"
    """<p>Amazon Resource Name (ARN) for the team.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApprovalTeamRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApprovalTeamRequest:
    out: GetApprovalTeamRequest = {}  # type: ignore[typeddict-item]
    return out
