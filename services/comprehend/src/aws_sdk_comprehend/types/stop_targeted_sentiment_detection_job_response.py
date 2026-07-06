"""Generated from Smithy shape ``com.amazonaws.comprehend#StopTargetedSentimentDetectionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.job_id
    import aws_sdk_comprehend.types.job_status


class StopTargetedSentimentDetectionJobResponse(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_comprehend.types.job_id.JobId"]
    """<p>The identifier of the targeted sentiment detection job to stop.</p>"""
    job_status: NotRequired["aws_sdk_comprehend.types.job_status.JobStatus"]
    """<p>Either <code>STOP_REQUESTED</code> if the job is currently running, or <code>STOPPED</code> if the job was previously stopped with the <code>StopSentimentDetectionJob</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopTargetedSentimentDetectionJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_status" in value:
        import aws_sdk_comprehend.types.job_status

        out["JobStatus"] = aws_sdk_comprehend.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopTargetedSentimentDetectionJobResponse:
    out: StopTargetedSentimentDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "JobStatus" in data:
        import aws_sdk_comprehend.types.job_status

        out["job_status"] = (
            aws_sdk_comprehend.types.job_status.deserialize_aws_json_1_1(
                data["JobStatus"]
            )
        )
    return out
