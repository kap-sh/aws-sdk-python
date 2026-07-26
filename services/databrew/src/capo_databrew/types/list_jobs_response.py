"""Generated from Smithy shape ``com.amazonaws.databrew#ListJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.job_list
    import capo_databrew.types.next_token


class ListJobsResponse(TypedDict, closed=True):
    jobs: "capo_databrew.types.job_list.JobList"
    """<p>A list of jobs that are defined.</p>"""
    next_token: NotRequired["capo_databrew.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsResponse) -> dict:
    out: dict = {}
    import capo_databrew.types.job_list

    out["Jobs"] = capo_databrew.types.job_list.serialize_json(value["jobs"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobsResponse:
    out: ListJobsResponse = {}  # type: ignore[typeddict-item]
    if "Jobs" in data:
        import capo_databrew.types.job_list

        out["jobs"] = capo_databrew.types.job_list.deserialize_json(data["Jobs"])
    else:
        raise DeserializationError("ListJobsResponse.jobs required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
