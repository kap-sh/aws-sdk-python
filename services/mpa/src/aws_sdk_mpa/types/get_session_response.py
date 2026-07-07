"""Generated from Smithy shape ``com.amazonaws.mpa#GetSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mpa.types.account_id
    import aws_sdk_mpa.types.action_completion_strategy
    import aws_sdk_mpa.types.action_name
    import aws_sdk_mpa.types.additional_security_requirements
    import aws_sdk_mpa.types.approval_strategy_response
    import aws_sdk_mpa.types.approval_team_arn
    import aws_sdk_mpa.types.approval_team_name
    import aws_sdk_mpa.types.description
    import aws_sdk_mpa.types.get_session_response_approver_responses
    import aws_sdk_mpa.types.iso_timestamp
    import aws_sdk_mpa.types.message
    import aws_sdk_mpa.types.region
    import aws_sdk_mpa.types.requester_comment
    import aws_sdk_mpa.types.service_principal
    import aws_sdk_mpa.types.session_arn
    import aws_sdk_mpa.types.session_execution_status
    import aws_sdk_mpa.types.session_metadata
    import aws_sdk_mpa.types.session_status
    import aws_sdk_mpa.types.session_status_code
    import aws_sdk_mpa.types.string


class GetSessionResponse(TypedDict, closed=True):
    session_arn: NotRequired["aws_sdk_mpa.types.session_arn.SessionArn"]
    """<p>Amazon Resource Name (ARN) for the session.</p>"""
    approval_team_arn: NotRequired[
        "aws_sdk_mpa.types.approval_team_arn.ApprovalTeamArn"
    ]
    """<p>Amazon Resource Name (ARN) for the approval team.</p>"""
    approval_team_name: NotRequired[
        "aws_sdk_mpa.types.approval_team_name.ApprovalTeamName"
    ]
    """<p>Name of the approval team.</p>"""
    protected_resource_arn: NotRequired["aws_sdk_mpa.types.string.String"]
    """<p>Amazon Resource Name (ARN) for the protected operation.</p>"""
    approval_strategy: NotRequired[
        "aws_sdk_mpa.types.approval_strategy_response.ApprovalStrategyResponse"
    ]
    """<p>An <code>ApprovalStrategyResponse</code> object. Contains details for how the team grants approval</p>"""
    number_of_approvers: NotRequired["int"]
    """<p>Total number of approvers in the session.</p>"""
    initiation_time: NotRequired["aws_sdk_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the session was initiated.</p>"""
    expiration_time: NotRequired["aws_sdk_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the session will expire.</p>"""
    completion_time: NotRequired["aws_sdk_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the session completed.</p>"""
    description: NotRequired["aws_sdk_mpa.types.description.Description"]
    """<p>Description for the session.</p>"""
    metadata: NotRequired["aws_sdk_mpa.types.session_metadata.SessionMetadata"]
    """<p>Metadata for the session.</p>"""
    status: NotRequired["aws_sdk_mpa.types.session_status.SessionStatus"]
    """<p>Status for the session. For example, if the team has approved the requested operation.</p>"""
    status_code: NotRequired["aws_sdk_mpa.types.session_status_code.SessionStatusCode"]
    """<p>Status code of the session.</p>"""
    status_message: NotRequired["aws_sdk_mpa.types.message.Message"]
    """<p>Message describing the status for session.</p>"""
    execution_status: NotRequired[
        "aws_sdk_mpa.types.session_execution_status.SessionExecutionStatus"
    ]
    """<p>Status for the protected operation. For example, if the operation is <code>PENDING</code>.</p>"""
    action_name: NotRequired["aws_sdk_mpa.types.action_name.ActionName"]
    """<p>Name of the protected operation.</p>"""
    requester_service_principal: NotRequired[
        "aws_sdk_mpa.types.service_principal.ServicePrincipal"
    ]
    r"""<p> <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services\">Service principal</a> for the service associated with the protected operation.</p>"""
    requester_principal_arn: NotRequired["aws_sdk_mpa.types.string.String"]
    r"""<p> <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-request\">IAM principal</a> that made the operation request.</p>"""
    requester_account_id: NotRequired["aws_sdk_mpa.types.account_id.AccountId"]
    """<p>ID for the account that made the operation request.</p>"""
    requester_region: NotRequired["aws_sdk_mpa.types.region.Region"]
    """<p>Amazon Web Services Region where the operation request originated.</p>"""
    requester_comment: NotRequired[
        "aws_sdk_mpa.types.requester_comment.RequesterComment"
    ]
    """<p>Message from the account that made the operation request</p>"""
    action_completion_strategy: NotRequired[
        "aws_sdk_mpa.types.action_completion_strategy.ActionCompletionStrategy"
    ]
    """<p>Strategy for executing the protected operation. <code>AUTO_COMPLETION_UPON_APPROVAL</code> means the operation is automatically executed using the requester's permissions, if approved.</p>"""
    approver_responses: NotRequired[
        "aws_sdk_mpa.types.get_session_response_approver_responses.GetSessionResponseApproverResponses"
    ]
    """<p>An array of <code>GetSessionResponseApproverResponse</code> objects. Contains details for approver responses in the session.</p>"""
    additional_security_requirements: NotRequired[
        "aws_sdk_mpa.types.additional_security_requirements.AdditionalSecurityRequirements"
    ]
    """<p>A list of <code>AdditionalSecurityRequirement</code> applied to the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionResponse) -> dict:
    out: dict = {}
    if "session_arn" in value:
        out["SessionArn"] = value["session_arn"]
    if "approval_team_arn" in value:
        out["ApprovalTeamArn"] = value["approval_team_arn"]
    if "approval_team_name" in value:
        out["ApprovalTeamName"] = value["approval_team_name"]
    if "protected_resource_arn" in value:
        out["ProtectedResourceArn"] = value["protected_resource_arn"]
    if "approval_strategy" in value:
        import aws_sdk_mpa.types.approval_strategy_response

        out["ApprovalStrategy"] = (
            aws_sdk_mpa.types.approval_strategy_response.serialize_json(
                value["approval_strategy"]
            )
        )
    if "number_of_approvers" in value:
        out["NumberOfApprovers"] = value["number_of_approvers"]
    if "initiation_time" in value:
        import aws_sdk_mpa.types.iso_timestamp

        out["InitiationTime"] = aws_sdk_mpa.types.iso_timestamp.serialize_json(
            value["initiation_time"]
        )
    if "expiration_time" in value:
        import aws_sdk_mpa.types.iso_timestamp

        out["ExpirationTime"] = aws_sdk_mpa.types.iso_timestamp.serialize_json(
            value["expiration_time"]
        )
    if "completion_time" in value:
        import aws_sdk_mpa.types.iso_timestamp

        out["CompletionTime"] = aws_sdk_mpa.types.iso_timestamp.serialize_json(
            value["completion_time"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "metadata" in value:
        import aws_sdk_mpa.types.session_metadata

        out["Metadata"] = aws_sdk_mpa.types.session_metadata.serialize_json(
            value["metadata"]
        )
    if "status" in value:
        import aws_sdk_mpa.types.session_status

        out["Status"] = aws_sdk_mpa.types.session_status.serialize_json(value["status"])
    if "status_code" in value:
        import aws_sdk_mpa.types.session_status_code

        out["StatusCode"] = aws_sdk_mpa.types.session_status_code.serialize_json(
            value["status_code"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "execution_status" in value:
        import aws_sdk_mpa.types.session_execution_status

        out["ExecutionStatus"] = (
            aws_sdk_mpa.types.session_execution_status.serialize_json(
                value["execution_status"]
            )
        )
    if "action_name" in value:
        out["ActionName"] = value["action_name"]
    if "requester_service_principal" in value:
        out["RequesterServicePrincipal"] = value["requester_service_principal"]
    if "requester_principal_arn" in value:
        out["RequesterPrincipalArn"] = value["requester_principal_arn"]
    if "requester_account_id" in value:
        out["RequesterAccountId"] = value["requester_account_id"]
    if "requester_region" in value:
        out["RequesterRegion"] = value["requester_region"]
    if "requester_comment" in value:
        out["RequesterComment"] = value["requester_comment"]
    if "action_completion_strategy" in value:
        import aws_sdk_mpa.types.action_completion_strategy

        out["ActionCompletionStrategy"] = (
            aws_sdk_mpa.types.action_completion_strategy.serialize_json(
                value["action_completion_strategy"]
            )
        )
    if "approver_responses" in value:
        import aws_sdk_mpa.types.get_session_response_approver_responses

        out["ApproverResponses"] = (
            aws_sdk_mpa.types.get_session_response_approver_responses.serialize_json(
                value["approver_responses"]
            )
        )
    if "additional_security_requirements" in value:
        import aws_sdk_mpa.types.additional_security_requirements

        out["AdditionalSecurityRequirements"] = (
            aws_sdk_mpa.types.additional_security_requirements.serialize_json(
                value["additional_security_requirements"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSessionResponse:
    out: GetSessionResponse = {}  # type: ignore[typeddict-item]
    if "SessionArn" in data:
        out["session_arn"] = data["SessionArn"]
    if "ApprovalTeamArn" in data:
        out["approval_team_arn"] = data["ApprovalTeamArn"]
    if "ApprovalTeamName" in data:
        out["approval_team_name"] = data["ApprovalTeamName"]
    if "ProtectedResourceArn" in data:
        out["protected_resource_arn"] = data["ProtectedResourceArn"]
    if "ApprovalStrategy" in data:
        import aws_sdk_mpa.types.approval_strategy_response

        out["approval_strategy"] = (
            aws_sdk_mpa.types.approval_strategy_response.deserialize_json(
                data["ApprovalStrategy"]
            )
        )
    if "NumberOfApprovers" in data:
        out["number_of_approvers"] = data["NumberOfApprovers"]
    if "InitiationTime" in data:
        import aws_sdk_mpa.types.iso_timestamp

        out["initiation_time"] = aws_sdk_mpa.types.iso_timestamp.deserialize_json(
            data["InitiationTime"]
        )
    if "ExpirationTime" in data:
        import aws_sdk_mpa.types.iso_timestamp

        out["expiration_time"] = aws_sdk_mpa.types.iso_timestamp.deserialize_json(
            data["ExpirationTime"]
        )
    if "CompletionTime" in data:
        import aws_sdk_mpa.types.iso_timestamp

        out["completion_time"] = aws_sdk_mpa.types.iso_timestamp.deserialize_json(
            data["CompletionTime"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Metadata" in data:
        import aws_sdk_mpa.types.session_metadata

        out["metadata"] = aws_sdk_mpa.types.session_metadata.deserialize_json(
            data["Metadata"]
        )
    if "Status" in data:
        import aws_sdk_mpa.types.session_status

        out["status"] = aws_sdk_mpa.types.session_status.deserialize_json(
            data["Status"]
        )
    if "StatusCode" in data:
        import aws_sdk_mpa.types.session_status_code

        out["status_code"] = aws_sdk_mpa.types.session_status_code.deserialize_json(
            data["StatusCode"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "ExecutionStatus" in data:
        import aws_sdk_mpa.types.session_execution_status

        out["execution_status"] = (
            aws_sdk_mpa.types.session_execution_status.deserialize_json(
                data["ExecutionStatus"]
            )
        )
    if "ActionName" in data:
        out["action_name"] = data["ActionName"]
    if "RequesterServicePrincipal" in data:
        out["requester_service_principal"] = data["RequesterServicePrincipal"]
    if "RequesterPrincipalArn" in data:
        out["requester_principal_arn"] = data["RequesterPrincipalArn"]
    if "RequesterAccountId" in data:
        out["requester_account_id"] = data["RequesterAccountId"]
    if "RequesterRegion" in data:
        out["requester_region"] = data["RequesterRegion"]
    if "RequesterComment" in data:
        out["requester_comment"] = data["RequesterComment"]
    if "ActionCompletionStrategy" in data:
        import aws_sdk_mpa.types.action_completion_strategy

        out["action_completion_strategy"] = (
            aws_sdk_mpa.types.action_completion_strategy.deserialize_json(
                data["ActionCompletionStrategy"]
            )
        )
    if "ApproverResponses" in data:
        import aws_sdk_mpa.types.get_session_response_approver_responses

        out["approver_responses"] = (
            aws_sdk_mpa.types.get_session_response_approver_responses.deserialize_json(
                data["ApproverResponses"]
            )
        )
    if "AdditionalSecurityRequirements" in data:
        import aws_sdk_mpa.types.additional_security_requirements

        out["additional_security_requirements"] = (
            aws_sdk_mpa.types.additional_security_requirements.deserialize_json(
                data["AdditionalSecurityRequirements"]
            )
        )
    return out
