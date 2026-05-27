"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointServiceConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list
    import aws_sdk_ec2.types.vpc_endpoint_service_id


class ModifyVpcEndpointServiceConfigurationRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    service_id: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_service_id.VpcEndpointServiceId"
    ]
    """<p>The ID of the service.</p>"""
    private_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>(Interface endpoint configuration) The private DNS name to assign to the endpoint service.</p>"""
    remove_private_dns_name: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>(Interface endpoint configuration) Removes the private DNS name of the endpoint service.</p>"""
    acceptance_required: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether requests to create an endpoint to the service must be accepted.</p>"""
    add_network_load_balancer_arns: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of Network Load Balancers to add to the service configuration.</p>"""
    remove_network_load_balancer_arns: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of Network Load Balancers to remove from the service configuration.</p>"""
    add_gateway_load_balancer_arns: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of Gateway Load Balancers to add to the service configuration.</p>"""
    remove_gateway_load_balancer_arns: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of Gateway Load Balancers to remove from the service configuration.</p>"""
    add_supported_ip_address_types: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IP address types to add to the service configuration.</p>"""
    remove_supported_ip_address_types: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IP address types to remove from the service configuration.</p>"""
    add_supported_regions: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The supported Regions to add to the service configuration.</p>"""
    remove_supported_regions: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The supported Regions to remove from the service configuration.</p>"""
