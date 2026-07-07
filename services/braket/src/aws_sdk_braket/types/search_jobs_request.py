"""Generated from Smithy shape ``com.amazonaws.braket#SearchJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.search_jobs_filter_list


class SearchJobsRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response.</p>"""
    filters: "aws_sdk_braket.types.search_jobs_filter_list.SearchJobsFilterList"
    """<p>Array of SearchJobsFilter objects to use when searching for hybrid jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchJobsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    import aws_sdk_braket.types.search_jobs_filter_list

    out["filters"] = aws_sdk_braket.types.search_jobs_filter_list.serialize_json(
        value["filters"]
    )
    return out


def deserialize_json(data: dict) -> SearchJobsRequest:
    out: SearchJobsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filters" in data:
        import aws_sdk_braket.types.search_jobs_filter_list

        out["filters"] = aws_sdk_braket.types.search_jobs_filter_list.deserialize_json(
            data["filters"]
        )
    else:
        raise DeserializationError("SearchJobsRequest.filters required")
    return out
