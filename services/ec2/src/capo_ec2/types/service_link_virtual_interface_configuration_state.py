"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceLinkVirtualInterfaceConfigurationState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ServiceLinkVirtualInterfaceConfigurationState: TypeAlias = Literal[
    "pending",
    "available",
    "deleting",
    "deleted",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ServiceLinkVirtualInterfaceConfigurationState) -> str:
    return value


def from_ec2_query_text(text: str) -> ServiceLinkVirtualInterfaceConfigurationState:
    return cast(ServiceLinkVirtualInterfaceConfigurationState, text)


def serialize_ec2_query(
    value: ServiceLinkVirtualInterfaceConfigurationState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ServiceLinkVirtualInterfaceConfigurationState:
    return from_ec2_query_text(el.text or "")
