"""Generated from Smithy shape ``com.amazonaws.ec2#DisableAwsNetworkPerformanceMetricSubscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.metric_type
    import aws_sdk_ec2.types.statistic_type
    import aws_sdk_ec2.types.string


class DisableAwsNetworkPerformanceMetricSubscriptionRequest(TypedDict):
    source: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source Region or Availability Zone that the metric subscription is disabled for. For example, <code>us-east-1</code>.</p>"""
    destination: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The target Region or Availability Zone that the metric subscription is disabled for. For example, <code>eu-north-1</code>.</p>"""
    metric: NotRequired["aws_sdk_ec2.types.metric_type.MetricType"]
    """<p>The metric used for the disabled subscription.</p>"""
    statistic: NotRequired["aws_sdk_ec2.types.statistic_type.StatisticType"]
    """<p>The statistic used for the disabled subscription. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableAwsNetworkPerformanceMetricSubscriptionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "source" in value:
        pairs.append((f"{prefix}.Source", str(value["source"])))
    if "destination" in value:
        pairs.append((f"{prefix}.Destination", str(value["destination"])))
    if "metric" in value:
        import aws_sdk_ec2.types.metric_type

        aws_sdk_ec2.types.metric_type.serialize_ec2_query(
            value["metric"], pairs, f"{prefix}.Metric"
        )
    if "statistic" in value:
        import aws_sdk_ec2.types.statistic_type

        aws_sdk_ec2.types.statistic_type.serialize_ec2_query(
            value["statistic"], pairs, f"{prefix}.Statistic"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> DisableAwsNetworkPerformanceMetricSubscriptionRequest:
    out: DisableAwsNetworkPerformanceMetricSubscriptionRequest = {}  # type: ignore[typeddict-item]
    child_source = el.find("Source")
    if child_source is not None:
        out["source"] = str(child_source.text or "")
    child_destination = el.find("Destination")
    if child_destination is not None:
        out["destination"] = str(child_destination.text or "")
    child_metric = el.find("Metric")
    if child_metric is not None:
        import aws_sdk_ec2.types.metric_type

        out["metric"] = aws_sdk_ec2.types.metric_type.deserialize_ec2_query(
            child_metric
        )
    child_statistic = el.find("Statistic")
    if child_statistic is not None:
        import aws_sdk_ec2.types.statistic_type

        out["statistic"] = aws_sdk_ec2.types.statistic_type.deserialize_ec2_query(
            child_statistic
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
