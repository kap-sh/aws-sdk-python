"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportAutoScalingGroupRecommendationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.job_id
    import aws_sdk_compute_optimizer.types.s3_destination


class ExportAutoScalingGroupRecommendationsResponse(TypedDict):
    job_id: NotRequired["aws_sdk_compute_optimizer.types.job_id.JobId"]
    """<p>The identification number of the export job.</p> <p>Use the <a>DescribeRecommendationExportJobs</a> action, and specify the job ID to view the status of an export job.</p>"""
    s3_destination: NotRequired[
        "aws_sdk_compute_optimizer.types.s3_destination.S3Destination"
    ]
    """<p>An object that describes the destination Amazon S3 bucket of a recommendations export file.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ExportAutoScalingGroupRecommendationsResponse,
) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "s3_destination" in value:
        import aws_sdk_compute_optimizer.types.s3_destination

        out["s3Destination"] = (
            aws_sdk_compute_optimizer.types.s3_destination.serialize_aws_json_1_0(
                value["s3_destination"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ExportAutoScalingGroupRecommendationsResponse:
    out: ExportAutoScalingGroupRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "s3Destination" in data:
        import aws_sdk_compute_optimizer.types.s3_destination

        out["s3_destination"] = (
            aws_sdk_compute_optimizer.types.s3_destination.deserialize_aws_json_1_0(
                data["s3Destination"]
            )
        )
    return out
