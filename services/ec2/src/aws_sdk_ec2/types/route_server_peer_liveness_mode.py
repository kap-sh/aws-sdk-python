"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPeerLivenessMode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

RouteServerPeerLivenessMode: TypeAlias = Literal[
    "bfd",
    "bgp-keepalive",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "bfd",
        "bgp-keepalive",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "bfd",
        "bgp-keepalive",
    )
)


def to_ec2_query_text(value: RouteServerPeerLivenessMode) -> str:
    return value


def from_ec2_query_text(text: str) -> RouteServerPeerLivenessMode:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown RouteServerPeerLivenessMode value: {text!r}"
        )
    return cast(RouteServerPeerLivenessMode, text)


def serialize_ec2_query(
    value: RouteServerPeerLivenessMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RouteServerPeerLivenessMode:
    return from_ec2_query_text(el.text or "")
