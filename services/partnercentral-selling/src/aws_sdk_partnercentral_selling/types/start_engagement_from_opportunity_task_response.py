"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#StartEngagementFromOpportunityTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.date_time
    import aws_sdk_partnercentral_selling.types.engagement_identifier
    import aws_sdk_partnercentral_selling.types.engagement_invitation_identifier
    import aws_sdk_partnercentral_selling.types.opportunity_identifier
    import aws_sdk_partnercentral_selling.types.reason_code
    import aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier
    import aws_sdk_partnercentral_selling.types.task_arn
    import aws_sdk_partnercentral_selling.types.task_identifier
    import aws_sdk_partnercentral_selling.types.task_status


class StartEngagementFromOpportunityTaskResponse(TypedDict):
    task_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.task_identifier.TaskIdentifier"
    ]
    """<p>The unique identifier of the task, used to track the task’s progress. This value follows a specific pattern: <code>^oit-[0-9a-z]{13}$</code>.</p>"""
    task_arn: NotRequired["aws_sdk_partnercentral_selling.types.task_arn.TaskArn"]
    """<p>The Amazon Resource Name (ARN) of the task, used for tracking and managing the task within AWS.</p>"""
    start_time: NotRequired["aws_sdk_partnercentral_selling.types.date_time.DateTime"]
    """<p>The timestamp indicating when the task was initiated. The format follows RFC 3339 section 5.6.</p>"""
    task_status: NotRequired[
        "aws_sdk_partnercentral_selling.types.task_status.TaskStatus"
    ]
    """<p>Indicates the current status of the task. Valid values include <code>IN_PROGRESS</code>, <code>COMPLETE</code>, and <code>FAILED</code>.</p>"""
    message: NotRequired["str"]
    """<p>If the task fails, this field contains a detailed message describing the failure and possible recovery steps.</p>"""
    reason_code: NotRequired[
        "aws_sdk_partnercentral_selling.types.reason_code.ReasonCode"
    ]
    """<p>Indicates the reason for task failure using an enumerated code.</p>"""
    opportunity_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    ]
    """<p>Returns the original opportunity identifier passed in the request, which is the unique identifier for the opportunity created in the partner’s system.</p>"""
    resource_snapshot_job_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier"
    ]
    """<p>The identifier of the resource snapshot job created to add the opportunity resource snapshot to the Engagement. Only populated if TaskStatus is COMPLETE</p>"""
    engagement_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p>The identifier of the newly created Engagement. Only populated if TaskStatus is COMPLETE.</p>"""
    engagement_invitation_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_invitation_identifier.EngagementInvitationIdentifier"
    ]
    """<p>The identifier of the new Engagement invitation. Only populated if TaskStatus is COMPLETE.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartEngagementFromOpportunityTaskResponse) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "start_time" in value:
        import aws_sdk_partnercentral_selling.types.date_time

        out["StartTime"] = (
            aws_sdk_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["start_time"]
            )
        )
    if "task_status" in value:
        import aws_sdk_partnercentral_selling.types.task_status

        out["TaskStatus"] = (
            aws_sdk_partnercentral_selling.types.task_status.serialize_aws_json_1_0(
                value["task_status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "reason_code" in value:
        import aws_sdk_partnercentral_selling.types.reason_code

        out["ReasonCode"] = (
            aws_sdk_partnercentral_selling.types.reason_code.serialize_aws_json_1_0(
                value["reason_code"]
            )
        )
    if "opportunity_id" in value:
        out["OpportunityId"] = value["opportunity_id"]
    if "resource_snapshot_job_id" in value:
        out["ResourceSnapshotJobId"] = value["resource_snapshot_job_id"]
    if "engagement_id" in value:
        out["EngagementId"] = value["engagement_id"]
    if "engagement_invitation_id" in value:
        out["EngagementInvitationId"] = value["engagement_invitation_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartEngagementFromOpportunityTaskResponse:
    out: StartEngagementFromOpportunityTaskResponse = {}  # type: ignore[typeddict-item]
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    if "TaskArn" in data:
        out["task_arn"] = data["TaskArn"]
    if "StartTime" in data:
        import aws_sdk_partnercentral_selling.types.date_time

        out["start_time"] = (
            aws_sdk_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    if "TaskStatus" in data:
        import aws_sdk_partnercentral_selling.types.task_status

        out["task_status"] = (
            aws_sdk_partnercentral_selling.types.task_status.deserialize_aws_json_1_0(
                data["TaskStatus"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "ReasonCode" in data:
        import aws_sdk_partnercentral_selling.types.reason_code

        out["reason_code"] = (
            aws_sdk_partnercentral_selling.types.reason_code.deserialize_aws_json_1_0(
                data["ReasonCode"]
            )
        )
    if "OpportunityId" in data:
        out["opportunity_id"] = data["OpportunityId"]
    if "ResourceSnapshotJobId" in data:
        out["resource_snapshot_job_id"] = data["ResourceSnapshotJobId"]
    if "EngagementId" in data:
        out["engagement_id"] = data["EngagementId"]
    if "EngagementInvitationId" in data:
        out["engagement_invitation_id"] = data["EngagementInvitationId"]
    return out
