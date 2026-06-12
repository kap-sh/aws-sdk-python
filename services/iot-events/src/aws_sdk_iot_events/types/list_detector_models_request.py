"""Generated from Smithy shape ``com.amazonaws.iotevents#ListDetectorModelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.max_results
    import aws_sdk_iot_events.types.next_token


class ListDetectorModelsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_iot_events.types.next_token.NextToken"]
    """<p>The token that you can use to return the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_iot_events.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDetectorModelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDetectorModelsRequest:
    out: ListDetectorModelsRequest = {}  # type: ignore[typeddict-item]
    return out
