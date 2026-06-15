"""Generated from Smithy shape ``com.amazonaws.snowball#CreateClusterResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.cluster_id
    import aws_sdk_snowball.types.job_list_entry_list


class CreateClusterResult(TypedDict):
    cluster_id: NotRequired["aws_sdk_snowball.types.cluster_id.ClusterId"]
    """<p>The automatically generated ID for a cluster.</p>"""
    job_list_entries: NotRequired[
        "aws_sdk_snowball.types.job_list_entry_list.JobListEntryList"
    ]
    r"""<p>List of jobs created for this cluster. For syntax, see <a href=\"http://amazonaws.com/snowball/latest/api-reference/API_ListJobs.html#API_ListJobs_ResponseSyntax\">ListJobsResult$JobListEntries</a> in this guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterResult) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "job_list_entries" in value:
        import aws_sdk_snowball.types.job_list_entry_list

        out["JobListEntries"] = (
            aws_sdk_snowball.types.job_list_entry_list.serialize_aws_json_1_1(
                value["job_list_entries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterResult:
    out: CreateClusterResult = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "JobListEntries" in data:
        import aws_sdk_snowball.types.job_list_entry_list

        out["job_list_entries"] = (
            aws_sdk_snowball.types.job_list_entry_list.deserialize_aws_json_1_1(
                data["JobListEntries"]
            )
        )
    return out
