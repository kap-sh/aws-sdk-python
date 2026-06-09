"""Generated from Smithy shape ``com.amazonaws.ec2#MetricType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

MetricType: TypeAlias = Literal["aggregate-latency",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("aggregate-latency",))


_VALUES: frozenset[str] = frozenset(("aggregate-latency",))


def to_ec2_query_text(value: MetricType) -> str:
    return value


def from_ec2_query_text(text: str) -> MetricType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown MetricType value: {text!r}")
    return cast(MetricType, text)


def serialize_ec2_query(
    value: MetricType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> MetricType:
    return from_ec2_query_text(el.text or "")
