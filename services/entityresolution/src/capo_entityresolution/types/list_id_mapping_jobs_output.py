"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListIdMappingJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.job_list
    import capo_entityresolution.types.next_token


class ListIdMappingJobsOutput(TypedDict, closed=True):
    jobs: NotRequired["capo_entityresolution.types.job_list.JobList"]
    """<p>A list of <code>JobSummary</code> objects.</p>"""
    next_token: NotRequired["capo_entityresolution.types.next_token.NextToken"]
    """<p>The pagination token from the previous API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdMappingJobsOutput) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_entityresolution.types.job_list

        out["jobs"] = capo_entityresolution.types.job_list.serialize_json(value["jobs"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIdMappingJobsOutput:
    out: ListIdMappingJobsOutput = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import capo_entityresolution.types.job_list

        out["jobs"] = capo_entityresolution.types.job_list.deserialize_json(
            data["jobs"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
