"""Generated from Smithy shape ``com.amazonaws.mpa#PendingUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.approval_strategy_response
    import capo_mpa.types.approval_team_status
    import capo_mpa.types.approval_team_status_code
    import capo_mpa.types.get_approval_team_response_approvers
    import capo_mpa.types.iso_timestamp
    import capo_mpa.types.message
    import capo_mpa.types.string


class PendingUpdate(TypedDict, closed=True):
    version_id: NotRequired["capo_mpa.types.string.String"]
    """<p>Version ID for the team.</p>"""
    description: NotRequired["capo_mpa.types.string.String"]
    """<p>Description for the team.</p>"""
    approval_strategy: NotRequired[
        "capo_mpa.types.approval_strategy_response.ApprovalStrategyResponse"
    ]
    """<p>An <code>ApprovalStrategyResponse</code> object. Contains details for how the team grants approval.</p>"""
    number_of_approvers: NotRequired["int"]
    """<p>Total number of approvers in the team.</p>"""
    status: NotRequired["capo_mpa.types.approval_team_status.ApprovalTeamStatus"]
    r"""<p>Status for the team. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html\">Team health</a> in the <i>Multi-party approval User Guide</i>.</p>"""
    status_code: NotRequired[
        "capo_mpa.types.approval_team_status_code.ApprovalTeamStatusCode"
    ]
    r"""<p>Status code for the update. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html\">Team health</a> in the <i>Multi-party approval User Guide</i>.</p>"""
    status_message: NotRequired["capo_mpa.types.message.Message"]
    """<p>Message describing the status for the team.</p>"""
    approvers: NotRequired[
        "capo_mpa.types.get_approval_team_response_approvers.GetApprovalTeamResponseApprovers"
    ]
    """<p>An array of <code>GetApprovalTeamResponseApprover </code> objects. Contains details for the approvers in the team.</p>"""
    update_initiation_time: NotRequired["capo_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the update request was initiated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PendingUpdate) -> dict:
    out: dict = {}
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "approval_strategy" in value:
        import capo_mpa.types.approval_strategy_response

        out["ApprovalStrategy"] = (
            capo_mpa.types.approval_strategy_response.serialize_json(
                value["approval_strategy"]
            )
        )
    if "number_of_approvers" in value:
        out["NumberOfApprovers"] = value["number_of_approvers"]
    if "status" in value:
        import capo_mpa.types.approval_team_status

        out["Status"] = capo_mpa.types.approval_team_status.serialize_json(
            value["status"]
        )
    if "status_code" in value:
        import capo_mpa.types.approval_team_status_code

        out["StatusCode"] = capo_mpa.types.approval_team_status_code.serialize_json(
            value["status_code"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "approvers" in value:
        import capo_mpa.types.get_approval_team_response_approvers

        out["Approvers"] = (
            capo_mpa.types.get_approval_team_response_approvers.serialize_json(
                value["approvers"]
            )
        )
    if "update_initiation_time" in value:
        import capo_mpa.types.iso_timestamp

        out["UpdateInitiationTime"] = capo_mpa.types.iso_timestamp.serialize_json(
            value["update_initiation_time"]
        )
    return out


def deserialize_json(data: dict) -> PendingUpdate:
    out: PendingUpdate = {}  # type: ignore[typeddict-item]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ApprovalStrategy" in data:
        import capo_mpa.types.approval_strategy_response

        out["approval_strategy"] = (
            capo_mpa.types.approval_strategy_response.deserialize_json(
                data["ApprovalStrategy"]
            )
        )
    if "NumberOfApprovers" in data:
        out["number_of_approvers"] = data["NumberOfApprovers"]
    if "Status" in data:
        import capo_mpa.types.approval_team_status

        out["status"] = capo_mpa.types.approval_team_status.deserialize_json(
            data["Status"]
        )
    if "StatusCode" in data:
        import capo_mpa.types.approval_team_status_code

        out["status_code"] = capo_mpa.types.approval_team_status_code.deserialize_json(
            data["StatusCode"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "Approvers" in data:
        import capo_mpa.types.get_approval_team_response_approvers

        out["approvers"] = (
            capo_mpa.types.get_approval_team_response_approvers.deserialize_json(
                data["Approvers"]
            )
        )
    if "UpdateInitiationTime" in data:
        import capo_mpa.types.iso_timestamp

        out["update_initiation_time"] = capo_mpa.types.iso_timestamp.deserialize_json(
            data["UpdateInitiationTime"]
        )
    return out
