"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.dns_options_specification
    import aws_sdk_ec2.types.ip_address_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_configurations_list
    import aws_sdk_ec2.types.vpc_endpoint_id
    import aws_sdk_ec2.types.vpc_endpoint_route_table_id_list
    import aws_sdk_ec2.types.vpc_endpoint_security_group_id_list
    import aws_sdk_ec2.types.vpc_endpoint_subnet_id_list


class ModifyVpcEndpointRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    vpc_endpoint_id: NotRequired["aws_sdk_ec2.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The ID of the endpoint.</p>"""
    reset_policy: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>(Gateway endpoint) Specify <code>true</code> to reset the policy document to the default policy. The default policy allows full access to the service.</p>"""
    policy_document: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>(Interface and gateway endpoints) A policy to attach to the endpoint that controls access to the service. The policy must be in valid JSON format.</p>"""
    add_route_table_ids: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_route_table_id_list.VpcEndpointRouteTableIdList"
    ]
    """<p>(Gateway endpoint) The IDs of the route tables to associate with the endpoint.</p>"""
    remove_route_table_ids: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_route_table_id_list.VpcEndpointRouteTableIdList"
    ]
    """<p>(Gateway endpoint) The IDs of the route tables to disassociate from the endpoint.</p>"""
    add_subnet_ids: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_subnet_id_list.VpcEndpointSubnetIdList"
    ]
    """<p>(Interface and Gateway Load Balancer endpoints) The IDs of the subnets in which to serve the endpoint. For a Gateway Load Balancer endpoint, you can specify only one subnet.</p>"""
    remove_subnet_ids: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_subnet_id_list.VpcEndpointSubnetIdList"
    ]
    """<p>(Interface endpoint) The IDs of the subnets from which to remove the endpoint.</p>"""
    add_security_group_ids: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_security_group_id_list.VpcEndpointSecurityGroupIdList"
    ]
    """<p>(Interface endpoint) The IDs of the security groups to associate with the endpoint network interfaces.</p>"""
    remove_security_group_ids: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_security_group_id_list.VpcEndpointSecurityGroupIdList"
    ]
    """<p>(Interface endpoint) The IDs of the security groups to disassociate from the endpoint network interfaces.</p>"""
    ip_address_type: NotRequired["aws_sdk_ec2.types.ip_address_type.IpAddressType"]
    """<p>The IP address type for the endpoint.</p>"""
    dns_options: NotRequired[
        "aws_sdk_ec2.types.dns_options_specification.DnsOptionsSpecification"
    ]
    """<p>The DNS options for the endpoint.</p>"""
    private_dns_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>(Interface endpoint) Indicates whether a private hosted zone is associated with the VPC.</p>"""
    subnet_configurations: NotRequired[
        "aws_sdk_ec2.types.subnet_configurations_list.SubnetConfigurationsList"
    ]
    """<p>The subnet configurations for the endpoint.</p>"""
