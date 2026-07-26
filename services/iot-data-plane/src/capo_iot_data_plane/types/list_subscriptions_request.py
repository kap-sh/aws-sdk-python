"""Generated from Smithy shape ``com.amazonaws.iotdataplane#ListSubscriptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_data_plane.types.client_id
    import capo_iot_data_plane.types.max_results
    import capo_iot_data_plane.types.next_token


class ListSubscriptionsRequest(TypedDict, closed=True):
    client_id: "capo_iot_data_plane.types.client_id.ClientId"
    """<p>The unique identifier of the MQTT client to list subscriptions for. The client ID can't start with a dollar sign ($).</p> <p>MQTT client IDs must be URL encoded (percent-encoded) when they contain characters that are not valid in HTTP requests, such as spaces, forward slashes (/), and UTF-8 characters.</p>"""
    next_token: NotRequired["capo_iot_data_plane.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired["capo_iot_data_plane.types.max_results.MaxResults"]
    """<p>The maximum number of subscriptions to return in a single request. By default, this is set to 20.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSubscriptionsRequest:
    out: ListSubscriptionsRequest = {}  # type: ignore[typeddict-item]
    return out
