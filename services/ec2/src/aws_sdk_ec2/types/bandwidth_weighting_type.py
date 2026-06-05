"""Generated from Smithy shape ``com.amazonaws.ec2#BandwidthWeightingType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

BandwidthWeightingType: TypeAlias = Literal[
    "default",
    "vpc-1",
    "ebs-1",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "vpc-1",
        "ebs-1",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "vpc-1",
        "ebs-1",
    )
)


def to_ec2_query_text(value: BandwidthWeightingType) -> str:
    return value


def from_ec2_query_text(text: str) -> BandwidthWeightingType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BandwidthWeightingType value: {text!r}")
    return cast(BandwidthWeightingType, text)


def serialize_ec2_query(
    value: BandwidthWeightingType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> BandwidthWeightingType:
    return from_ec2_query_text(el.text or "")
