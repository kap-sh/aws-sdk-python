"""Generated from Smithy shape ``com.amazonaws.ec2#TransportProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

TransportProtocol: TypeAlias = Literal[
    "tcp",
    "udp",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "tcp",
        "udp",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "tcp",
        "udp",
    )
)


def to_ec2_query_text(value: TransportProtocol) -> str:
    return value


def from_ec2_query_text(text: str) -> TransportProtocol:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TransportProtocol value: {text!r}")
    return cast(TransportProtocol, text)


def serialize_ec2_query(
    value: TransportProtocol, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransportProtocol:
    return from_ec2_query_text(el.text or "")
