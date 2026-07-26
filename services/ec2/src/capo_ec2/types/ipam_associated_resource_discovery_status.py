"""Generated from Smithy shape ``com.amazonaws.ec2#IpamAssociatedResourceDiscoveryStatus``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

IpamAssociatedResourceDiscoveryStatus: TypeAlias = Literal[
    "active",
    "not-found",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamAssociatedResourceDiscoveryStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamAssociatedResourceDiscoveryStatus:
    return cast(IpamAssociatedResourceDiscoveryStatus, text)


def serialize_ec2_query(
    value: IpamAssociatedResourceDiscoveryStatus,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamAssociatedResourceDiscoveryStatus:
    return from_ec2_query_text(el.text or "")
