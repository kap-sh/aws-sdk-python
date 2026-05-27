"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceLinkVirtualInterfaceSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_link_virtual_interface

ServiceLinkVirtualInterfaceSet: TypeAlias = list[
    "aws_sdk_ec2.types.service_link_virtual_interface.ServiceLinkVirtualInterface"
]
