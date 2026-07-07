"""Generated from Smithy shape ``com.amazonaws.personalize#MetricAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.event_type
    import aws_sdk_personalize.types.metric_expression
    import aws_sdk_personalize.types.metric_name


class MetricAttribute(TypedDict, closed=True):
    event_type: "aws_sdk_personalize.types.event_type.EventType"
    """<p>The metric's event type.</p>"""
    metric_name: "aws_sdk_personalize.types.metric_name.MetricName"
    """<p>The metric's name. The name helps you identify the metric in Amazon CloudWatch or Amazon S3.</p>"""
    expression: "aws_sdk_personalize.types.metric_expression.MetricExpression"
    """<p>The attribute's expression. Available functions are <code>SUM()</code> or <code>SAMPLECOUNT()</code>. For SUM() functions, provide the dataset type (either Interactions or Items) and column to sum as a parameter. For example SUM(Items.PRICE).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricAttribute) -> dict:
    out: dict = {}
    out["eventType"] = value["event_type"]
    out["metricName"] = value["metric_name"]
    out["expression"] = value["expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricAttribute:
    out: MetricAttribute = {}  # type: ignore[typeddict-item]
    if "eventType" in data:
        out["event_type"] = data["eventType"]
    else:
        raise DeserializationError("MetricAttribute.event_type required")
    if "metricName" in data:
        out["metric_name"] = data["metricName"]
    else:
        raise DeserializationError("MetricAttribute.metric_name required")
    if "expression" in data:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError("MetricAttribute.expression required")
    return out
