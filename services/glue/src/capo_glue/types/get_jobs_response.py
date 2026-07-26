"""Generated from Smithy shape ``com.amazonaws.glue#GetJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic_string
    import capo_glue.types.job_list


class GetJobsResponse(TypedDict, closed=True):
    jobs: NotRequired["capo_glue.types.job_list.JobList"]
    """<p>A list of job definitions.</p>"""
    next_token: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if not all job definitions have yet been returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobsResponse) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_glue.types.job_list

        out["Jobs"] = capo_glue.types.job_list.serialize_aws_json_1_1(value["jobs"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobsResponse:
    out: GetJobsResponse = {}  # type: ignore[typeddict-item]
    if "Jobs" in data:
        import capo_glue.types.job_list

        out["jobs"] = capo_glue.types.job_list.deserialize_aws_json_1_1(data["Jobs"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
