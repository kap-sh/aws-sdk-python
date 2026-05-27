"""Generated from Smithy shape ``com.amazonaws.ec2#AuthorizationRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_vpn_authorization_rule_status
    import aws_sdk_ec2.types.string


class AuthorizationRule(TypedDict):
    client_vpn_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Client VPN endpoint with which the authorization rule is associated.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A brief description of the authorization rule.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Active Directory group to which the authorization rule grants access.</p>"""
    access_all: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the authorization rule grants access to all clients.</p>"""
    destination_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation, of the network to which the authorization rule applies.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_authorization_rule_status.ClientVpnAuthorizationRuleStatus"
    ]
    """<p>The current state of the authorization rule.</p>"""
