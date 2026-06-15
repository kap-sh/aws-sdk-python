"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchTextResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.search_text_result_item_list
    import aws_sdk_geo_places.types.token


class SearchTextResponse(TypedDict):
    pricing_bucket: "str"
    r"""<p>The pricing bucket for which the query is charged at.</p> <p>For more information on pricing, please visit <a href=\"https://aws.amazon.com/location/pricing/\">Amazon Location Service Pricing</a>.</p>"""
    result_items: NotRequired[
        "aws_sdk_geo_places.types.search_text_result_item_list.SearchTextResultItemList"
    ]
    """<p>List of places or results returned for a query. </p>"""
    next_token: NotRequired["aws_sdk_geo_places.types.token.Token"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchTextResponse) -> dict:
    out: dict = {}
    if "result_items" in value:
        import aws_sdk_geo_places.types.search_text_result_item_list

        out["ResultItems"] = (
            aws_sdk_geo_places.types.search_text_result_item_list.serialize_json(
                value["result_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchTextResponse:
    out: SearchTextResponse = {}  # type: ignore[typeddict-item]
    if "ResultItems" in data:
        import aws_sdk_geo_places.types.search_text_result_item_list

        out["result_items"] = (
            aws_sdk_geo_places.types.search_text_result_item_list.deserialize_json(
                data["ResultItems"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
