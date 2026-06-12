"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchAllRelatedItemsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.next_token
    import aws_sdk_connectcases.types.search_all_related_items_response_item_list


class SearchAllRelatedItemsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""
    related_items: "aws_sdk_connectcases.types.search_all_related_items_response_item_list.SearchAllRelatedItemsResponseItemList"
    """<p>A list of items related to a case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAllRelatedItemsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_connectcases.types.search_all_related_items_response_item_list

    out["relatedItems"] = (
        aws_sdk_connectcases.types.search_all_related_items_response_item_list.serialize_json(
            value["related_items"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchAllRelatedItemsResponse:
    out: SearchAllRelatedItemsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "relatedItems" in data:
        import aws_sdk_connectcases.types.search_all_related_items_response_item_list

        out["related_items"] = (
            aws_sdk_connectcases.types.search_all_related_items_response_item_list.deserialize_json(
                data["relatedItems"]
            )
        )
    else:
        raise DeserializationError(
            "SearchAllRelatedItemsResponse.related_items required"
        )
    return out
