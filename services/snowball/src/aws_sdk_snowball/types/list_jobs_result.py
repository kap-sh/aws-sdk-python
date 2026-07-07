"""Generated from Smithy shape ``com.amazonaws.snowball#ListJobsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snowball.types.job_list_entry_list
    import aws_sdk_snowball.types.string


class ListJobsResult(TypedDict, closed=True):
    job_list_entries: NotRequired[
        "aws_sdk_snowball.types.job_list_entry_list.JobListEntryList"
    ]
    """<p>Each <code>JobListEntry</code> object contains a job's state, a job's ID, and a value that indicates whether the job is a job part, in the case of export jobs. </p>"""
    next_token: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>HTTP requests are stateless. If you use this automatically generated <code>NextToken</code> value in your next <code>ListJobs</code> call, your returned <code>JobListEntry</code> objects will start from this point in the array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListJobsResult) -> dict:
    out: dict = {}
    if "job_list_entries" in value:
        import aws_sdk_snowball.types.job_list_entry_list

        out["JobListEntries"] = (
            aws_sdk_snowball.types.job_list_entry_list.serialize_aws_json_1_1(
                value["job_list_entries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListJobsResult:
    out: ListJobsResult = {}  # type: ignore[typeddict-item]
    if "JobListEntries" in data:
        import aws_sdk_snowball.types.job_list_entry_list

        out["job_list_entries"] = (
            aws_sdk_snowball.types.job_list_entry_list.deserialize_aws_json_1_1(
                data["JobListEntries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
