"""Generated from Smithy shape ``com.amazonaws.connect#ListPredefinedAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.max_result100
    import capo_connect.types.next_token


class ListPredefinedAttributesRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPredefinedAttributesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPredefinedAttributesRequest:
    out: ListPredefinedAttributesRequest = {}  # type: ignore[typeddict-item]
    return out
