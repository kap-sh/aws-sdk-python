"""Generated from Smithy shape ``com.amazonaws.braket#SearchJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_braket.errors import DeserializationError

if TYPE_CHECKING:
    import capo_braket.types.job_summary_list


class SearchJobsResponse(TypedDict, closed=True):
    jobs: "capo_braket.types.job_summary_list.JobSummaryList"
    """<p>An array of <code>JobSummary</code> objects for devices that match the specified filter values.</p>"""
    next_token: NotRequired["str"]
    """<p>A token used for pagination of results, or <code>null</code> if there are no additional results. Use the token value in a subsequent request to continue search where the previous request ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchJobsResponse) -> dict:
    out: dict = {}
    import capo_braket.types.job_summary_list

    out["jobs"] = capo_braket.types.job_summary_list.serialize_json(value["jobs"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchJobsResponse:
    out: SearchJobsResponse = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import capo_braket.types.job_summary_list

        out["jobs"] = capo_braket.types.job_summary_list.deserialize_json(data["jobs"])
    else:
        raise DeserializationError("SearchJobsResponse.jobs required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
