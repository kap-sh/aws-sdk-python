"""Generated from Smithy shape ``com.amazonaws.ec2#MetricType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

MetricType: TypeAlias = Literal["aggregate-latency",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: MetricType) -> str:
    return value


def from_ec2_query_text(text: str) -> MetricType:
    return cast(MetricType, text)


def serialize_ec2_query(
    value: MetricType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> MetricType:
    return from_ec2_query_text(el.text or "")
