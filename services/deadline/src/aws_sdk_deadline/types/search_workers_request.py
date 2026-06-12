"""Generated from Smithy shape ``com.amazonaws.deadline#SearchWorkersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_ids
    import aws_sdk_deadline.types.integer
    import aws_sdk_deadline.types.search_grouped_filter_expressions
    import aws_sdk_deadline.types.search_sort_expressions


class SearchWorkersRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID in the workers search.</p>"""
    filter_expressions: NotRequired[
        "aws_sdk_deadline.types.search_grouped_filter_expressions.SearchGroupedFilterExpressions"
    ]
    """<p>The search terms for a resource.</p>"""
    sort_expressions: NotRequired[
        "aws_sdk_deadline.types.search_sort_expressions.SearchSortExpressions"
    ]
    """<p>The search terms for a resource.</p>"""
    item_offset: "aws_sdk_deadline.types.integer.Integer"
    """<p>The offset for the search results.</p>"""
    page_size: "aws_sdk_deadline.types.integer.Integer"
    """<p>Specifies the number of results to return.</p>"""
    fleet_ids: "aws_sdk_deadline.types.fleet_ids.FleetIds"
    """<p>The fleet ID of the workers to search for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchWorkersRequest) -> dict:
    out: dict = {}
    if "filter_expressions" in value:
        import aws_sdk_deadline.types.search_grouped_filter_expressions

        out["filterExpressions"] = (
            aws_sdk_deadline.types.search_grouped_filter_expressions.serialize_json(
                value["filter_expressions"]
            )
        )
    if "sort_expressions" in value:
        import aws_sdk_deadline.types.search_sort_expressions

        out["sortExpressions"] = (
            aws_sdk_deadline.types.search_sort_expressions.serialize_json(
                value["sort_expressions"]
            )
        )
    out["itemOffset"] = value["item_offset"]
    out["pageSize"] = value.get("page_size", 100)
    import aws_sdk_deadline.types.fleet_ids

    out["fleetIds"] = aws_sdk_deadline.types.fleet_ids.serialize_json(
        value["fleet_ids"]
    )
    return out


def deserialize_json(data: dict) -> SearchWorkersRequest:
    out: SearchWorkersRequest = {}  # type: ignore[typeddict-item]
    if "filterExpressions" in data:
        import aws_sdk_deadline.types.search_grouped_filter_expressions

        out["filter_expressions"] = (
            aws_sdk_deadline.types.search_grouped_filter_expressions.deserialize_json(
                data["filterExpressions"]
            )
        )
    if "sortExpressions" in data:
        import aws_sdk_deadline.types.search_sort_expressions

        out["sort_expressions"] = (
            aws_sdk_deadline.types.search_sort_expressions.deserialize_json(
                data["sortExpressions"]
            )
        )
    if "itemOffset" in data:
        out["item_offset"] = data["itemOffset"]
    else:
        raise DeserializationError("SearchWorkersRequest.item_offset required")
    if "pageSize" in data:
        out["page_size"] = data["pageSize"]
    else:
        out["page_size"] = 100
    if "fleetIds" in data:
        import aws_sdk_deadline.types.fleet_ids

        out["fleet_ids"] = aws_sdk_deadline.types.fleet_ids.deserialize_json(
            data["fleetIds"]
        )
    else:
        raise DeserializationError("SearchWorkersRequest.fleet_ids required")
    return out
