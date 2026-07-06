"""Generated from Smithy shape ``com.amazonaws.sagemaker#JobSecondaryStatusTransition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.job_secondary_status
    import aws_sdk_sagemaker.types.string
    import aws_sdk_sagemaker.types.timestamp


class JobSecondaryStatusTransition(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_sagemaker.types.job_secondary_status.JobSecondaryStatus"
    ]
    """<p>The secondary status of the job at this transition point.</p>"""
    start_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the status transition started.</p>"""
    end_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the status transition ended.</p>"""
    status_message: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>A detailed message about the status transition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobSecondaryStatusTransition) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sagemaker.types.job_secondary_status

        out["Status"] = (
            aws_sdk_sagemaker.types.job_secondary_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "start_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["StartTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["EndTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobSecondaryStatusTransition:
    out: JobSecondaryStatusTransition = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sagemaker.types.job_secondary_status

        out["status"] = (
            aws_sdk_sagemaker.types.job_secondary_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["start_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["end_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
