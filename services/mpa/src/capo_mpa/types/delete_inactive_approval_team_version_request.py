"""Generated from Smithy shape ``com.amazonaws.mpa#DeleteInactiveApprovalTeamVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.approval_team_arn
    import capo_mpa.types.string


class DeleteInactiveApprovalTeamVersionRequest(TypedDict, closed=True):
    arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn"
    """<p>Amaazon Resource Name (ARN) for the team.</p>"""
    version_id: "capo_mpa.types.string.String"
    """<p>Version ID for the team.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInactiveApprovalTeamVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInactiveApprovalTeamVersionRequest:
    out: DeleteInactiveApprovalTeamVersionRequest = {}  # type: ignore[typeddict-item]
    return out
