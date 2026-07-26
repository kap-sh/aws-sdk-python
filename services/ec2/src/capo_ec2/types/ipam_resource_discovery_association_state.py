"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceDiscoveryAssociationState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

IpamResourceDiscoveryAssociationState: TypeAlias = Literal[
    "associate-in-progress",
    "associate-complete",
    "associate-failed",
    "disassociate-in-progress",
    "disassociate-complete",
    "disassociate-failed",
    "isolate-in-progress",
    "isolate-complete",
    "restore-in-progress",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamResourceDiscoveryAssociationState) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamResourceDiscoveryAssociationState:
    return cast(IpamResourceDiscoveryAssociationState, text)


def serialize_ec2_query(
    value: IpamResourceDiscoveryAssociationState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamResourceDiscoveryAssociationState:
    return from_ec2_query_text(el.text or "")
