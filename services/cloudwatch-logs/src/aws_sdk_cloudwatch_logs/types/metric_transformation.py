"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#MetricTransformation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.default_value
    import aws_sdk_cloudwatch_logs.types.dimensions
    import aws_sdk_cloudwatch_logs.types.metric_name
    import aws_sdk_cloudwatch_logs.types.metric_namespace
    import aws_sdk_cloudwatch_logs.types.metric_value
    import aws_sdk_cloudwatch_logs.types.standard_unit


class MetricTransformation(TypedDict):
    metric_name: "aws_sdk_cloudwatch_logs.types.metric_name.MetricName"
    """<p>The name of the CloudWatch metric.</p>"""
    metric_namespace: "aws_sdk_cloudwatch_logs.types.metric_namespace.MetricNamespace"
    r"""<p>A custom namespace to contain your metric in CloudWatch. Use namespaces to group together metrics that are similar. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace\">Namespaces</a>.</p>"""
    metric_value: "aws_sdk_cloudwatch_logs.types.metric_value.MetricValue"
    """<p>The value to publish to the CloudWatch metric when a filter pattern matches a log event.</p>"""
    default_value: NotRequired[
        "aws_sdk_cloudwatch_logs.types.default_value.DefaultValue"
    ]
    """<p>(Optional) The value to emit when a filter pattern does not match a log event. This value can be null.</p>"""
    dimensions: NotRequired["aws_sdk_cloudwatch_logs.types.dimensions.Dimensions"]
    r"""<p>The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions.</p> <important> <p>Metrics extracted from log events are charged as custom metrics. To prevent unexpected high charges, do not specify high-cardinality fields such as <code>IPAddress</code> or <code>requestID</code> as dimensions. Each different value found for a dimension is treated as a separate metric and accrues charges as a separate custom metric. </p> <p>CloudWatch Logs disables a metric filter if it generates 1000 different name/value pairs for your specified dimensions within a certain amount of time. This helps to prevent accidental high charges.</p> <p>You can also set up a billing alarm to alert you if your charges are higher than expected. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html\"> Creating a Billing Alarm to Monitor Your Estimated Amazon Web Services Charges</a>. </p> </important>"""
    unit: NotRequired["aws_sdk_cloudwatch_logs.types.standard_unit.StandardUnit"]
    """<p>The unit to assign to the metric. If you omit this, the unit is set as <code>None</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricTransformation) -> dict:
    out: dict = {}
    out["metricName"] = value["metric_name"]
    out["metricNamespace"] = value["metric_namespace"]
    out["metricValue"] = value["metric_value"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "dimensions" in value:
        import aws_sdk_cloudwatch_logs.types.dimensions

        out["dimensions"] = (
            aws_sdk_cloudwatch_logs.types.dimensions.serialize_aws_json_1_1(
                value["dimensions"]
            )
        )
    if "unit" in value:
        import aws_sdk_cloudwatch_logs.types.standard_unit

        out["unit"] = (
            aws_sdk_cloudwatch_logs.types.standard_unit.serialize_aws_json_1_1(
                value["unit"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricTransformation:
    out: MetricTransformation = {}  # type: ignore[typeddict-item]
    if "metricName" in data:
        out["metric_name"] = data["metricName"]
    else:
        raise DeserializationError("MetricTransformation.metric_name required")
    if "metricNamespace" in data:
        out["metric_namespace"] = data["metricNamespace"]
    else:
        raise DeserializationError("MetricTransformation.metric_namespace required")
    if "metricValue" in data:
        out["metric_value"] = data["metricValue"]
    else:
        raise DeserializationError("MetricTransformation.metric_value required")
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    if "dimensions" in data:
        import aws_sdk_cloudwatch_logs.types.dimensions

        out["dimensions"] = (
            aws_sdk_cloudwatch_logs.types.dimensions.deserialize_aws_json_1_1(
                data["dimensions"]
            )
        )
    if "unit" in data:
        import aws_sdk_cloudwatch_logs.types.standard_unit

        out["unit"] = (
            aws_sdk_cloudwatch_logs.types.standard_unit.deserialize_aws_json_1_1(
                data["unit"]
            )
        )
    return out
