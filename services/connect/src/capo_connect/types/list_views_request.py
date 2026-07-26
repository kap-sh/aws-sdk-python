"""Generated from Smithy shape ``com.amazonaws.connect#ListViewsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.max_results
    import capo_connect.types.view_type
    import capo_connect.types.views_instance_id
    import capo_connect.types.views_next_token


class ListViewsRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.views_instance_id.ViewsInstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.</p>"""
    type: NotRequired["capo_connect.types.view_type.ViewType"]
    """<p>The type of the view.</p>"""
    next_token: NotRequired["capo_connect.types.views_next_token.ViewsNextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page. The default MaxResult size is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListViewsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListViewsRequest:
    out: ListViewsRequest = {}  # type: ignore[typeddict-item]
    return out
