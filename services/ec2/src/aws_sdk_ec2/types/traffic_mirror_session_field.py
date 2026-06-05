"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorSessionField``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

TrafficMirrorSessionField: TypeAlias = Literal[
    "packet-length",
    "description",
    "virtual-network-id",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "packet-length",
        "description",
        "virtual-network-id",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "packet-length",
        "description",
        "virtual-network-id",
    )
)


def to_ec2_query_text(value: TrafficMirrorSessionField) -> str:
    return value


def from_ec2_query_text(text: str) -> TrafficMirrorSessionField:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TrafficMirrorSessionField value: {text!r}")
    return cast(TrafficMirrorSessionField, text)


def serialize_ec2_query(
    value: TrafficMirrorSessionField, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TrafficMirrorSessionField:
    return from_ec2_query_text(el.text or "")
