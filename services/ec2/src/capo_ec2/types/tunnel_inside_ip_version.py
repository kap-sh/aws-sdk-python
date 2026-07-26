"""Generated from Smithy shape ``com.amazonaws.ec2#TunnelInsideIpVersion``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TunnelInsideIpVersion: TypeAlias = Literal[
    "ipv4",
    "ipv6",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TunnelInsideIpVersion) -> str:
    return value


def from_ec2_query_text(text: str) -> TunnelInsideIpVersion:
    return cast(TunnelInsideIpVersion, text)


def serialize_ec2_query(
    value: TunnelInsideIpVersion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TunnelInsideIpVersion:
    return from_ec2_query_text(el.text or "")
