"""Generated from Smithy shape ``com.amazonaws.deadline#SearchWorkersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.next_item_offset
    import aws_sdk_deadline.types.total_results
    import aws_sdk_deadline.types.worker_search_summaries


class SearchWorkersResponse(TypedDict):
    workers: "aws_sdk_deadline.types.worker_search_summaries.WorkerSearchSummaries"
    """<p>The workers for the search.</p>"""
    next_item_offset: NotRequired[
        "aws_sdk_deadline.types.next_item_offset.NextItemOffset"
    ]
    """<p>The next item offset for the search results.</p>"""
    total_results: "aws_sdk_deadline.types.total_results.TotalResults"
    """<p>The total number of results in the search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchWorkersResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.worker_search_summaries

    out["workers"] = aws_sdk_deadline.types.worker_search_summaries.serialize_json(
        value["workers"]
    )
    if "next_item_offset" in value:
        out["nextItemOffset"] = value["next_item_offset"]
    out["totalResults"] = value["total_results"]
    return out


def deserialize_json(data: dict) -> SearchWorkersResponse:
    out: SearchWorkersResponse = {}  # type: ignore[typeddict-item]
    if "workers" in data:
        import aws_sdk_deadline.types.worker_search_summaries

        out["workers"] = (
            aws_sdk_deadline.types.worker_search_summaries.deserialize_json(
                data["workers"]
            )
        )
    else:
        raise DeserializationError("SearchWorkersResponse.workers required")
    if "nextItemOffset" in data:
        out["next_item_offset"] = data["nextItemOffset"]
    if "totalResults" in data:
        out["total_results"] = data["totalResults"]
    else:
        raise DeserializationError("SearchWorkersResponse.total_results required")
    return out
