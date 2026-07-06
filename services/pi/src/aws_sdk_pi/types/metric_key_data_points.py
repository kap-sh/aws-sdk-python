"""Generated from Smithy shape ``com.amazonaws.pi#MetricKeyDataPoints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pi.types.data_points_list
    import aws_sdk_pi.types.response_resource_metric_key


class MetricKeyDataPoints(TypedDict, closed=True):
    key: NotRequired[
        "aws_sdk_pi.types.response_resource_metric_key.ResponseResourceMetricKey"
    ]
    """<p>The dimensions to which the data points apply.</p>"""
    data_points: NotRequired["aws_sdk_pi.types.data_points_list.DataPointsList"]
    """<p>An array of timestamp-value pairs, representing measurements over a period of time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricKeyDataPoints) -> dict:
    out: dict = {}
    if "key" in value:
        import aws_sdk_pi.types.response_resource_metric_key

        out["Key"] = (
            aws_sdk_pi.types.response_resource_metric_key.serialize_aws_json_1_1(
                value["key"]
            )
        )
    if "data_points" in value:
        import aws_sdk_pi.types.data_points_list

        out["DataPoints"] = aws_sdk_pi.types.data_points_list.serialize_aws_json_1_1(
            value["data_points"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricKeyDataPoints:
    out: MetricKeyDataPoints = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import aws_sdk_pi.types.response_resource_metric_key

        out["key"] = (
            aws_sdk_pi.types.response_resource_metric_key.deserialize_aws_json_1_1(
                data["Key"]
            )
        )
    if "DataPoints" in data:
        import aws_sdk_pi.types.data_points_list

        out["data_points"] = aws_sdk_pi.types.data_points_list.deserialize_aws_json_1_1(
            data["DataPoints"]
        )
    return out
