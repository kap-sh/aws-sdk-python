"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListOpportunityFromEngagementTaskSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.context_identifier
    import aws_sdk_partnercentral_selling.types.date_time
    import aws_sdk_partnercentral_selling.types.engagement_identifier
    import aws_sdk_partnercentral_selling.types.opportunity_identifier
    import aws_sdk_partnercentral_selling.types.reason_code
    import aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier
    import aws_sdk_partnercentral_selling.types.task_arn
    import aws_sdk_partnercentral_selling.types.task_identifier
    import aws_sdk_partnercentral_selling.types.task_status


class ListOpportunityFromEngagementTaskSummary(TypedDict):
    task_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.task_identifier.TaskIdentifier"
    ]
    """<p>The unique identifier of the task for creating an opportunity from an engagement.</p>"""
    task_arn: NotRequired["aws_sdk_partnercentral_selling.types.task_arn.TaskArn"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the task within AWS. This ARN can be used for referencing the task in other AWS services or APIs.</p>"""
    start_time: NotRequired["aws_sdk_partnercentral_selling.types.date_time.DateTime"]
    """<p>The timestamp indicating when the task was initiated, in RFC 3339 format.</p>"""
    task_status: NotRequired[
        "aws_sdk_partnercentral_selling.types.task_status.TaskStatus"
    ]
    """<p>The current status of the task. Valid values are COMPLETE, INPROGRESS, or FAILED.</p>"""
    message: NotRequired["str"]
    """<p>A detailed message providing additional information about the task, especially useful in case of failures. This field may contain error details or other relevant information about the task's execution.</p>"""
    reason_code: NotRequired[
        "aws_sdk_partnercentral_selling.types.reason_code.ReasonCode"
    ]
    """<p>A code indicating the specific reason for a task failure. This field is populated when the task status is FAILED and provides a categorized reason for the failure.</p>"""
    opportunity_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    ]
    """<p>The unique identifier of the opportunity created as a result of the task. This field is populated when the task is completed successfully.</p>"""
    resource_snapshot_job_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier"
    ]
    """<p>The identifier of the resource snapshot job associated with this task, if a snapshot was created as part of the opportunity creation process.</p>"""
    engagement_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p>The unique identifier of the engagement from which the opportunity is being created. This field helps track the source of the opportunity creation task.</p>"""
    context_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.context_identifier.ContextIdentifier"
    ]
    """<p>The unique identifier of the engagement context associated with the opportunity creation task. This links the task to specific contextual information within the engagement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListOpportunityFromEngagementTaskSummary) -> dict:
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
    if "context_id" in value:
        out["ContextId"] = value["context_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListOpportunityFromEngagementTaskSummary:
    out: ListOpportunityFromEngagementTaskSummary = {}  # type: ignore[typeddict-item]
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
    if "ContextId" in data:
        out["context_id"] = data["ContextId"]
    return out
