"""Generated from Smithy shape ``com.amazonaws.batch#ListJobsByConsumableResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.consumable_resource_properties
    import aws_sdk_batch.types.long
    import aws_sdk_batch.types.string


class ListJobsByConsumableResourceSummary(TypedDict, closed=True):
    job_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    job_queue_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job queue.</p>"""
    job_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the job.</p>"""
    job_definition_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job definition.</p>"""
    share_identifier: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The fair-share scheduling identifier for the job.</p>"""
    job_status: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The status of the job. Can be one of:</p> <ul> <li> <p> <code>SUBMITTED</code> </p> </li> <li> <p> <code>PENDING</code> </p> </li> <li> <p> <code>RUNNABLE</code> </p> </li> <li> <p> <code>STARTING</code> </p> </li> <li> <p> <code>RUNNING</code> </p> </li> <li> <p> <code>SUCCEEDED</code> </p> </li> <li> <p> <code>FAILED</code> </p> </li> </ul>"""
    quantity: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The total amount of the consumable resource that is available.</p>"""
    status_reason: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>A short, human-readable string to provide more details for the current status of the job.</p>"""
    started_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp for when the job was started. More specifically, it's when the job transitioned from the <code>STARTING</code> state to the <code>RUNNING</code> state.</p>"""
    created_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the consumable resource was created.</p>"""
    consumable_resource_properties: NotRequired[
        "aws_sdk_batch.types.consumable_resource_properties.ConsumableResourceProperties"
    ]
    """<p>Contains a list of consumable resources required by the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsByConsumableResourceSummary) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_queue_arn" in value:
        out["jobQueueArn"] = value["job_queue_arn"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "job_definition_arn" in value:
        out["jobDefinitionArn"] = value["job_definition_arn"]
    if "share_identifier" in value:
        out["shareIdentifier"] = value["share_identifier"]
    if "job_status" in value:
        out["jobStatus"] = value["job_status"]
    if "quantity" in value:
        out["quantity"] = value["quantity"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "started_at" in value:
        out["startedAt"] = value["started_at"]
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "consumable_resource_properties" in value:
        import aws_sdk_batch.types.consumable_resource_properties

        out["consumableResourceProperties"] = (
            aws_sdk_batch.types.consumable_resource_properties.serialize_json(
                value["consumable_resource_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListJobsByConsumableResourceSummary:
    out: ListJobsByConsumableResourceSummary = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "jobQueueArn" in data:
        out["job_queue_arn"] = data["jobQueueArn"]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "jobDefinitionArn" in data:
        out["job_definition_arn"] = data["jobDefinitionArn"]
    if "shareIdentifier" in data:
        out["share_identifier"] = data["shareIdentifier"]
    if "jobStatus" in data:
        out["job_status"] = data["jobStatus"]
    if "quantity" in data:
        out["quantity"] = data["quantity"]
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "startedAt" in data:
        out["started_at"] = data["startedAt"]
    if "createdAt" in data:
        out["created_at"] = data["createdAt"]
    if "consumableResourceProperties" in data:
        import aws_sdk_batch.types.consumable_resource_properties

        out["consumable_resource_properties"] = (
            aws_sdk_batch.types.consumable_resource_properties.deserialize_json(
                data["consumableResourceProperties"]
            )
        )
    return out
