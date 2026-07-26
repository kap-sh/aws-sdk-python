"""Generated from Smithy shape ``com.amazonaws.autoscaling#PredefinedLoadMetricType``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

PredefinedLoadMetricType: TypeAlias = Literal[
    "ASGTotalCPUUtilization",
    "ASGTotalNetworkIn",
    "ASGTotalNetworkOut",
    "ALBTargetGroupRequestCount",
]


# --- awsQuery ser/de ---
def to_query_text(value: PredefinedLoadMetricType) -> str:
    return value


def from_query_text(text: str) -> PredefinedLoadMetricType:
    return cast(PredefinedLoadMetricType, text)


def serialize_query(
    value: PredefinedLoadMetricType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PredefinedLoadMetricType:
    return from_query_text(el.text or "")
