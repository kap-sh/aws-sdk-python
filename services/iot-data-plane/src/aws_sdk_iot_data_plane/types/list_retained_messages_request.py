"""Generated from Smithy shape ``com.amazonaws.iotdataplane#ListRetainedMessagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_data_plane.types.max_results
    import aws_sdk_iot_data_plane.types.next_token


class ListRetainedMessagesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_iot_data_plane.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired["aws_sdk_iot_data_plane.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRetainedMessagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRetainedMessagesRequest:
    out: ListRetainedMessagesRequest = {}  # type: ignore[typeddict-item]
    return out
