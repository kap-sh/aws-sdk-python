"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayVirtualInterfaceGroupConfigurationState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

LocalGatewayVirtualInterfaceGroupConfigurationState: TypeAlias = Literal[
    "pending",
    "incomplete",
    "available",
    "deleting",
    "deleted",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(
    value: LocalGatewayVirtualInterfaceGroupConfigurationState,
) -> str:
    return value


def from_ec2_query_text(
    text: str,
) -> LocalGatewayVirtualInterfaceGroupConfigurationState:
    return cast(LocalGatewayVirtualInterfaceGroupConfigurationState, text)


def serialize_ec2_query(
    value: LocalGatewayVirtualInterfaceGroupConfigurationState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(
    el: Element,
) -> LocalGatewayVirtualInterfaceGroupConfigurationState:
    return from_ec2_query_text(el.text or "")
