"""Generated from Smithy shape ``com.amazonaws.mediaconvert#SearchJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of_job
    import capo_mediaconvert.types.__string


class SearchJobsResponse(TypedDict, closed=True):
    jobs: NotRequired["capo_mediaconvert.types.__list_of_job.__listOfJob"]
    """List of jobs."""
    next_token: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Use this string to request the next batch of jobs."""


# --- restJson1 ser/de ---
def serialize_json(value: SearchJobsResponse) -> dict:
    out: dict = {}
    if "jobs" in value:
        import capo_mediaconvert.types.__list_of_job

        out["jobs"] = capo_mediaconvert.types.__list_of_job.serialize_json(
            value["jobs"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchJobsResponse:
    out: SearchJobsResponse = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import capo_mediaconvert.types.__list_of_job

        out["jobs"] = capo_mediaconvert.types.__list_of_job.deserialize_json(
            data["jobs"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
