"""Generated from Smithy shape ``com.amazonaws.iot#DescribeCustomMetricRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.metric_name


class DescribeCustomMetricRequest(TypedDict):
    metric_name: "aws_sdk_iot.types.metric_name.MetricName"
    """<p> The name of the custom metric. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCustomMetricRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeCustomMetricRequest:
    out: DescribeCustomMetricRequest = {}  # type: ignore[typeddict-item]
    return out
