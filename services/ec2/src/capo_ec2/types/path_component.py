"""Generated from Smithy shape ``com.amazonaws.ec2#PathComponent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.additional_detail_list
    import capo_ec2.types.analysis_acl_rule
    import capo_ec2.types.analysis_component
    import capo_ec2.types.analysis_packet_header
    import capo_ec2.types.analysis_route_table_route
    import capo_ec2.types.analysis_security_group_rule
    import capo_ec2.types.explanation_list
    import capo_ec2.types.firewall_stateful_rule
    import capo_ec2.types.firewall_stateless_rule
    import capo_ec2.types.integer
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_route_table_route


class PathComponent(TypedDict, closed=True):
    sequence_number: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The sequence number.</p>"""
    acl_rule: NotRequired["capo_ec2.types.analysis_acl_rule.AnalysisAclRule"]
    """<p>The network ACL rule.</p>"""
    attached_to: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The resource to which the path component is attached.</p>"""
    component: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The component.</p>"""
    destination_vpc: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The destination VPC.</p>"""
    outbound_header: NotRequired[
        "capo_ec2.types.analysis_packet_header.AnalysisPacketHeader"
    ]
    """<p>The outbound header.</p>"""
    inbound_header: NotRequired[
        "capo_ec2.types.analysis_packet_header.AnalysisPacketHeader"
    ]
    """<p>The inbound header.</p>"""
    route_table_route: NotRequired[
        "capo_ec2.types.analysis_route_table_route.AnalysisRouteTableRoute"
    ]
    """<p>The route table route.</p>"""
    security_group_rule: NotRequired[
        "capo_ec2.types.analysis_security_group_rule.AnalysisSecurityGroupRule"
    ]
    """<p>The security group rule.</p>"""
    source_vpc: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The source VPC.</p>"""
    subnet: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The subnet.</p>"""
    vpc: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The component VPC.</p>"""
    additional_details: NotRequired[
        "capo_ec2.types.additional_detail_list.AdditionalDetailList"
    ]
    """<p>The additional details.</p>"""
    transit_gateway: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The transit gateway.</p>"""
    transit_gateway_route_table_route: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_route.TransitGatewayRouteTableRoute"
    ]
    """<p>The route in a transit gateway route table.</p>"""
    explanations: NotRequired["capo_ec2.types.explanation_list.ExplanationList"]
    """<p>The explanation codes.</p>"""
    elastic_load_balancer_listener: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The load balancer listener.</p>"""
    firewall_stateless_rule: NotRequired[
        "capo_ec2.types.firewall_stateless_rule.FirewallStatelessRule"
    ]
    """<p>The Network Firewall stateless rule.</p>"""
    firewall_stateful_rule: NotRequired[
        "capo_ec2.types.firewall_stateful_rule.FirewallStatefulRule"
    ]
    """<p>The Network Firewall stateful rule.</p>"""
    service_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the VPC endpoint service.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PathComponent, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "sequence_number" in value:
        pairs.append((f"{prefix}.SequenceNumber", str(value["sequence_number"])))
    if "acl_rule" in value:
        import capo_ec2.types.analysis_acl_rule

        capo_ec2.types.analysis_acl_rule.serialize_ec2_query(
            value["acl_rule"], pairs, f"{prefix}.AclRule"
        )
    if "attached_to" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["attached_to"], pairs, f"{prefix}.AttachedTo"
        )
    if "component" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["component"], pairs, f"{prefix}.Component"
        )
    if "destination_vpc" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["destination_vpc"], pairs, f"{prefix}.DestinationVpc"
        )
    if "outbound_header" in value:
        import capo_ec2.types.analysis_packet_header

        capo_ec2.types.analysis_packet_header.serialize_ec2_query(
            value["outbound_header"], pairs, f"{prefix}.OutboundHeader"
        )
    if "inbound_header" in value:
        import capo_ec2.types.analysis_packet_header

        capo_ec2.types.analysis_packet_header.serialize_ec2_query(
            value["inbound_header"], pairs, f"{prefix}.InboundHeader"
        )
    if "route_table_route" in value:
        import capo_ec2.types.analysis_route_table_route

        capo_ec2.types.analysis_route_table_route.serialize_ec2_query(
            value["route_table_route"], pairs, f"{prefix}.RouteTableRoute"
        )
    if "security_group_rule" in value:
        import capo_ec2.types.analysis_security_group_rule

        capo_ec2.types.analysis_security_group_rule.serialize_ec2_query(
            value["security_group_rule"], pairs, f"{prefix}.SecurityGroupRule"
        )
    if "source_vpc" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["source_vpc"], pairs, f"{prefix}.SourceVpc"
        )
    if "subnet" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["subnet"], pairs, f"{prefix}.Subnet"
        )
    if "vpc" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["vpc"], pairs, f"{prefix}.Vpc"
        )
    if "additional_details" in value:
        import capo_ec2.types.additional_detail_list

        capo_ec2.types.additional_detail_list.serialize_ec2_query(
            value["additional_details"], pairs, f"{prefix}.AdditionalDetailSet"
        )
    if "transit_gateway" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["transit_gateway"], pairs, f"{prefix}.TransitGateway"
        )
    if "transit_gateway_route_table_route" in value:
        import capo_ec2.types.transit_gateway_route_table_route

        capo_ec2.types.transit_gateway_route_table_route.serialize_ec2_query(
            value["transit_gateway_route_table_route"],
            pairs,
            f"{prefix}.TransitGatewayRouteTableRoute",
        )
    if "explanations" in value:
        import capo_ec2.types.explanation_list

        capo_ec2.types.explanation_list.serialize_ec2_query(
            value["explanations"], pairs, f"{prefix}.ExplanationSet"
        )
    if "elastic_load_balancer_listener" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["elastic_load_balancer_listener"],
            pairs,
            f"{prefix}.ElasticLoadBalancerListener",
        )
    if "firewall_stateless_rule" in value:
        import capo_ec2.types.firewall_stateless_rule

        capo_ec2.types.firewall_stateless_rule.serialize_ec2_query(
            value["firewall_stateless_rule"], pairs, f"{prefix}.FirewallStatelessRule"
        )
    if "firewall_stateful_rule" in value:
        import capo_ec2.types.firewall_stateful_rule

        capo_ec2.types.firewall_stateful_rule.serialize_ec2_query(
            value["firewall_stateful_rule"], pairs, f"{prefix}.FirewallStatefulRule"
        )
    if "service_name" in value:
        pairs.append((f"{prefix}.ServiceName", str(value["service_name"])))


def deserialize_ec2_query(el: Element) -> PathComponent:
    out: PathComponent = {}  # type: ignore[typeddict-item]
    child_sequence_number = el.find("SequenceNumber")
    if child_sequence_number is not None:
        out["sequence_number"] = int(child_sequence_number.text or "")
    child_acl_rule = el.find("AclRule")
    if child_acl_rule is not None:
        import capo_ec2.types.analysis_acl_rule

        out["acl_rule"] = capo_ec2.types.analysis_acl_rule.deserialize_ec2_query(
            child_acl_rule
        )
    child_attached_to = el.find("AttachedTo")
    if child_attached_to is not None:
        import capo_ec2.types.analysis_component

        out["attached_to"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_attached_to
        )
    child_component = el.find("Component")
    if child_component is not None:
        import capo_ec2.types.analysis_component

        out["component"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_component
        )
    child_destination_vpc = el.find("DestinationVpc")
    if child_destination_vpc is not None:
        import capo_ec2.types.analysis_component

        out["destination_vpc"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_destination_vpc
            )
        )
    child_outbound_header = el.find("OutboundHeader")
    if child_outbound_header is not None:
        import capo_ec2.types.analysis_packet_header

        out["outbound_header"] = (
            capo_ec2.types.analysis_packet_header.deserialize_ec2_query(
                child_outbound_header
            )
        )
    child_inbound_header = el.find("InboundHeader")
    if child_inbound_header is not None:
        import capo_ec2.types.analysis_packet_header

        out["inbound_header"] = (
            capo_ec2.types.analysis_packet_header.deserialize_ec2_query(
                child_inbound_header
            )
        )
    child_route_table_route = el.find("RouteTableRoute")
    if child_route_table_route is not None:
        import capo_ec2.types.analysis_route_table_route

        out["route_table_route"] = (
            capo_ec2.types.analysis_route_table_route.deserialize_ec2_query(
                child_route_table_route
            )
        )
    child_security_group_rule = el.find("SecurityGroupRule")
    if child_security_group_rule is not None:
        import capo_ec2.types.analysis_security_group_rule

        out["security_group_rule"] = (
            capo_ec2.types.analysis_security_group_rule.deserialize_ec2_query(
                child_security_group_rule
            )
        )
    child_source_vpc = el.find("SourceVpc")
    if child_source_vpc is not None:
        import capo_ec2.types.analysis_component

        out["source_vpc"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_source_vpc
        )
    child_subnet = el.find("Subnet")
    if child_subnet is not None:
        import capo_ec2.types.analysis_component

        out["subnet"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_subnet
        )
    child_vpc = el.find("Vpc")
    if child_vpc is not None:
        import capo_ec2.types.analysis_component

        out["vpc"] = capo_ec2.types.analysis_component.deserialize_ec2_query(child_vpc)
    if el.find("AdditionalDetailSet") is not None:
        import capo_ec2.types.additional_detail_list

        out["additional_details"] = (
            capo_ec2.types.additional_detail_list.deserialize_ec2_query(
                el, "AdditionalDetailSet"
            )
        )
    child_transit_gateway = el.find("TransitGateway")
    if child_transit_gateway is not None:
        import capo_ec2.types.analysis_component

        out["transit_gateway"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_transit_gateway
            )
        )
    child_transit_gateway_route_table_route = el.find("TransitGatewayRouteTableRoute")
    if child_transit_gateway_route_table_route is not None:
        import capo_ec2.types.transit_gateway_route_table_route

        out["transit_gateway_route_table_route"] = (
            capo_ec2.types.transit_gateway_route_table_route.deserialize_ec2_query(
                child_transit_gateway_route_table_route
            )
        )
    if el.find("ExplanationSet") is not None:
        import capo_ec2.types.explanation_list

        out["explanations"] = capo_ec2.types.explanation_list.deserialize_ec2_query(
            el, "ExplanationSet"
        )
    child_elastic_load_balancer_listener = el.find("ElasticLoadBalancerListener")
    if child_elastic_load_balancer_listener is not None:
        import capo_ec2.types.analysis_component

        out["elastic_load_balancer_listener"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_elastic_load_balancer_listener
            )
        )
    child_firewall_stateless_rule = el.find("FirewallStatelessRule")
    if child_firewall_stateless_rule is not None:
        import capo_ec2.types.firewall_stateless_rule

        out["firewall_stateless_rule"] = (
            capo_ec2.types.firewall_stateless_rule.deserialize_ec2_query(
                child_firewall_stateless_rule
            )
        )
    child_firewall_stateful_rule = el.find("FirewallStatefulRule")
    if child_firewall_stateful_rule is not None:
        import capo_ec2.types.firewall_stateful_rule

        out["firewall_stateful_rule"] = (
            capo_ec2.types.firewall_stateful_rule.deserialize_ec2_query(
                child_firewall_stateful_rule
            )
        )
    child_service_name = el.find("ServiceName")
    if child_service_name is not None:
        out["service_name"] = str(child_service_name.text or "")
    return out
