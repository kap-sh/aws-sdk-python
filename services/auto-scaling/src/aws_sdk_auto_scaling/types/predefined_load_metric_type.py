"""Generated from Smithy shape ``com.amazonaws.autoscaling#PredefinedLoadMetricType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

PredefinedLoadMetricType: TypeAlias = Literal[
    "ASGTotalCPUUtilization",
    "ASGTotalNetworkIn",
    "ASGTotalNetworkOut",
    "ALBTargetGroupRequestCount",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASGTotalCPUUtilization",
        "ASGTotalNetworkIn",
        "ASGTotalNetworkOut",
        "ALBTargetGroupRequestCount",
    )
)


def to_query_text(value: PredefinedLoadMetricType) -> str:
    return value


def from_query_text(text: str) -> PredefinedLoadMetricType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PredefinedLoadMetricType value: {text!r}")
    return cast(PredefinedLoadMetricType, text)


def serialize_query(
    value: PredefinedLoadMetricType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PredefinedLoadMetricType:
    return from_query_text(el.text or "")
