"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnAuthorizationRuleStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_authorization_rule_status_code
    import aws_sdk_ec2.types.string


class ClientVpnAuthorizationRuleStatus(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.client_vpn_authorization_rule_status_code.ClientVpnAuthorizationRuleStatusCode"
    ]
    """<p>The state of the authorization rule.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message about the status of the authorization rule, if applicable.</p>"""
