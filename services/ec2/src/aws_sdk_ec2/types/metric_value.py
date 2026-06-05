"""Generated from Smithy shape ``com.amazonaws.ec2#MetricValue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.metric


class MetricValue(TypedDict):
    metric: NotRequired["aws_sdk_ec2.types.metric.Metric"]
    """<p> The name of the metric. </p>"""
    value: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p> The numerical value of the metric for the specified statistic and time period. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MetricValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "metric" in value:
        import aws_sdk_ec2.types.metric

        aws_sdk_ec2.types.metric.serialize_ec2_query(
            value["metric"], pairs, f"{prefix}.Metric"
        )
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_ec2_query(el: Element) -> MetricValue:
    out: MetricValue = {}  # type: ignore[typeddict-item]
    child_metric = el.find("Metric")
    if child_metric is not None:
        import aws_sdk_ec2.types.metric

        out["metric"] = aws_sdk_ec2.types.metric.deserialize_ec2_query(child_metric)
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = float(child_value.text or "")
    return out
