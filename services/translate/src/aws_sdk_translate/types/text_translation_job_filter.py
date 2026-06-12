"""Generated from Smithy shape ``com.amazonaws.translate#TextTranslationJobFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_translate.types.job_name
    import aws_sdk_translate.types.job_status
    import aws_sdk_translate.types.timestamp


class TextTranslationJobFilter(TypedDict):
    job_name: NotRequired["aws_sdk_translate.types.job_name.JobName"]
    """<p>Filters the list of jobs by name.</p>"""
    job_status: NotRequired["aws_sdk_translate.types.job_status.JobStatus"]
    """<p>Filters the list of jobs based by job status.</p>"""
    submitted_before_time: NotRequired["aws_sdk_translate.types.timestamp.Timestamp"]
    """<p>Filters the list of jobs based on the time that the job was submitted for processing and returns only the jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.</p>"""
    submitted_after_time: NotRequired["aws_sdk_translate.types.timestamp.Timestamp"]
    """<p>Filters the list of jobs based on the time that the job was submitted for processing and returns only the jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextTranslationJobFilter) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import aws_sdk_translate.types.job_status

        out["JobStatus"] = aws_sdk_translate.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    if "submitted_before_time" in value:
        import aws_sdk_translate.types.timestamp

        out["SubmittedBeforeTime"] = (
            aws_sdk_translate.types.timestamp.serialize_aws_json_1_1(
                value["submitted_before_time"]
            )
        )
    if "submitted_after_time" in value:
        import aws_sdk_translate.types.timestamp

        out["SubmittedAfterTime"] = (
            aws_sdk_translate.types.timestamp.serialize_aws_json_1_1(
                value["submitted_after_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TextTranslationJobFilter:
    out: TextTranslationJobFilter = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobStatus" in data:
        import aws_sdk_translate.types.job_status

        out["job_status"] = aws_sdk_translate.types.job_status.deserialize_aws_json_1_1(
            data["JobStatus"]
        )
    if "SubmittedBeforeTime" in data:
        import aws_sdk_translate.types.timestamp

        out["submitted_before_time"] = (
            aws_sdk_translate.types.timestamp.deserialize_aws_json_1_1(
                data["SubmittedBeforeTime"]
            )
        )
    if "SubmittedAfterTime" in data:
        import aws_sdk_translate.types.timestamp

        out["submitted_after_time"] = (
            aws_sdk_translate.types.timestamp.deserialize_aws_json_1_1(
                data["SubmittedAfterTime"]
            )
        )
    return out
