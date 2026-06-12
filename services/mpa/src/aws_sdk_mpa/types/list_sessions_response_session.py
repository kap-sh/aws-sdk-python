"""Generated from Smithy shape ``com.amazonaws.mpa#ListSessionsResponseSession``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mpa.types.account_id
    import aws_sdk_mpa.types.action_completion_strategy
    import aws_sdk_mpa.types.action_name
    import aws_sdk_mpa.types.additional_security_requirements
    import aws_sdk_mpa.types.approval_team_arn
    import aws_sdk_mpa.types.approval_team_name
    import aws_sdk_mpa.types.description
    import aws_sdk_mpa.types.iso_timestamp
    import aws_sdk_mpa.types.message
    import aws_sdk_mpa.types.region
    import aws_sdk_mpa.types.service_principal
    import aws_sdk_mpa.types.session_arn
    import aws_sdk_mpa.types.session_status
    import aws_sdk_mpa.types.session_status_code
    import aws_sdk_mpa.types.string


class ListSessionsResponseSession(TypedDict):
    session_arn: NotRequired["aws_sdk_mpa.types.session_arn.SessionArn"]
    """<p>Amazon Resource Name (ARN) for the session.</p>"""
    approval_team_name: NotRequired[
        "aws_sdk_mpa.types.approval_team_name.ApprovalTeamName"
    ]
    """<p>Name of the approval team.</p>"""
    approval_team_arn: NotRequired[
        "aws_sdk_mpa.types.approval_team_arn.ApprovalTeamArn"
    ]
    """<p>Amazon Resource Name (ARN) for the approval team.</p>"""
    initiation_time: NotRequired["aws_sdk_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the session was initiated.</p>"""
    expiration_time: NotRequired["aws_sdk_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the session was expire.</p>"""
    completion_time: NotRequired["aws_sdk_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the session was completed.</p>"""
    description: NotRequired["aws_sdk_mpa.types.description.Description"]
    """<p>Description for the team.</p>"""
    action_name: NotRequired["aws_sdk_mpa.types.action_name.ActionName"]
    """<p>Name of the protected operation.</p>"""
    protected_resource_arn: NotRequired["aws_sdk_mpa.types.string.String"]
    """<p>Amazon Resource Name (ARN) for the protected operation.</p>"""
    requester_service_principal: NotRequired[
        "aws_sdk_mpa.types.service_principal.ServicePrincipal"
    ]
    """<p> <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services\">Service principal</a> for the service associated with the protected operation.</p>"""
    requester_principal_arn: NotRequired["aws_sdk_mpa.types.string.String"]
    """<p> <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-request\">IAM principal</a> that made the operation request.</p>"""
    requester_region: NotRequired["aws_sdk_mpa.types.region.Region"]
    """<p>Amazon Web Services Region where the operation request originated.</p>"""
    requester_account_id: NotRequired["aws_sdk_mpa.types.account_id.AccountId"]
    """<p>ID for the account that made the operation request.</p>"""
    status: NotRequired["aws_sdk_mpa.types.session_status.SessionStatus"]
    """<p>Status for the protected operation. For example, if the operation is <code>PENDING</code>.</p>"""
    status_code: NotRequired["aws_sdk_mpa.types.session_status_code.SessionStatusCode"]
    """<p>Status code of the session.</p>"""
    status_message: NotRequired["aws_sdk_mpa.types.message.Message"]
    """<p>Message describing the status for session.</p>"""
    action_completion_strategy: NotRequired[
        "aws_sdk_mpa.types.action_completion_strategy.ActionCompletionStrategy"
    ]
    """<p>Strategy for executing the protected operation. <code>AUTO_COMPLETION_UPON_APPROVAL</code> means the operation is executed automatically using the requester's permissions, if approved.</p>"""
    additional_security_requirements: NotRequired[
        "aws_sdk_mpa.types.additional_security_requirements.AdditionalSecurityRequirements"
    ]
    """<p>A list of <code>AdditionalSecurityRequirement</code> applied to the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsResponseSession) -> dict:
    out: dict = {}
    if "session_arn" in value:
        out["SessionArn"] = value["session_arn"]
    if "approval_team_name" in value:
        out["ApprovalTeamName"] = value["approval_team_name"]
    if "approval_team_arn" in value:
        out["ApprovalTeamArn"] = value["approval_team_arn"]
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
    if "action_name" in value:
        out["ActionName"] = value["action_name"]
    if "protected_resource_arn" in value:
        out["ProtectedResourceArn"] = value["protected_resource_arn"]
    if "requester_service_principal" in value:
        out["RequesterServicePrincipal"] = value["requester_service_principal"]
    if "requester_principal_arn" in value:
        out["RequesterPrincipalArn"] = value["requester_principal_arn"]
    if "requester_region" in value:
        out["RequesterRegion"] = value["requester_region"]
    if "requester_account_id" in value:
        out["RequesterAccountId"] = value["requester_account_id"]
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
    if "action_completion_strategy" in value:
        import aws_sdk_mpa.types.action_completion_strategy

        out["ActionCompletionStrategy"] = (
            aws_sdk_mpa.types.action_completion_strategy.serialize_json(
                value["action_completion_strategy"]
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


def deserialize_json(data: dict) -> ListSessionsResponseSession:
    out: ListSessionsResponseSession = {}  # type: ignore[typeddict-item]
    if "SessionArn" in data:
        out["session_arn"] = data["SessionArn"]
    if "ApprovalTeamName" in data:
        out["approval_team_name"] = data["ApprovalTeamName"]
    if "ApprovalTeamArn" in data:
        out["approval_team_arn"] = data["ApprovalTeamArn"]
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
    if "ActionName" in data:
        out["action_name"] = data["ActionName"]
    if "ProtectedResourceArn" in data:
        out["protected_resource_arn"] = data["ProtectedResourceArn"]
    if "RequesterServicePrincipal" in data:
        out["requester_service_principal"] = data["RequesterServicePrincipal"]
    if "RequesterPrincipalArn" in data:
        out["requester_principal_arn"] = data["RequesterPrincipalArn"]
    if "RequesterRegion" in data:
        out["requester_region"] = data["RequesterRegion"]
    if "RequesterAccountId" in data:
        out["requester_account_id"] = data["RequesterAccountId"]
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
    if "ActionCompletionStrategy" in data:
        import aws_sdk_mpa.types.action_completion_strategy

        out["action_completion_strategy"] = (
            aws_sdk_mpa.types.action_completion_strategy.deserialize_json(
                data["ActionCompletionStrategy"]
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
