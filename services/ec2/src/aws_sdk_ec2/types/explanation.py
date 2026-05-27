"""Generated from Smithy shape ``com.amazonaws.ec2#Explanation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.analysis_acl_rule
    import aws_sdk_ec2.types.analysis_component
    import aws_sdk_ec2.types.analysis_component_list
    import aws_sdk_ec2.types.analysis_load_balancer_listener
    import aws_sdk_ec2.types.analysis_load_balancer_target
    import aws_sdk_ec2.types.analysis_route_table_route
    import aws_sdk_ec2.types.analysis_security_group_rule
    import aws_sdk_ec2.types.component_account
    import aws_sdk_ec2.types.component_region
    import aws_sdk_ec2.types.firewall_stateful_rule
    import aws_sdk_ec2.types.firewall_stateless_rule
    import aws_sdk_ec2.types.ip_address
    import aws_sdk_ec2.types.ip_address_list
    import aws_sdk_ec2.types.port
    import aws_sdk_ec2.types.port_range_list
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.string_list
    import aws_sdk_ec2.types.transit_gateway_route_table_route
    import aws_sdk_ec2.types.value_string_list


class Explanation(TypedDict):
    acl: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The network ACL.</p>"""
    acl_rule: NotRequired["aws_sdk_ec2.types.analysis_acl_rule.AnalysisAclRule"]
    """<p>The network ACL rule.</p>"""
    address: NotRequired["aws_sdk_ec2.types.ip_address.IpAddress"]
    """<p>The IPv4 address, in CIDR notation.</p>"""
    addresses: NotRequired["aws_sdk_ec2.types.ip_address_list.IpAddressList"]
    """<p>The IPv4 addresses, in CIDR notation.</p>"""
    attached_to: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The resource to which the component is attached.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Availability Zones.</p>"""
    availability_zone_ids: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IDs of the Availability Zones.</p>"""
    cidrs: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The CIDR ranges.</p>"""
    component: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The component.</p>"""
    customer_gateway: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The customer gateway.</p>"""
    destination: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The destination.</p>"""
    destination_vpc: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The destination VPC.</p>"""
    direction: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The direction. The following are the possible values:</p> <ul> <li> <p>egress</p> </li> <li> <p>ingress</p> </li> </ul>"""
    explanation_code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The explanation code.</p>"""
    ingress_route_table: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The route table.</p>"""
    internet_gateway: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The internet gateway.</p>"""
    load_balancer_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    classic_load_balancer_listener: NotRequired[
        "aws_sdk_ec2.types.analysis_load_balancer_listener.AnalysisLoadBalancerListener"
    ]
    """<p>The listener for a Classic Load Balancer.</p>"""
    load_balancer_listener_port: NotRequired["aws_sdk_ec2.types.port.Port"]
    """<p>The listener port of the load balancer.</p>"""
    load_balancer_target: NotRequired[
        "aws_sdk_ec2.types.analysis_load_balancer_target.AnalysisLoadBalancerTarget"
    ]
    """<p>The target.</p>"""
    load_balancer_target_group: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The target group.</p>"""
    load_balancer_target_groups: NotRequired[
        "aws_sdk_ec2.types.analysis_component_list.AnalysisComponentList"
    ]
    """<p>The target groups.</p>"""
    load_balancer_target_port: NotRequired["aws_sdk_ec2.types.port.Port"]
    """<p>The target port.</p>"""
    elastic_load_balancer_listener: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The load balancer listener.</p>"""
    missing_component: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The missing component.</p>"""
    nat_gateway: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The NAT gateway.</p>"""
    network_interface: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The network interface.</p>"""
    packet_field: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The packet field.</p>"""
    vpc_peering_connection: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The VPC peering connection.</p>"""
    port: NotRequired["aws_sdk_ec2.types.port.Port"]
    """<p>The port.</p>"""
    port_ranges: NotRequired["aws_sdk_ec2.types.port_range_list.PortRangeList"]
    """<p>The port ranges.</p>"""
    prefix_list: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The prefix list.</p>"""
    protocols: NotRequired["aws_sdk_ec2.types.string_list.StringList"]
    """<p>The protocols.</p>"""
    route_table_route: NotRequired[
        "aws_sdk_ec2.types.analysis_route_table_route.AnalysisRouteTableRoute"
    ]
    """<p>The route table route.</p>"""
    route_table: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The route table.</p>"""
    security_group: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The security group.</p>"""
    security_group_rule: NotRequired[
        "aws_sdk_ec2.types.analysis_security_group_rule.AnalysisSecurityGroupRule"
    ]
    """<p>The security group rule.</p>"""
    security_groups: NotRequired[
        "aws_sdk_ec2.types.analysis_component_list.AnalysisComponentList"
    ]
    """<p>The security groups.</p>"""
    source_vpc: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The source VPC.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The state.</p>"""
    subnet: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The subnet.</p>"""
    subnet_route_table: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The route table for the subnet.</p>"""
    vpc: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The component VPC.</p>"""
    vpc_endpoint: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The VPC endpoint.</p>"""
    vpn_connection: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The VPN connection.</p>"""
    vpn_gateway: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The VPN gateway.</p>"""
    transit_gateway: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The transit gateway.</p>"""
    transit_gateway_route_table: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The transit gateway route table.</p>"""
    transit_gateway_route_table_route: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_route.TransitGatewayRouteTableRoute"
    ]
    """<p>The transit gateway route table route.</p>"""
    transit_gateway_attachment: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The transit gateway attachment.</p>"""
    component_account: NotRequired[
        "aws_sdk_ec2.types.component_account.ComponentAccount"
    ]
    """<p>The Amazon Web Services account for the component.</p>"""
    component_region: NotRequired["aws_sdk_ec2.types.component_region.ComponentRegion"]
    """<p>The Region for the component.</p>"""
    firewall_stateless_rule: NotRequired[
        "aws_sdk_ec2.types.firewall_stateless_rule.FirewallStatelessRule"
    ]
    """<p>The Network Firewall stateless rule.</p>"""
    firewall_stateful_rule: NotRequired[
        "aws_sdk_ec2.types.firewall_stateful_rule.FirewallStatefulRule"
    ]
    """<p>The Network Firewall stateful rule.</p>"""
