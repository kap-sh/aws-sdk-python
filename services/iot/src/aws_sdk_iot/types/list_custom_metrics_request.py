"""Generated from Smithy shape ``com.amazonaws.iot#ListCustomMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.max_results
    import aws_sdk_iot.types.next_token


class ListCustomMetricsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p> The token for the next set of results. </p>"""
    max_results: NotRequired["aws_sdk_iot.types.max_results.MaxResults"]
    """<p> The maximum number of results to return at one time. The default is 25. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomMetricsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCustomMetricsRequest:
    out: ListCustomMetricsRequest = {}  # type: ignore[typeddict-item]
    return out
