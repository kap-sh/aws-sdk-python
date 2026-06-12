"""Generated from Smithy shape ``com.amazonaws.rum#ListRumMetricsDestinationsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_rum.types.app_monitor_name
    import aws_sdk_rum.types.max_results_integer

class ListRumMetricsDestinationsRequest(TypedDict):
    app_monitor_name: "aws_sdk_rum.types.app_monitor_name.AppMonitorName"
    """<p>The name of the app monitor associated with the destinations that you want to retrieve.</p>"""
    max_results: NotRequired["aws_sdk_rum.types.max_results_integer.MaxResultsInteger"]
    """<p>The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.</p> <p>To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. </p>"""
    next_token: NotRequired["str"]
    """<p>Use the token returned by the previous operation to request the next page of results.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListRumMetricsDestinationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRumMetricsDestinationsRequest:
    out: ListRumMetricsDestinationsRequest = {}  # type: ignore[typeddict-item]
    return out