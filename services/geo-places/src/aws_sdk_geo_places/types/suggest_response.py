"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.query_refinement_list
    import aws_sdk_geo_places.types.suggest_result_item_list


class SuggestResponse(TypedDict):
    pricing_bucket: "str"
    r"""<p>The pricing bucket for which the query is charged at.</p> <p>For more information on pricing, please visit <a href=\"https://aws.amazon.com/location/pricing/\">Amazon Location Service Pricing</a>.</p>"""
    result_items: NotRequired[
        "aws_sdk_geo_places.types.suggest_result_item_list.SuggestResultItemList"
    ]
    """<p>List of places or results returned for a query. </p>"""
    query_refinements: NotRequired[
        "aws_sdk_geo_places.types.query_refinement_list.QueryRefinementList"
    ]
    r"""<p> Maximum number of query terms to be returned for use with a search text query. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestResponse) -> dict:
    out: dict = {}
    if "result_items" in value:
        import aws_sdk_geo_places.types.suggest_result_item_list

        out["ResultItems"] = (
            aws_sdk_geo_places.types.suggest_result_item_list.serialize_json(
                value["result_items"]
            )
        )
    if "query_refinements" in value:
        import aws_sdk_geo_places.types.query_refinement_list

        out["QueryRefinements"] = (
            aws_sdk_geo_places.types.query_refinement_list.serialize_json(
                value["query_refinements"]
            )
        )
    return out


def deserialize_json(data: dict) -> SuggestResponse:
    out: SuggestResponse = {}  # type: ignore[typeddict-item]
    if "ResultItems" in data:
        import aws_sdk_geo_places.types.suggest_result_item_list

        out["result_items"] = (
            aws_sdk_geo_places.types.suggest_result_item_list.deserialize_json(
                data["ResultItems"]
            )
        )
    if "QueryRefinements" in data:
        import aws_sdk_geo_places.types.query_refinement_list

        out["query_refinements"] = (
            aws_sdk_geo_places.types.query_refinement_list.deserialize_json(
                data["QueryRefinements"]
            )
        )
    return out
