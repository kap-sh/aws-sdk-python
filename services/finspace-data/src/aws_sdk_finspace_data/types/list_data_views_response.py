"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListDataViewsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.data_view_list
    import aws_sdk_finspace_data.types.pagination_token


class ListDataViewsResponse(TypedDict):
    next_token: NotRequired[
        "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
    ]
    """<p>A token that indicates where a results page should begin.</p>"""
    data_views: NotRequired["aws_sdk_finspace_data.types.data_view_list.DataViewList"]
    """<p>A list of Dataviews.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataViewsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "data_views" in value:
        import aws_sdk_finspace_data.types.data_view_list

        out["dataViews"] = aws_sdk_finspace_data.types.data_view_list.serialize_json(
            value["data_views"]
        )
    return out


def deserialize_json(data: dict) -> ListDataViewsResponse:
    out: ListDataViewsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "dataViews" in data:
        import aws_sdk_finspace_data.types.data_view_list

        out["data_views"] = aws_sdk_finspace_data.types.data_view_list.deserialize_json(
            data["dataViews"]
        )
    return out
