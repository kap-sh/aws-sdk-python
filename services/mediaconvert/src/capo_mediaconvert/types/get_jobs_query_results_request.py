"""Generated from Smithy shape ``com.amazonaws.mediaconvert#GetJobsQueryResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string


class GetJobsQueryResultsRequest(TypedDict, closed=True):
    id: "capo_mediaconvert.types.__string.__string"
    """The ID of the jobs query."""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobsQueryResultsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetJobsQueryResultsRequest:
    out: GetJobsQueryResultsRequest = {}  # type: ignore[typeddict-item]
    return out
