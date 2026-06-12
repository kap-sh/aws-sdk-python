"""Generated from Smithy shape ``com.amazonaws.autoscaling#MetricStatistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

MetricStatistic: TypeAlias = Literal[
    "Average",
    "Minimum",
    "Maximum",
    "SampleCount",
    "Sum",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Average",
        "Minimum",
        "Maximum",
        "SampleCount",
        "Sum",
    )
)


def to_query_text(value: MetricStatistic) -> str:
    return value


def from_query_text(text: str) -> MetricStatistic:
    if text not in _VALUES:
        raise DeserializationError(f"unknown MetricStatistic value: {text!r}")
    return cast(MetricStatistic, text)


def serialize_query(
    value: MetricStatistic, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> MetricStatistic:
    return from_query_text(el.text or "")
