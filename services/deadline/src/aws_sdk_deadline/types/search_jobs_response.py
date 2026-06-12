"""Generated from Smithy shape ``com.amazonaws.deadline#SearchJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.job_search_summaries
    import aws_sdk_deadline.types.next_item_offset
    import aws_sdk_deadline.types.total_results


class SearchJobsResponse(TypedDict):
    jobs: "aws_sdk_deadline.types.job_search_summaries.JobSearchSummaries"
    """<p>The jobs in the search.</p>"""
    next_item_offset: NotRequired[
        "aws_sdk_deadline.types.next_item_offset.NextItemOffset"
    ]
    """<p>The next item offset for the search results.</p>"""
    total_results: "aws_sdk_deadline.types.total_results.TotalResults"
    """<p>The total number of results in the search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchJobsResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.job_search_summaries

    out["jobs"] = aws_sdk_deadline.types.job_search_summaries.serialize_json(
        value["jobs"]
    )
    if "next_item_offset" in value:
        out["nextItemOffset"] = value["next_item_offset"]
    out["totalResults"] = value["total_results"]
    return out


def deserialize_json(data: dict) -> SearchJobsResponse:
    out: SearchJobsResponse = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import aws_sdk_deadline.types.job_search_summaries

        out["jobs"] = aws_sdk_deadline.types.job_search_summaries.deserialize_json(
            data["jobs"]
        )
    else:
        raise DeserializationError("SearchJobsResponse.jobs required")
    if "nextItemOffset" in data:
        out["next_item_offset"] = data["nextItemOffset"]
    if "totalResults" in data:
        out["total_results"] = data["totalResults"]
    else:
        raise DeserializationError("SearchJobsResponse.total_results required")
    return out
