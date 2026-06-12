"""Generated from Smithy shape ``com.amazonaws.iot#UpdateCustomMetricResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.custom_metric_arn
    import aws_sdk_iot.types.custom_metric_display_name
    import aws_sdk_iot.types.custom_metric_type
    import aws_sdk_iot.types.metric_name
    import aws_sdk_iot.types.timestamp


class UpdateCustomMetricResponse(TypedDict):
    metric_name: NotRequired["aws_sdk_iot.types.metric_name.MetricName"]
    """<p> The name of the custom metric. </p>"""
    metric_arn: NotRequired["aws_sdk_iot.types.custom_metric_arn.CustomMetricArn"]
    """<p> The Amazon Resource Number (ARN) of the custom metric. </p>"""
    metric_type: NotRequired["aws_sdk_iot.types.custom_metric_type.CustomMetricType"]
    """<p> The type of the custom metric. </p> <important> <p>The type <code>number</code> only takes a single metric value as an input, but while submitting the metrics value in the DeviceMetrics report, it must be passed as an array with a single value.</p> </important>"""
    display_name: NotRequired[
        "aws_sdk_iot.types.custom_metric_display_name.CustomMetricDisplayName"
    ]
    """<p> A friendly name in the console for the custom metric </p>"""
    creation_date: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p> The creation date of the custom metric in milliseconds since epoch. </p>"""
    last_modified_date: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p> The time the custom metric was last modified in milliseconds since epoch. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomMetricResponse) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["metricName"] = value["metric_name"]
    if "metric_arn" in value:
        out["metricArn"] = value["metric_arn"]
    if "metric_type" in value:
        import aws_sdk_iot.types.custom_metric_type

        out["metricType"] = aws_sdk_iot.types.custom_metric_type.serialize_json(
            value["metric_type"]
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "creation_date" in value:
        import aws_sdk_iot.types.timestamp

        out["creationDate"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import aws_sdk_iot.types.timestamp

        out["lastModifiedDate"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["last_modified_date"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCustomMetricResponse:
    out: UpdateCustomMetricResponse = {}  # type: ignore[typeddict-item]
    if "metricName" in data:
        out["metric_name"] = data["metricName"]
    if "metricArn" in data:
        out["metric_arn"] = data["metricArn"]
    if "metricType" in data:
        import aws_sdk_iot.types.custom_metric_type

        out["metric_type"] = aws_sdk_iot.types.custom_metric_type.deserialize_json(
            data["metricType"]
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "creationDate" in data:
        import aws_sdk_iot.types.timestamp

        out["creation_date"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    if "lastModifiedDate" in data:
        import aws_sdk_iot.types.timestamp

        out["last_modified_date"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["lastModifiedDate"]
        )
    return out
