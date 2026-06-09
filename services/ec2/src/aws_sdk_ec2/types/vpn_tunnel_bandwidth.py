"""Generated from Smithy shape ``com.amazonaws.ec2#VpnTunnelBandwidth``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

VpnTunnelBandwidth: TypeAlias = Literal[
    "standard",
    "large",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "large",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "large",
    )
)


def to_ec2_query_text(value: VpnTunnelBandwidth) -> str:
    return value


def from_ec2_query_text(text: str) -> VpnTunnelBandwidth:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VpnTunnelBandwidth value: {text!r}")
    return cast(VpnTunnelBandwidth, text)


def serialize_ec2_query(
    value: VpnTunnelBandwidth, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpnTunnelBandwidth:
    return from_ec2_query_text(el.text or "")
