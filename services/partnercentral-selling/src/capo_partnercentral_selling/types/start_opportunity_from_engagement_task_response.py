"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#StartOpportunityFromEngagementTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.context_identifier
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.engagement_identifier
    import capo_partnercentral_selling.types.opportunity_identifier
    import capo_partnercentral_selling.types.reason_code
    import capo_partnercentral_selling.types.resource_snapshot_job_identifier
    import capo_partnercentral_selling.types.task_arn
    import capo_partnercentral_selling.types.task_identifier
    import capo_partnercentral_selling.types.task_status


class StartOpportunityFromEngagementTaskResponse(TypedDict, closed=True):
    task_id: NotRequired[
        "capo_partnercentral_selling.types.task_identifier.TaskIdentifier"
    ]
    """<p>The unique identifier of the task, used to track the task's progress.</p>"""
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
    """<p>The unique identifier of the opportunity created as a result of the task. This field is populated when the task is completed successfully.</p>"""
    resource_snapshot_job_id: NotRequired[
        "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier"
    ]
    """<p>The identifier of the resource snapshot job created as part of the opportunity creation process.</p>"""
    engagement_id: NotRequired[
        "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p>The unique identifier of the engagement from which the opportunity was created.</p>"""
    context_id: NotRequired[
        "capo_partnercentral_selling.types.context_identifier.ContextIdentifier"
    ]
    """<p>The unique identifier of the engagement context used to create the opportunity.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartOpportunityFromEngagementTaskResponse) -> dict:
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
    if "engagement_id" in value:
        out["EngagementId"] = value["engagement_id"]
    if "context_id" in value:
        out["ContextId"] = value["context_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartOpportunityFromEngagementTaskResponse:
    out: StartOpportunityFromEngagementTaskResponse = {}  # type: ignore[typeddict-item]
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
    if "EngagementId" in data:
        out["engagement_id"] = data["EngagementId"]
    if "ContextId" in data:
        out["context_id"] = data["ContextId"]
    return out
