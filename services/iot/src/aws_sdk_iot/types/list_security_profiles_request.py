"""Generated from Smithy shape ``com.amazonaws.iot#ListSecurityProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.dimension_name
    import aws_sdk_iot.types.max_results
    import aws_sdk_iot.types.metric_name
    import aws_sdk_iot.types.next_token


class ListSecurityProfilesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""
    dimension_name: NotRequired["aws_sdk_iot.types.dimension_name.DimensionName"]
    """<p>A filter to limit results to the security profiles that use the defined dimension. Cannot be used with <code>metricName</code> </p>"""
    metric_name: NotRequired["aws_sdk_iot.types.metric_name.MetricName"]
    """<p> The name of the custom metric. Cannot be used with <code>dimensionName</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityProfilesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSecurityProfilesRequest:
    out: ListSecurityProfilesRequest = {}  # type: ignore[typeddict-item]
    return out
