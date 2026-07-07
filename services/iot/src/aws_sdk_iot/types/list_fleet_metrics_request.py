"""Generated from Smithy shape ``com.amazonaws.iot#ListFleetMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.max_results
    import aws_sdk_iot.types.next_token


class ListFleetMetricsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <code>null</code> to receive the first set of results.</p>"""
    max_results: NotRequired["aws_sdk_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFleetMetricsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFleetMetricsRequest:
    out: ListFleetMetricsRequest = {}  # type: ignore[typeddict-item]
    return out
