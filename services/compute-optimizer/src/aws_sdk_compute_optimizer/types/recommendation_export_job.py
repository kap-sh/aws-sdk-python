"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationExportJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.creation_timestamp
    import aws_sdk_compute_optimizer.types.export_destination
    import aws_sdk_compute_optimizer.types.failure_reason
    import aws_sdk_compute_optimizer.types.job_id
    import aws_sdk_compute_optimizer.types.job_status
    import aws_sdk_compute_optimizer.types.last_updated_timestamp
    import aws_sdk_compute_optimizer.types.resource_type


class RecommendationExportJob(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_compute_optimizer.types.job_id.JobId"]
    """<p>The identification number of the export job.</p>"""
    destination: NotRequired[
        "aws_sdk_compute_optimizer.types.export_destination.ExportDestination"
    ]
    """<p>An object that describes the destination of the export file.</p>"""
    resource_type: NotRequired[
        "aws_sdk_compute_optimizer.types.resource_type.ResourceType"
    ]
    """<p>The resource type of the exported recommendations.</p>"""
    status: NotRequired["aws_sdk_compute_optimizer.types.job_status.JobStatus"]
    """<p>The status of the export job.</p>"""
    creation_timestamp: NotRequired[
        "aws_sdk_compute_optimizer.types.creation_timestamp.CreationTimestamp"
    ]
    """<p>The timestamp of when the export job was created.</p>"""
    last_updated_timestamp: NotRequired[
        "aws_sdk_compute_optimizer.types.last_updated_timestamp.LastUpdatedTimestamp"
    ]
    """<p>The timestamp of when the export job was last updated.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_compute_optimizer.types.failure_reason.FailureReason"
    ]
    """<p>The reason for an export job failure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationExportJob) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "destination" in value:
        import aws_sdk_compute_optimizer.types.export_destination

        out["destination"] = (
            aws_sdk_compute_optimizer.types.export_destination.serialize_aws_json_1_0(
                value["destination"]
            )
        )
    if "resource_type" in value:
        import aws_sdk_compute_optimizer.types.resource_type

        out["resourceType"] = (
            aws_sdk_compute_optimizer.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "status" in value:
        import aws_sdk_compute_optimizer.types.job_status

        out["status"] = (
            aws_sdk_compute_optimizer.types.job_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "creation_timestamp" in value:
        import aws_sdk_compute_optimizer.types.creation_timestamp

        out["creationTimestamp"] = (
            aws_sdk_compute_optimizer.types.creation_timestamp.serialize_aws_json_1_0(
                value["creation_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import aws_sdk_compute_optimizer.types.last_updated_timestamp

        out["lastUpdatedTimestamp"] = (
            aws_sdk_compute_optimizer.types.last_updated_timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendationExportJob:
    out: RecommendationExportJob = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "destination" in data:
        import aws_sdk_compute_optimizer.types.export_destination

        out["destination"] = (
            aws_sdk_compute_optimizer.types.export_destination.deserialize_aws_json_1_0(
                data["destination"]
            )
        )
    if "resourceType" in data:
        import aws_sdk_compute_optimizer.types.resource_type

        out["resource_type"] = (
            aws_sdk_compute_optimizer.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    if "status" in data:
        import aws_sdk_compute_optimizer.types.job_status

        out["status"] = (
            aws_sdk_compute_optimizer.types.job_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "creationTimestamp" in data:
        import aws_sdk_compute_optimizer.types.creation_timestamp

        out["creation_timestamp"] = (
            aws_sdk_compute_optimizer.types.creation_timestamp.deserialize_aws_json_1_0(
                data["creationTimestamp"]
            )
        )
    if "lastUpdatedTimestamp" in data:
        import aws_sdk_compute_optimizer.types.last_updated_timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_compute_optimizer.types.last_updated_timestamp.deserialize_aws_json_1_0(
                data["lastUpdatedTimestamp"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
