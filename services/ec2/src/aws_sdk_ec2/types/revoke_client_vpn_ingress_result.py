"""Generated from Smithy shape ``com.amazonaws.ec2#RevokeClientVpnIngressResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_authorization_rule_status


class RevokeClientVpnIngressResult(TypedDict):
    status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_authorization_rule_status.ClientVpnAuthorizationRuleStatus"
    ]
    """<p>The current state of the authorization rule.</p>"""
