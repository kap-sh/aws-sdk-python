"""Generated from Smithy shape ``com.amazonaws.mpa#GetApprovalTeamResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mpa.types.approval_strategy_response
    import aws_sdk_mpa.types.approval_team_status
    import aws_sdk_mpa.types.approval_team_status_code
    import aws_sdk_mpa.types.description
    import aws_sdk_mpa.types.get_approval_team_response_approvers
    import aws_sdk_mpa.types.iso_timestamp
    import aws_sdk_mpa.types.message
    import aws_sdk_mpa.types.pending_update
    import aws_sdk_mpa.types.policies_references
    import aws_sdk_mpa.types.string


class GetApprovalTeamResponse(TypedDict):
    creation_time: NotRequired["aws_sdk_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the team was created.</p>"""
    approval_strategy: NotRequired[
        "aws_sdk_mpa.types.approval_strategy_response.ApprovalStrategyResponse"
    ]
    """<p>An <code>ApprovalStrategyResponse</code> object. Contains details for how the team grants approval.</p>"""
    number_of_approvers: NotRequired["int"]
    """<p>Total number of approvers in the team.</p>"""
    approvers: NotRequired[
        "aws_sdk_mpa.types.get_approval_team_response_approvers.GetApprovalTeamResponseApprovers"
    ]
    """<p>An array of <code>GetApprovalTeamResponseApprover </code> objects. Contains details for the approvers in the team.</p>"""
    arn: NotRequired["aws_sdk_mpa.types.string.String"]
    """<p>Amazon Resource Name (ARN) for the team.</p>"""
    description: NotRequired["aws_sdk_mpa.types.description.Description"]
    """<p>Description for the team.</p>"""
    name: NotRequired["aws_sdk_mpa.types.string.String"]
    """<p>Name of the approval team.</p>"""
    status: NotRequired["aws_sdk_mpa.types.approval_team_status.ApprovalTeamStatus"]
    r"""<p>Status for the team. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html\">Team health</a> in the <i>Multi-party approval User Guide</i>.</p>"""
    status_code: NotRequired[
        "aws_sdk_mpa.types.approval_team_status_code.ApprovalTeamStatusCode"
    ]
    r"""<p>Status code for the approval team. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html\">Team health</a> in the <i>Multi-party approval User Guide</i>.</p>"""
    status_message: NotRequired["aws_sdk_mpa.types.message.Message"]
    """<p>Message describing the status for the team.</p>"""
    update_session_arn: NotRequired["aws_sdk_mpa.types.string.String"]
    """<p>Amazon Resource Name (ARN) for the session.</p>"""
    version_id: NotRequired["aws_sdk_mpa.types.string.String"]
    """<p>Version ID for the team.</p>"""
    policies: NotRequired["aws_sdk_mpa.types.policies_references.PoliciesReferences"]
    """<p>An array of <code>PolicyReference</code> objects. Contains a list of policies that define the permissions for team resources.</p>"""
    last_update_time: NotRequired["aws_sdk_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the team was last updated.</p>"""
    pending_update: NotRequired["aws_sdk_mpa.types.pending_update.PendingUpdate"]
    """<p>A <code>PendingUpdate</code> object. Contains details for the pending updates for the team, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApprovalTeamResponse) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import aws_sdk_mpa.types.iso_timestamp

        out["CreationTime"] = aws_sdk_mpa.types.iso_timestamp.serialize_json(
            value["creation_time"]
        )
    if "approval_strategy" in value:
        import aws_sdk_mpa.types.approval_strategy_response

        out["ApprovalStrategy"] = (
            aws_sdk_mpa.types.approval_strategy_response.serialize_json(
                value["approval_strategy"]
            )
        )
    if "number_of_approvers" in value:
        out["NumberOfApprovers"] = value["number_of_approvers"]
    if "approvers" in value:
        import aws_sdk_mpa.types.get_approval_team_response_approvers

        out["Approvers"] = (
            aws_sdk_mpa.types.get_approval_team_response_approvers.serialize_json(
                value["approvers"]
            )
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_mpa.types.approval_team_status

        out["Status"] = aws_sdk_mpa.types.approval_team_status.serialize_json(
            value["status"]
        )
    if "status_code" in value:
        import aws_sdk_mpa.types.approval_team_status_code

        out["StatusCode"] = aws_sdk_mpa.types.approval_team_status_code.serialize_json(
            value["status_code"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "update_session_arn" in value:
        out["UpdateSessionArn"] = value["update_session_arn"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "policies" in value:
        import aws_sdk_mpa.types.policies_references

        out["Policies"] = aws_sdk_mpa.types.policies_references.serialize_json(
            value["policies"]
        )
    if "last_update_time" in value:
        import aws_sdk_mpa.types.iso_timestamp

        out["LastUpdateTime"] = aws_sdk_mpa.types.iso_timestamp.serialize_json(
            value["last_update_time"]
        )
    if "pending_update" in value:
        import aws_sdk_mpa.types.pending_update

        out["PendingUpdate"] = aws_sdk_mpa.types.pending_update.serialize_json(
            value["pending_update"]
        )
    return out


def deserialize_json(data: dict) -> GetApprovalTeamResponse:
    out: GetApprovalTeamResponse = {}  # type: ignore[typeddict-item]
    if "CreationTime" in data:
        import aws_sdk_mpa.types.iso_timestamp

        out["creation_time"] = aws_sdk_mpa.types.iso_timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "ApprovalStrategy" in data:
        import aws_sdk_mpa.types.approval_strategy_response

        out["approval_strategy"] = (
            aws_sdk_mpa.types.approval_strategy_response.deserialize_json(
                data["ApprovalStrategy"]
            )
        )
    if "NumberOfApprovers" in data:
        out["number_of_approvers"] = data["NumberOfApprovers"]
    if "Approvers" in data:
        import aws_sdk_mpa.types.get_approval_team_response_approvers

        out["approvers"] = (
            aws_sdk_mpa.types.get_approval_team_response_approvers.deserialize_json(
                data["Approvers"]
            )
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_mpa.types.approval_team_status

        out["status"] = aws_sdk_mpa.types.approval_team_status.deserialize_json(
            data["Status"]
        )
    if "StatusCode" in data:
        import aws_sdk_mpa.types.approval_team_status_code

        out["status_code"] = (
            aws_sdk_mpa.types.approval_team_status_code.deserialize_json(
                data["StatusCode"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "UpdateSessionArn" in data:
        out["update_session_arn"] = data["UpdateSessionArn"]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    if "Policies" in data:
        import aws_sdk_mpa.types.policies_references

        out["policies"] = aws_sdk_mpa.types.policies_references.deserialize_json(
            data["Policies"]
        )
    if "LastUpdateTime" in data:
        import aws_sdk_mpa.types.iso_timestamp

        out["last_update_time"] = aws_sdk_mpa.types.iso_timestamp.deserialize_json(
            data["LastUpdateTime"]
        )
    if "PendingUpdate" in data:
        import aws_sdk_mpa.types.pending_update

        out["pending_update"] = aws_sdk_mpa.types.pending_update.deserialize_json(
            data["PendingUpdate"]
        )
    return out
