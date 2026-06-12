"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricStreamFilterMetricNames``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.metric_name

MetricStreamFilterMetricNames: TypeAlias = list[
    "aws_sdk_cloudwatch.types.metric_name.MetricName"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricStreamFilterMetricNames, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> MetricStreamFilterMetricNames:
    out: MetricStreamFilterMetricNames = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: MetricStreamFilterMetricNames, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> MetricStreamFilterMetricNames:
    out: MetricStreamFilterMetricNames = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricStreamFilterMetricNames) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> MetricStreamFilterMetricNames:
    return list(data)
