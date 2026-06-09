"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

VerifiedAccessEndpointProtocol: TypeAlias = Literal[
    "http",
    "https",
    "tcp",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "http",
        "https",
        "tcp",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "http",
        "https",
        "tcp",
    )
)


def to_ec2_query_text(value: VerifiedAccessEndpointProtocol) -> str:
    return value


def from_ec2_query_text(text: str) -> VerifiedAccessEndpointProtocol:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown VerifiedAccessEndpointProtocol value: {text!r}"
        )
    return cast(VerifiedAccessEndpointProtocol, text)


def serialize_ec2_query(
    value: VerifiedAccessEndpointProtocol, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VerifiedAccessEndpointProtocol:
    return from_ec2_query_text(el.text or "")
