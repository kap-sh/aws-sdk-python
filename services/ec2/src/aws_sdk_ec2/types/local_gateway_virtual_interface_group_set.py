"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayVirtualInterfaceGroupSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group

LocalGatewayVirtualInterfaceGroupSet: TypeAlias = list[
    "aws_sdk_ec2.types.local_gateway_virtual_interface_group.LocalGatewayVirtualInterfaceGroup"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewayVirtualInterfaceGroupSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.local_gateway_virtual_interface_group

        aws_sdk_ec2.types.local_gateway_virtual_interface_group.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> LocalGatewayVirtualInterfaceGroupSet:
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group

    out: LocalGatewayVirtualInterfaceGroupSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.local_gateway_virtual_interface_group.deserialize_ec2_query(
                child
            )
        )
    return out
