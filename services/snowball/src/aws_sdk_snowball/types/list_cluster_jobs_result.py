"""Generated from Smithy shape ``com.amazonaws.snowball#ListClusterJobsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.job_list_entry_list
    import aws_sdk_snowball.types.string


class ListClusterJobsResult(TypedDict):
    job_list_entries: NotRequired[
        "aws_sdk_snowball.types.job_list_entry_list.JobListEntryList"
    ]
    """<p>Each <code>JobListEntry</code> object contains a job's state, a job's ID, and a value that indicates whether the job is a job part, in the case of export jobs. </p>"""
    next_token: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>HTTP requests are stateless. If you use the automatically generated <code>NextToken</code> value in your next <code>ListClusterJobsResult</code> call, your list of returned jobs will start from this point in the array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterJobsResult) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ListClusterJobsResult:
    out: ListClusterJobsResult = {}  # type: ignore[typeddict-item]
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
