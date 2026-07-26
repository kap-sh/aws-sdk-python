"""Generated from Smithy shape ``com.amazonaws.deadline#SearchStepsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.integer
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_ids
    import capo_deadline.types.search_grouped_filter_expressions
    import capo_deadline.types.search_sort_expressions


class SearchStepsRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID to use for the step search.</p>"""
    filter_expressions: NotRequired[
        "capo_deadline.types.search_grouped_filter_expressions.SearchGroupedFilterExpressions"
    ]
    """<p>The search terms for a resource.</p>"""
    sort_expressions: NotRequired[
        "capo_deadline.types.search_sort_expressions.SearchSortExpressions"
    ]
    """<p>The search terms for a resource.</p>"""
    item_offset: "capo_deadline.types.integer.Integer"
    """<p>The offset for the search results.</p>"""
    page_size: "capo_deadline.types.integer.Integer"
    """<p>Specifies the number of results to return.</p>"""
    queue_ids: "capo_deadline.types.queue_ids.QueueIds"
    """<p>The queue IDs in the step search.</p>"""
    job_id: NotRequired["capo_deadline.types.job_id.JobId"]
    """<p>The job ID to use in the step search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchStepsRequest) -> dict:
    out: dict = {}
    if "filter_expressions" in value:
        import capo_deadline.types.search_grouped_filter_expressions

        out["filterExpressions"] = (
            capo_deadline.types.search_grouped_filter_expressions.serialize_json(
                value["filter_expressions"]
            )
        )
    if "sort_expressions" in value:
        import capo_deadline.types.search_sort_expressions

        out["sortExpressions"] = (
            capo_deadline.types.search_sort_expressions.serialize_json(
                value["sort_expressions"]
            )
        )
    out["itemOffset"] = value["item_offset"]
    out["pageSize"] = value.get("page_size", 100)
    import capo_deadline.types.queue_ids

    out["queueIds"] = capo_deadline.types.queue_ids.serialize_json(value["queue_ids"])
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> SearchStepsRequest:
    out: SearchStepsRequest = {}  # type: ignore[typeddict-item]
    if "filterExpressions" in data:
        import capo_deadline.types.search_grouped_filter_expressions

        out["filter_expressions"] = (
            capo_deadline.types.search_grouped_filter_expressions.deserialize_json(
                data["filterExpressions"]
            )
        )
    if "sortExpressions" in data:
        import capo_deadline.types.search_sort_expressions

        out["sort_expressions"] = (
            capo_deadline.types.search_sort_expressions.deserialize_json(
                data["sortExpressions"]
            )
        )
    if "itemOffset" in data:
        out["item_offset"] = data["itemOffset"]
    else:
        raise DeserializationError("SearchStepsRequest.item_offset required")
    if "pageSize" in data:
        out["page_size"] = data["pageSize"]
    else:
        out["page_size"] = 100
    if "queueIds" in data:
        import capo_deadline.types.queue_ids

        out["queue_ids"] = capo_deadline.types.queue_ids.deserialize_json(
            data["queueIds"]
        )
    else:
        raise DeserializationError("SearchStepsRequest.queue_ids required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    return out
