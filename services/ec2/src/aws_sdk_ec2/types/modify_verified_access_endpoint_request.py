"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.modify_verified_access_endpoint_cidr_options
    import aws_sdk_ec2.types.modify_verified_access_endpoint_eni_options
    import aws_sdk_ec2.types.modify_verified_access_endpoint_load_balancer_options
    import aws_sdk_ec2.types.modify_verified_access_endpoint_rds_options
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_endpoint_id
    import aws_sdk_ec2.types.verified_access_group_id


class ModifyVerifiedAccessEndpointRequest(TypedDict):
    verified_access_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_id.VerifiedAccessEndpointId"
    ]
    """<p>The ID of the Verified Access endpoint.</p>"""
    verified_access_group_id: NotRequired[
        "aws_sdk_ec2.types.verified_access_group_id.VerifiedAccessGroupId"
    ]
    """<p>The ID of the Verified Access group.</p>"""
    load_balancer_options: NotRequired[
        "aws_sdk_ec2.types.modify_verified_access_endpoint_load_balancer_options.ModifyVerifiedAccessEndpointLoadBalancerOptions"
    ]
    """<p>The load balancer details if creating the Verified Access endpoint as <code>load-balancer</code>type.</p>"""
    network_interface_options: NotRequired[
        "aws_sdk_ec2.types.modify_verified_access_endpoint_eni_options.ModifyVerifiedAccessEndpointEniOptions"
    ]
    """<p>The network interface options.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the Verified Access endpoint.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    rds_options: NotRequired[
        "aws_sdk_ec2.types.modify_verified_access_endpoint_rds_options.ModifyVerifiedAccessEndpointRdsOptions"
    ]
    """<p>The RDS options.</p>"""
    cidr_options: NotRequired[
        "aws_sdk_ec2.types.modify_verified_access_endpoint_cidr_options.ModifyVerifiedAccessEndpointCidrOptions"
    ]
    """<p>The CIDR options.</p>"""
