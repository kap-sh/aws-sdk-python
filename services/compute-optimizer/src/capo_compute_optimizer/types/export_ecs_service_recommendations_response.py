"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportECSServiceRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.job_id
    import capo_compute_optimizer.types.s3_destination


class ExportECSServiceRecommendationsResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_compute_optimizer.types.job_id.JobId"]
    """<p> The identification number of the export job. </p> <p>To view the status of an export job, use the <a>DescribeRecommendationExportJobs</a> action and specify the job ID. </p>"""
    s3_destination: NotRequired[
        "capo_compute_optimizer.types.s3_destination.S3Destination"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportECSServiceRecommendationsResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "s3_destination" in value:
        import capo_compute_optimizer.types.s3_destination

        out["s3Destination"] = (
            capo_compute_optimizer.types.s3_destination.serialize_aws_json_1_0(
                value["s3_destination"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportECSServiceRecommendationsResponse:
    out: ExportECSServiceRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "s3Destination" in data:
        import capo_compute_optimizer.types.s3_destination

        out["s3_destination"] = (
            capo_compute_optimizer.types.s3_destination.deserialize_aws_json_1_0(
                data["s3Destination"]
            )
        )
    return out
