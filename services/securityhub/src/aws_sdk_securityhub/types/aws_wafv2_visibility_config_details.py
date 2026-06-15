"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2VisibilityConfigDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsWafv2VisibilityConfigDetails(TypedDict):
    cloud_watch_metrics_enabled: NotRequired[
        "aws_sdk_securityhub.types.boolean.Boolean"
    ]
    r"""<p> A boolean indicating whether the associated resource sends metrics to Amazon CloudWatch. For the list of available metrics, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html#waf-metrics\">WAF metrics and dimensions</a> in the <i>WAF Developer Guide</i>. </p>"""
    metric_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A name of the Amazon CloudWatch metric. </p>"""
    sampled_requests_enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> A boolean indicating whether WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the WAF console. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2VisibilityConfigDetails) -> dict:
    out: dict = {}
    if "cloud_watch_metrics_enabled" in value:
        out["CloudWatchMetricsEnabled"] = value["cloud_watch_metrics_enabled"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "sampled_requests_enabled" in value:
        out["SampledRequestsEnabled"] = value["sampled_requests_enabled"]
    return out


def deserialize_json(data: dict) -> AwsWafv2VisibilityConfigDetails:
    out: AwsWafv2VisibilityConfigDetails = {}  # type: ignore[typeddict-item]
    if "CloudWatchMetricsEnabled" in data:
        out["cloud_watch_metrics_enabled"] = data["CloudWatchMetricsEnabled"]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "SampledRequestsEnabled" in data:
        out["sampled_requests_enabled"] = data["SampledRequestsEnabled"]
    return out
