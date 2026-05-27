"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnEndpointIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_endpoint_id

ClientVpnEndpointIdList: TypeAlias = list[
    "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
]
