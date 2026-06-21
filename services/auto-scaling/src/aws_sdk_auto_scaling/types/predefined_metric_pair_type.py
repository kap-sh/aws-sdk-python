"""Generated from Smithy shape ``com.amazonaws.autoscaling#PredefinedMetricPairType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element

PredefinedMetricPairType: TypeAlias = Literal[
    "ASGCPUUtilization",
    "ASGNetworkIn",
    "ASGNetworkOut",
    "ALBRequestCount",
]


# --- awsQuery ser/de ---
def to_query_text(value: PredefinedMetricPairType) -> str:
    return value


def from_query_text(text: str) -> PredefinedMetricPairType:
    return cast(PredefinedMetricPairType, text)


def serialize_query(
    value: PredefinedMetricPairType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PredefinedMetricPairType:
    return from_query_text(el.text or "")
