"""Generated from Smithy shape ``com.amazonaws.applicationsignals#MetricReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.aws_account_id
    import aws_sdk_application_signals.types.dimensions
    import aws_sdk_application_signals.types.metric_name
    import aws_sdk_application_signals.types.metric_type
    import aws_sdk_application_signals.types.namespace


class MetricReference(TypedDict, closed=True):
    namespace: "aws_sdk_application_signals.types.namespace.Namespace"
    r"""<p>The namespace of the metric. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace\">CloudWatchNamespaces</a>.</p>"""
    metric_type: "aws_sdk_application_signals.types.metric_type.MetricType"
    """<p>Used to display the appropriate statistics in the CloudWatch console.</p>"""
    dimensions: NotRequired["aws_sdk_application_signals.types.dimensions.Dimensions"]
    r"""<p>An array of one or more dimensions that further define the metric. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension\">CloudWatchDimensions</a>.</p>"""
    metric_name: "aws_sdk_application_signals.types.metric_name.MetricName"
    """<p>The name of the metric.</p>"""
    account_id: NotRequired[
        "aws_sdk_application_signals.types.aws_account_id.AwsAccountId"
    ]
    """<p>Amazon Web Services account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricReference) -> dict:
    out: dict = {}
    out["Namespace"] = value["namespace"]
    out["MetricType"] = value["metric_type"]
    if "dimensions" in value:
        import aws_sdk_application_signals.types.dimensions

        out["Dimensions"] = aws_sdk_application_signals.types.dimensions.serialize_json(
            value["dimensions"]
        )
    out["MetricName"] = value["metric_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> MetricReference:
    out: MetricReference = {}  # type: ignore[typeddict-item]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    else:
        raise DeserializationError("MetricReference.namespace required")
    if "MetricType" in data:
        out["metric_type"] = data["MetricType"]
    else:
        raise DeserializationError("MetricReference.metric_type required")
    if "Dimensions" in data:
        import aws_sdk_application_signals.types.dimensions

        out["dimensions"] = (
            aws_sdk_application_signals.types.dimensions.deserialize_json(
                data["Dimensions"]
            )
        )
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    else:
        raise DeserializationError("MetricReference.metric_name required")
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    return out
