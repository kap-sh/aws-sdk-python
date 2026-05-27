"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpnConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.customer_gateway_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.transit_gateway_id
    import aws_sdk_ec2.types.vpn_concentrator_id
    import aws_sdk_ec2.types.vpn_connection_options_specification
    import aws_sdk_ec2.types.vpn_gateway_id


class CreateVpnConnectionRequest(TypedDict):
    customer_gateway_id: NotRequired[
        "aws_sdk_ec2.types.customer_gateway_id.CustomerGatewayId"
    ]
    """<p>The ID of the customer gateway.</p>"""
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of VPN connection (<code>ipsec.1</code>).</p>"""
    vpn_gateway_id: NotRequired["aws_sdk_ec2.types.vpn_gateway_id.VpnGatewayId"]
    """<p>The ID of the virtual private gateway. If you specify a virtual private gateway, you cannot specify a transit gateway.</p>"""
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway. If you specify a transit gateway, you cannot specify a virtual private gateway.</p>"""
    vpn_concentrator_id: NotRequired[
        "aws_sdk_ec2.types.vpn_concentrator_id.VpnConcentratorId"
    ]
    """<p>The ID of the VPN concentrator to associate with the VPN connection.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the VPN connection.</p>"""
    pre_shared_key_storage: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Specifies the storage mode for the pre-shared key (PSK). Valid values are <code>Standard</code>\" (stored in the Site-to-Site VPN service) or <code>SecretsManager</code> (stored in Amazon Web Services Secrets Manager).</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_options_specification.VpnConnectionOptionsSpecification"
    ]
    """<p>The options for the VPN connection.</p>"""
