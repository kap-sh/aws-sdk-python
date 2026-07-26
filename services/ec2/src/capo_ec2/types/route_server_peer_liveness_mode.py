"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPeerLivenessMode``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

RouteServerPeerLivenessMode: TypeAlias = Literal[
    "bfd",
    "bgp-keepalive",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: RouteServerPeerLivenessMode) -> str:
    return value


def from_ec2_query_text(text: str) -> RouteServerPeerLivenessMode:
    return cast(RouteServerPeerLivenessMode, text)


def serialize_ec2_query(
    value: RouteServerPeerLivenessMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RouteServerPeerLivenessMode:
    return from_ec2_query_text(el.text or "")
