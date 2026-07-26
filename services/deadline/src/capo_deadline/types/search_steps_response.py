"""Generated from Smithy shape ``com.amazonaws.deadline#SearchStepsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.next_item_offset
    import capo_deadline.types.step_search_summaries
    import capo_deadline.types.total_results


class SearchStepsResponse(TypedDict, closed=True):
    steps: "capo_deadline.types.step_search_summaries.StepSearchSummaries"
    """<p>The steps in the search.</p>"""
    next_item_offset: NotRequired["capo_deadline.types.next_item_offset.NextItemOffset"]
    """<p>The next item offset for the search results.</p>"""
    total_results: "capo_deadline.types.total_results.TotalResults"
    """<p>The total number of results in the search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchStepsResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.step_search_summaries

    out["steps"] = capo_deadline.types.step_search_summaries.serialize_json(
        value["steps"]
    )
    if "next_item_offset" in value:
        out["nextItemOffset"] = value["next_item_offset"]
    out["totalResults"] = value["total_results"]
    return out


def deserialize_json(data: dict) -> SearchStepsResponse:
    out: SearchStepsResponse = {}  # type: ignore[typeddict-item]
    if "steps" in data:
        import capo_deadline.types.step_search_summaries

        out["steps"] = capo_deadline.types.step_search_summaries.deserialize_json(
            data["steps"]
        )
    else:
        raise DeserializationError("SearchStepsResponse.steps required")
    if "nextItemOffset" in data:
        out["next_item_offset"] = data["nextItemOffset"]
    if "totalResults" in data:
        out["total_results"] = data["totalResults"]
    else:
        raise DeserializationError("SearchStepsResponse.total_results required")
    return out
