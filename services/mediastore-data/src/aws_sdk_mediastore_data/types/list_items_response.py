"""Generated from Smithy shape ``com.amazonaws.mediastoredata#ListItemsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediastore_data.types.item_list
    import aws_sdk_mediastore_data.types.pagination_token


class ListItemsResponse(TypedDict):
    items: NotRequired["aws_sdk_mediastore_data.types.item_list.ItemList"]
    """<p>The metadata entries for the folders and objects at the requested path.</p>"""
    next_token: NotRequired[
        "aws_sdk_mediastore_data.types.pagination_token.PaginationToken"
    ]
    """<p>The token that can be used in a request to view the next set of results. For example, you submit a <code>ListItems</code> request that matches 2,000 items with <code>MaxResults</code> set at 500. The service returns the first batch of results (up to 500) and a <code>NextToken</code> value that can be used to fetch the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListItemsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_mediastore_data.types.item_list

        out["Items"] = aws_sdk_mediastore_data.types.item_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListItemsResponse:
    out: ListItemsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_mediastore_data.types.item_list

        out["items"] = aws_sdk_mediastore_data.types.item_list.deserialize_json(
            data["Items"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
