"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIpv6AddressListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_ipv6_address_request

InstanceIpv6AddressListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.instance_ipv6_address_request.InstanceIpv6AddressRequest"
]
