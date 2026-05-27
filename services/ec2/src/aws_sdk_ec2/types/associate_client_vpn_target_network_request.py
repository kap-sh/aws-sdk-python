"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateClientVpnTargetNetworkRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_name
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_vpn_endpoint_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id


class AssociateClientVpnTargetNetworkRequest(TypedDict):
    client_vpn_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet to associate with the Client VPN endpoint. Required for VPC-based endpoints. For Transit Gateway-based endpoints, use <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> instead.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone name for the Transit Gateway association. Required if when associating an Availability Zone with a Client VPN endpoint that uses a Transit Gateway. You cannot specify both <code>SubnetId</code> and <code>AvailabilityZone</code>.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The Availability Zone ID for the Transit Gateway association. Required if when associating an Availability Zone with a Client VPN endpoint that uses a Transit Gateway. You cannot specify both <code>AvailabilityZone</code> and <code>AvailabilityZoneId</code>.</p>"""
