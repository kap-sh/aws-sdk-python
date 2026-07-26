"""Generated from Smithy shape ``com.amazonaws.mpa#UpdateApprovalTeamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.approval_strategy
    import capo_mpa.types.approval_team_arn
    import capo_mpa.types.approval_team_request_approvers
    import capo_mpa.types.description
    import capo_mpa.types.update_actions


class UpdateApprovalTeamRequest(TypedDict, closed=True):
    approval_strategy: NotRequired["capo_mpa.types.approval_strategy.ApprovalStrategy"]
    """<p>An <code>ApprovalStrategy</code> object. Contains details for how the team grants approval.</p>"""
    approvers: NotRequired[
        "capo_mpa.types.approval_team_request_approvers.ApprovalTeamRequestApprovers"
    ]
    """<p>An array of <code>ApprovalTeamRequestApprover</code> objects. Contains details for the approvers in the team.</p>"""
    description: NotRequired["capo_mpa.types.description.Description"]
    """<p>Description for the team.</p>"""
    arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn"
    """<p>Amazon Resource Name (ARN) for the team.</p>"""
    update_actions: NotRequired["capo_mpa.types.update_actions.UpdateActions"]
    """<p>A list of <code>UpdateAction</code> to perform when updating the team.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApprovalTeamRequest) -> dict:
    out: dict = {}
    if "approval_strategy" in value:
        import capo_mpa.types.approval_strategy

        out["ApprovalStrategy"] = capo_mpa.types.approval_strategy.serialize_json(
            value["approval_strategy"]
        )
    if "approvers" in value:
        import capo_mpa.types.approval_team_request_approvers

        out["Approvers"] = (
            capo_mpa.types.approval_team_request_approvers.serialize_json(
                value["approvers"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "update_actions" in value:
        import capo_mpa.types.update_actions

        out["UpdateActions"] = capo_mpa.types.update_actions.serialize_json(
            value["update_actions"]
        )
    return out


def deserialize_json(data: dict) -> UpdateApprovalTeamRequest:
    out: UpdateApprovalTeamRequest = {}  # type: ignore[typeddict-item]
    if "ApprovalStrategy" in data:
        import capo_mpa.types.approval_strategy

        out["approval_strategy"] = capo_mpa.types.approval_strategy.deserialize_json(
            data["ApprovalStrategy"]
        )
    if "Approvers" in data:
        import capo_mpa.types.approval_team_request_approvers

        out["approvers"] = (
            capo_mpa.types.approval_team_request_approvers.deserialize_json(
                data["Approvers"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "UpdateActions" in data:
        import capo_mpa.types.update_actions

        out["update_actions"] = capo_mpa.types.update_actions.deserialize_json(
            data["UpdateActions"]
        )
    return out
