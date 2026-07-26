"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ComprehendMedicalAsyncJobFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.job_name
    import capo_comprehendmedical.types.job_status
    import capo_comprehendmedical.types.timestamp


class ComprehendMedicalAsyncJobFilter(TypedDict, closed=True):
    job_name: NotRequired["capo_comprehendmedical.types.job_name.JobName"]
    """<p>Filters on the name of the job.</p>"""
    job_status: NotRequired["capo_comprehendmedical.types.job_status.JobStatus"]
    """<p>Filters the list of jobs based on job status. Returns only jobs with the specified status.</p>"""
    submit_time_before: NotRequired["capo_comprehendmedical.types.timestamp.Timestamp"]
    """<p>Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.</p>"""
    submit_time_after: NotRequired["capo_comprehendmedical.types.timestamp.Timestamp"]
    """<p>Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComprehendMedicalAsyncJobFilter) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import capo_comprehendmedical.types.job_status

        out["JobStatus"] = (
            capo_comprehendmedical.types.job_status.serialize_aws_json_1_1(
                value["job_status"]
            )
        )
    if "submit_time_before" in value:
        import capo_comprehendmedical.types.timestamp

        out["SubmitTimeBefore"] = (
            capo_comprehendmedical.types.timestamp.serialize_aws_json_1_1(
                value["submit_time_before"]
            )
        )
    if "submit_time_after" in value:
        import capo_comprehendmedical.types.timestamp

        out["SubmitTimeAfter"] = (
            capo_comprehendmedical.types.timestamp.serialize_aws_json_1_1(
                value["submit_time_after"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComprehendMedicalAsyncJobFilter:
    out: ComprehendMedicalAsyncJobFilter = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobStatus" in data:
        import capo_comprehendmedical.types.job_status

        out["job_status"] = (
            capo_comprehendmedical.types.job_status.deserialize_aws_json_1_1(
                data["JobStatus"]
            )
        )
    if "SubmitTimeBefore" in data:
        import capo_comprehendmedical.types.timestamp

        out["submit_time_before"] = (
            capo_comprehendmedical.types.timestamp.deserialize_aws_json_1_1(
                data["SubmitTimeBefore"]
            )
        )
    if "SubmitTimeAfter" in data:
        import capo_comprehendmedical.types.timestamp

        out["submit_time_after"] = (
            capo_comprehendmedical.types.timestamp.deserialize_aws_json_1_1(
                data["SubmitTimeAfter"]
            )
        )
    return out
