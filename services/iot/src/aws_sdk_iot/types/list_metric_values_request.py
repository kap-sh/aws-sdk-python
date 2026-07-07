"""Generated from Smithy shape ``com.amazonaws.iot#ListMetricValuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.behavior_metric
    import aws_sdk_iot.types.device_defender_thing_name
    import aws_sdk_iot.types.dimension_name
    import aws_sdk_iot.types.dimension_value_operator
    import aws_sdk_iot.types.max_results
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.timestamp


class ListMetricValuesRequest(TypedDict, closed=True):
    thing_name: "aws_sdk_iot.types.device_defender_thing_name.DeviceDefenderThingName"
    """<p>The name of the thing for which security profile metric values are returned.</p>"""
    metric_name: "aws_sdk_iot.types.behavior_metric.BehaviorMetric"
    """<p>The name of the security profile metric for which values are returned.</p>"""
    dimension_name: NotRequired["aws_sdk_iot.types.dimension_name.DimensionName"]
    """<p>The dimension name.</p>"""
    dimension_value_operator: NotRequired[
        "aws_sdk_iot.types.dimension_value_operator.DimensionValueOperator"
    ]
    """<p>The dimension value operator.</p>"""
    start_time: "aws_sdk_iot.types.timestamp.Timestamp"
    """<p>The start of the time period for which metric values are returned.</p>"""
    end_time: "aws_sdk_iot.types.timestamp.Timestamp"
    """<p>The end of the time period for which metric values are returned.</p>"""
    max_results: NotRequired["aws_sdk_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMetricValuesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMetricValuesRequest:
    out: ListMetricValuesRequest = {}  # type: ignore[typeddict-item]
    return out
