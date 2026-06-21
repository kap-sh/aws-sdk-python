"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceBandwidthWeighting``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

InstanceBandwidthWeighting: TypeAlias = Literal[
    "default",
    "vpc-1",
    "ebs-1",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: InstanceBandwidthWeighting) -> str:
    return value


def from_ec2_query_text(text: str) -> InstanceBandwidthWeighting:
    return cast(InstanceBandwidthWeighting, text)


def serialize_ec2_query(
    value: InstanceBandwidthWeighting, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InstanceBandwidthWeighting:
    return from_ec2_query_text(el.text or "")
