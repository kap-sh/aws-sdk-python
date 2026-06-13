"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListMatchingJobsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.job_list
    import aws_sdk_entityresolution.types.next_token


class ListMatchingJobsOutput(TypedDict):
    jobs: NotRequired["aws_sdk_entityresolution.types.job_list.JobList"]
    """<p>A list of <code>JobSummary</code> objects, each of which contain the ID, status, start time, and end time of a job.</p>"""
    next_token: NotRequired["aws_sdk_entityresolution.types.next_token.NextToken"]
    """<p>The pagination token from the previous API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMatchingJobsOutput) -> dict:
    out: dict = {}
    if "jobs" in value:
        import aws_sdk_entityresolution.types.job_list

        out["jobs"] = aws_sdk_entityresolution.types.job_list.serialize_json(
            value["jobs"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMatchingJobsOutput:
    out: ListMatchingJobsOutput = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import aws_sdk_entityresolution.types.job_list

        out["jobs"] = aws_sdk_entityresolution.types.job_list.deserialize_json(
            data["jobs"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
