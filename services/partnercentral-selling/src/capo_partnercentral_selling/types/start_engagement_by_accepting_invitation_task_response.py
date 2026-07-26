"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#StartEngagementByAcceptingInvitationTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.engagement_invitation_identifier
    import capo_partnercentral_selling.types.opportunity_identifier
    import capo_partnercentral_selling.types.reason_code
    import capo_partnercentral_selling.types.resource_snapshot_job_identifier
    import capo_partnercentral_selling.types.task_arn
    import capo_partnercentral_selling.types.task_identifier
    import capo_partnercentral_selling.types.task_status


class StartEngagementByAcceptingInvitationTaskResponse(TypedDict, closed=True):
    task_id: NotRequired[
        "capo_partnercentral_selling.types.task_identifier.TaskIdentifier"
    ]
    """<p>The unique identifier of the task, used to track the task’s progress.</p>"""
    task_arn: NotRequired["capo_partnercentral_selling.types.task_arn.TaskArn"]
    """<p>The Amazon Resource Name (ARN) of the task, used for tracking and managing the task within AWS.</p>"""
    start_time: NotRequired["capo_partnercentral_selling.types.date_time.DateTime"]
    """<p>The timestamp indicating when the task was initiated. The format follows RFC 3339 section 5.6.</p>"""
    task_status: NotRequired["capo_partnercentral_selling.types.task_status.TaskStatus"]
    """<p>Indicates the current status of the task.</p>"""
    message: NotRequired["str"]
    """<p>If the task fails, this field contains a detailed message describing the failure and possible recovery steps.</p>"""
    reason_code: NotRequired["capo_partnercentral_selling.types.reason_code.ReasonCode"]
    """<p>Indicates the reason for task failure using an enumerated code.</p>"""
    opportunity_id: NotRequired[
        "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    ]
    """<p>Returns the original opportunity identifier passed in the request. This is the unique identifier for the opportunity.</p>"""
    resource_snapshot_job_id: NotRequired[
        "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier"
    ]
    """<p>The identifier of the Resource Snapshot Job created as part of this task.</p>"""
    engagement_invitation_id: NotRequired[
        "capo_partnercentral_selling.types.engagement_invitation_identifier.EngagementInvitationIdentifier"
    ]
    """<p>Returns the identifier of the engagement invitation that was accepted and used to create the opportunity.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: StartEngagementByAcceptingInvitationTaskResponse,
) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "start_time" in value:
        import capo_partnercentral_selling.types.date_time

        out["StartTime"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["start_time"]
            )
        )
    if "task_status" in value:
        import capo_partnercentral_selling.types.task_status

        out["TaskStatus"] = (
            capo_partnercentral_selling.types.task_status.serialize_aws_json_1_0(
                value["task_status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "reason_code" in value:
        import capo_partnercentral_selling.types.reason_code

        out["ReasonCode"] = (
            capo_partnercentral_selling.types.reason_code.serialize_aws_json_1_0(
                value["reason_code"]
            )
        )
    if "opportunity_id" in value:
        out["OpportunityId"] = value["opportunity_id"]
    if "resource_snapshot_job_id" in value:
        out["ResourceSnapshotJobId"] = value["resource_snapshot_job_id"]
    if "engagement_invitation_id" in value:
        out["EngagementInvitationId"] = value["engagement_invitation_id"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> StartEngagementByAcceptingInvitationTaskResponse:
    out: StartEngagementByAcceptingInvitationTaskResponse = {}  # type: ignore[typeddict-item]
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    if "TaskArn" in data:
        out["task_arn"] = data["TaskArn"]
    if "StartTime" in data:
        import capo_partnercentral_selling.types.date_time

        out["start_time"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    if "TaskStatus" in data:
        import capo_partnercentral_selling.types.task_status

        out["task_status"] = (
            capo_partnercentral_selling.types.task_status.deserialize_aws_json_1_0(
                data["TaskStatus"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "ReasonCode" in data:
        import capo_partnercentral_selling.types.reason_code

        out["reason_code"] = (
            capo_partnercentral_selling.types.reason_code.deserialize_aws_json_1_0(
                data["ReasonCode"]
            )
        )
    if "OpportunityId" in data:
        out["opportunity_id"] = data["OpportunityId"]
    if "ResourceSnapshotJobId" in data:
        out["resource_snapshot_job_id"] = data["ResourceSnapshotJobId"]
    if "EngagementInvitationId" in data:
        out["engagement_invitation_id"] = data["EngagementInvitationId"]
    return out
