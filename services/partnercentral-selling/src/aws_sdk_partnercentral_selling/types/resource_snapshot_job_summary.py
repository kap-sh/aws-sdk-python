"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ResourceSnapshotJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.engagement_identifier
    import aws_sdk_partnercentral_selling.types.resource_snapshot_job_arn
    import aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier
    import aws_sdk_partnercentral_selling.types.resource_snapshot_job_status


class ResourceSnapshotJobSummary(TypedDict):
    id: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier"
    ]
    """<p> The unique identifier for the resource snapshot job within the AWS Partner Central system. This ID is used for direct references to the job within the service. </p>"""
    arn: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_snapshot_job_arn.ResourceSnapshotJobArn"
    ]
    """<p> The Amazon Resource Name (ARN) for the resource snapshot job. </p>"""
    engagement_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p>The unique identifier of the Engagement.</p>"""
    status: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_snapshot_job_status.ResourceSnapshotJobStatus"
    ]
    """<p>The current status of the snapshot job.</p> <p>Valid values:</p> <ul> <li> <p> STOPPED: The job is not currently running. </p> </li> <li> <p> RUNNING: The job is actively executing. </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSnapshotJobSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "engagement_id" in value:
        out["EngagementId"] = value["engagement_id"]
    if "status" in value:
        import aws_sdk_partnercentral_selling.types.resource_snapshot_job_status

        out["Status"] = (
            aws_sdk_partnercentral_selling.types.resource_snapshot_job_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceSnapshotJobSummary:
    out: ResourceSnapshotJobSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "EngagementId" in data:
        out["engagement_id"] = data["EngagementId"]
    if "Status" in data:
        import aws_sdk_partnercentral_selling.types.resource_snapshot_job_status

        out["status"] = (
            aws_sdk_partnercentral_selling.types.resource_snapshot_job_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
