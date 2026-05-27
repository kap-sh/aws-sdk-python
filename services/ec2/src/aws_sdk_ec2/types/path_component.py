"""Generated from Smithy shape ``com.amazonaws.ec2#PathComponent``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.additional_detail_list
    import aws_sdk_ec2.types.analysis_acl_rule
    import aws_sdk_ec2.types.analysis_component
    import aws_sdk_ec2.types.analysis_packet_header
    import aws_sdk_ec2.types.analysis_route_table_route
    import aws_sdk_ec2.types.analysis_security_group_rule
    import aws_sdk_ec2.types.explanation_list
    import aws_sdk_ec2.types.firewall_stateful_rule
    import aws_sdk_ec2.types.firewall_stateless_rule
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_route_table_route


class PathComponent(TypedDict):
    sequence_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The sequence number.</p>"""
    acl_rule: NotRequired["aws_sdk_ec2.types.analysis_acl_rule.AnalysisAclRule"]
    """<p>The network ACL rule.</p>"""
    attached_to: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The resource to which the path component is attached.</p>"""
    component: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The component.</p>"""
    destination_vpc: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The destination VPC.</p>"""
    outbound_header: NotRequired[
        "aws_sdk_ec2.types.analysis_packet_header.AnalysisPacketHeader"
    ]
    """<p>The outbound header.</p>"""
    inbound_header: NotRequired[
        "aws_sdk_ec2.types.analysis_packet_header.AnalysisPacketHeader"
    ]
    """<p>The inbound header.</p>"""
    route_table_route: NotRequired[
        "aws_sdk_ec2.types.analysis_route_table_route.AnalysisRouteTableRoute"
    ]
    """<p>The route table route.</p>"""
    security_group_rule: NotRequired[
        "aws_sdk_ec2.types.analysis_security_group_rule.AnalysisSecurityGroupRule"
    ]
    """<p>The security group rule.</p>"""
    source_vpc: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The source VPC.</p>"""
    subnet: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The subnet.</p>"""
    vpc: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The component VPC.</p>"""
    additional_details: NotRequired[
        "aws_sdk_ec2.types.additional_detail_list.AdditionalDetailList"
    ]
    """<p>The additional details.</p>"""
    transit_gateway: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The transit gateway.</p>"""
    transit_gateway_route_table_route: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_route.TransitGatewayRouteTableRoute"
    ]
    """<p>The route in a transit gateway route table.</p>"""
    explanations: NotRequired["aws_sdk_ec2.types.explanation_list.ExplanationList"]
    """<p>The explanation codes.</p>"""
    elastic_load_balancer_listener: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The load balancer listener.</p>"""
    firewall_stateless_rule: NotRequired[
        "aws_sdk_ec2.types.firewall_stateless_rule.FirewallStatelessRule"
    ]
    """<p>The Network Firewall stateless rule.</p>"""
    firewall_stateful_rule: NotRequired[
        "aws_sdk_ec2.types.firewall_stateful_rule.FirewallStatefulRule"
    ]
    """<p>The Network Firewall stateful rule.</p>"""
    service_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the VPC endpoint service.</p>"""
