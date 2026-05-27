"""Generated from Smithy shape ``com.amazonaws.ec2#ApplySecurityGroupsToClientVpnTargetNetworkResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_security_group_id_set


class ApplySecurityGroupsToClientVpnTargetNetworkResult(TypedDict):
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.client_vpn_security_group_id_set.ClientVpnSecurityGroupIdSet"
    ]
    """<p>The IDs of the applied security groups.</p>"""
