"""Generated from Smithy shape ``com.amazonaws.iotevents#ListInputsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.max_results
    import capo_iot_events.types.next_token


class ListInputsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iot_events.types.next_token.NextToken"]
    """<p>The token that you can use to return the next set of results.</p>"""
    max_results: NotRequired["capo_iot_events.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInputsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInputsRequest:
    out: ListInputsRequest = {}  # type: ignore[typeddict-item]
    return out
