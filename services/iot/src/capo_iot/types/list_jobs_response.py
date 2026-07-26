"""Generated from Smithy shape ``com.amazonaws.iot#ListJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.job_summary_list
    import capo_iot.types.next_token


class ListJobsResponse(TypedDict, closed=True):
    jobs: NotRequired["capo_iot.types.job_summary_list.JobSummaryList"]
    """<p>A list of jobs.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsResponse) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_iot.types.job_summary_list

        out["jobs"] = capo_iot.types.job_summary_list.serialize_json(value["jobs"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobsResponse:
    out: ListJobsResponse = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import capo_iot.types.job_summary_list

        out["jobs"] = capo_iot.types.job_summary_list.deserialize_json(data["jobs"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
