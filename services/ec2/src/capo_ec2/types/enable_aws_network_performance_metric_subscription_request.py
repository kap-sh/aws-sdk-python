"""Generated from Smithy shape ``com.amazonaws.ec2#EnableAwsNetworkPerformanceMetricSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.metric_type
    import capo_ec2.types.statistic_type
    import capo_ec2.types.string


class EnableAwsNetworkPerformanceMetricSubscriptionRequest(TypedDict, closed=True):
    source: NotRequired["capo_ec2.types.string.String"]
    """<p>The source Region (like <code>us-east-1</code>) or Availability Zone ID (like <code>use1-az1</code>) that the metric subscription is enabled for. If you use Availability Zone IDs, the Source and Destination Availability Zones must be in the same Region.</p>"""
    destination: NotRequired["capo_ec2.types.string.String"]
    """<p>The target Region (like <code>us-east-2</code>) or Availability Zone ID (like <code>use2-az2</code>) that the metric subscription is enabled for. If you use Availability Zone IDs, the Source and Destination Availability Zones must be in the same Region.</p>"""
    metric: NotRequired["capo_ec2.types.metric_type.MetricType"]
    """<p>The metric used for the enabled subscription.</p>"""
    statistic: NotRequired["capo_ec2.types.statistic_type.StatisticType"]
    """<p>The statistic used for the enabled subscription.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableAwsNetworkPerformanceMetricSubscriptionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source" in value:
        pairs.append((f"{key_prefix}Source", str(value["source"])))
    if "destination" in value:
        pairs.append((f"{key_prefix}Destination", str(value["destination"])))
    if "metric" in value:
        import capo_ec2.types.metric_type

        capo_ec2.types.metric_type.serialize_ec2_query(
            value["metric"], pairs, f"{key_prefix}Metric"
        )
    if "statistic" in value:
        import capo_ec2.types.statistic_type

        capo_ec2.types.statistic_type.serialize_ec2_query(
            value["statistic"], pairs, f"{key_prefix}Statistic"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> EnableAwsNetworkPerformanceMetricSubscriptionRequest:
    out: EnableAwsNetworkPerformanceMetricSubscriptionRequest = {}  # type: ignore[typeddict-item]
    child_source = el.find("Source")
    if child_source is not None:
        out["source"] = str(child_source.text or "")
    child_destination = el.find("Destination")
    if child_destination is not None:
        out["destination"] = str(child_destination.text or "")
    child_metric = el.find("Metric")
    if child_metric is not None:
        import capo_ec2.types.metric_type

        out["metric"] = capo_ec2.types.metric_type.deserialize_ec2_query(child_metric)
    child_statistic = el.find("Statistic")
    if child_statistic is not None:
        import capo_ec2.types.statistic_type

        out["statistic"] = capo_ec2.types.statistic_type.deserialize_ec2_query(
            child_statistic
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
