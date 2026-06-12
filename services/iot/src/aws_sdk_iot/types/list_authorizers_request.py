"""Generated from Smithy shape ``com.amazonaws.iot#ListAuthorizersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.ascending_order
    import aws_sdk_iot.types.authorizer_status
    import aws_sdk_iot.types.marker
    import aws_sdk_iot.types.page_size


class ListAuthorizersRequest(TypedDict):
    page_size: NotRequired["aws_sdk_iot.types.page_size.PageSize"]
    """<p>The maximum number of results to return at one time.</p>"""
    marker: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>A marker used to get the next set of results.</p>"""
    ascending_order: "aws_sdk_iot.types.ascending_order.AscendingOrder"
    """<p>Return the list of authorizers in ascending alphabetical order.</p>"""
    status: NotRequired["aws_sdk_iot.types.authorizer_status.AuthorizerStatus"]
    """<p>The status of the list authorizers request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuthorizersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAuthorizersRequest:
    out: ListAuthorizersRequest = {}  # type: ignore[typeddict-item]
    return out
