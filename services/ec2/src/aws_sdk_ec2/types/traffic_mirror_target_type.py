"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorTargetType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

TrafficMirrorTargetType: TypeAlias = Literal[
    "network-interface",
    "network-load-balancer",
    "gateway-load-balancer-endpoint",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "network-interface",
        "network-load-balancer",
        "gateway-load-balancer-endpoint",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "network-interface",
        "network-load-balancer",
        "gateway-load-balancer-endpoint",
    )
)


def to_ec2_query_text(value: TrafficMirrorTargetType) -> str:
    return value


def from_ec2_query_text(text: str) -> TrafficMirrorTargetType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TrafficMirrorTargetType value: {text!r}")
    return cast(TrafficMirrorTargetType, text)


def serialize_ec2_query(
    value: TrafficMirrorTargetType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TrafficMirrorTargetType:
    return from_ec2_query_text(el.text or "")
