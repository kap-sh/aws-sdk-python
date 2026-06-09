"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayVirtualInterfaceGroupIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group_id

LocalGatewayVirtualInterfaceGroupIdSet: TypeAlias = list[
    "aws_sdk_ec2.types.local_gateway_virtual_interface_group_id.LocalGatewayVirtualInterfaceGroupId"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewayVirtualInterfaceGroupIdSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(
    parent: Element, tag: str
) -> LocalGatewayVirtualInterfaceGroupIdSet:
    out: LocalGatewayVirtualInterfaceGroupIdSet = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
