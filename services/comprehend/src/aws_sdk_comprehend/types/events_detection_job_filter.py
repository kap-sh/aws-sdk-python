"""Generated from Smithy shape ``com.amazonaws.comprehend#EventsDetectionJobFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.job_name
    import aws_sdk_comprehend.types.job_status
    import aws_sdk_comprehend.types.timestamp


class EventsDetectionJobFilter(TypedDict):
    job_name: NotRequired["aws_sdk_comprehend.types.job_name.JobName"]
    """<p>Filters on the name of the events detection job.</p>"""
    job_status: NotRequired["aws_sdk_comprehend.types.job_status.JobStatus"]
    """<p>Filters the list of jobs based on job status. Returns only jobs with the specified status.</p>"""
    submit_time_before: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.</p>"""
    submit_time_after: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventsDetectionJobFilter) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import aws_sdk_comprehend.types.job_status

        out["JobStatus"] = aws_sdk_comprehend.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    if "submit_time_before" in value:
        import aws_sdk_comprehend.types.timestamp

        out["SubmitTimeBefore"] = (
            aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["submit_time_before"]
            )
        )
    if "submit_time_after" in value:
        import aws_sdk_comprehend.types.timestamp

        out["SubmitTimeAfter"] = (
            aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["submit_time_after"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventsDetectionJobFilter:
    out: EventsDetectionJobFilter = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobStatus" in data:
        import aws_sdk_comprehend.types.job_status

        out["job_status"] = (
            aws_sdk_comprehend.types.job_status.deserialize_aws_json_1_1(
                data["JobStatus"]
            )
        )
    if "SubmitTimeBefore" in data:
        import aws_sdk_comprehend.types.timestamp

        out["submit_time_before"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["SubmitTimeBefore"]
            )
        )
    if "SubmitTimeAfter" in data:
        import aws_sdk_comprehend.types.timestamp

        out["submit_time_after"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["SubmitTimeAfter"]
            )
        )
    return out
