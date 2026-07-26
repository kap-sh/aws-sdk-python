"""Generated from Smithy shape ``com.amazonaws.autoscaling#PredefinedScalingMetricType``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

PredefinedScalingMetricType: TypeAlias = Literal[
    "ASGAverageCPUUtilization",
    "ASGAverageNetworkIn",
    "ASGAverageNetworkOut",
    "ALBRequestCountPerTarget",
]


# --- awsQuery ser/de ---
def to_query_text(value: PredefinedScalingMetricType) -> str:
    return value


def from_query_text(text: str) -> PredefinedScalingMetricType:
    return cast(PredefinedScalingMetricType, text)


def serialize_query(
    value: PredefinedScalingMetricType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PredefinedScalingMetricType:
    return from_query_text(el.text or "")
