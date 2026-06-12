"""Generated from Smithy shape ``com.amazonaws.autoscaling#MetricType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

MetricType: TypeAlias = Literal[
    "ASGAverageCPUUtilization",
    "ASGAverageNetworkIn",
    "ASGAverageNetworkOut",
    "ALBRequestCountPerTarget",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASGAverageCPUUtilization",
        "ASGAverageNetworkIn",
        "ASGAverageNetworkOut",
        "ALBRequestCountPerTarget",
    )
)


def to_query_text(value: MetricType) -> str:
    return value


def from_query_text(text: str) -> MetricType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown MetricType value: {text!r}")
    return cast(MetricType, text)


def serialize_query(
    value: MetricType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> MetricType:
    return from_query_text(el.text or "")
