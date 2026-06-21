"""Generated from Smithy shape ``com.amazonaws.autoscaling#MetricStatistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element

MetricStatistic: TypeAlias = Literal[
    "Average",
    "Minimum",
    "Maximum",
    "SampleCount",
    "Sum",
]


# --- awsQuery ser/de ---
def to_query_text(value: MetricStatistic) -> str:
    return value


def from_query_text(text: str) -> MetricStatistic:
    return cast(MetricStatistic, text)


def serialize_query(
    value: MetricStatistic, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> MetricStatistic:
    return from_query_text(el.text or "")
