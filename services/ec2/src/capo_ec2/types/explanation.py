"""Generated from Smithy shape ``com.amazonaws.ec2#Explanation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.analysis_acl_rule
    import capo_ec2.types.analysis_component
    import capo_ec2.types.analysis_component_list
    import capo_ec2.types.analysis_load_balancer_listener
    import capo_ec2.types.analysis_load_balancer_target
    import capo_ec2.types.analysis_route_table_route
    import capo_ec2.types.analysis_security_group_rule
    import capo_ec2.types.component_account
    import capo_ec2.types.component_region
    import capo_ec2.types.firewall_stateful_rule
    import capo_ec2.types.firewall_stateless_rule
    import capo_ec2.types.ip_address
    import capo_ec2.types.ip_address_list
    import capo_ec2.types.port
    import capo_ec2.types.port_range_list
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.string_list
    import capo_ec2.types.transit_gateway_route_table_route
    import capo_ec2.types.value_string_list


class Explanation(TypedDict, closed=True):
    acl: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The network ACL.</p>"""
    acl_rule: NotRequired["capo_ec2.types.analysis_acl_rule.AnalysisAclRule"]
    """<p>The network ACL rule.</p>"""
    address: NotRequired["capo_ec2.types.ip_address.IpAddress"]
    """<p>The IPv4 address, in CIDR notation.</p>"""
    addresses: NotRequired["capo_ec2.types.ip_address_list.IpAddressList"]
    """<p>The IPv4 addresses, in CIDR notation.</p>"""
    attached_to: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The resource to which the component is attached.</p>"""
    availability_zones: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The Availability Zones.</p>"""
    availability_zone_ids: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IDs of the Availability Zones.</p>"""
    cidrs: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The CIDR ranges.</p>"""
    component: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The component.</p>"""
    customer_gateway: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The customer gateway.</p>"""
    destination: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The destination.</p>"""
    destination_vpc: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The destination VPC.</p>"""
    direction: NotRequired["capo_ec2.types.string.String"]
    """<p>The direction. The following are the possible values:</p> <ul> <li> <p>egress</p> </li> <li> <p>ingress</p> </li> </ul>"""
    explanation_code: NotRequired["capo_ec2.types.string.String"]
    """<p>The explanation code.</p>"""
    ingress_route_table: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The route table.</p>"""
    internet_gateway: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The internet gateway.</p>"""
    load_balancer_arn: NotRequired["capo_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    classic_load_balancer_listener: NotRequired[
        "capo_ec2.types.analysis_load_balancer_listener.AnalysisLoadBalancerListener"
    ]
    """<p>The listener for a Classic Load Balancer.</p>"""
    load_balancer_listener_port: NotRequired["capo_ec2.types.port.Port"]
    """<p>The listener port of the load balancer.</p>"""
    load_balancer_target: NotRequired[
        "capo_ec2.types.analysis_load_balancer_target.AnalysisLoadBalancerTarget"
    ]
    """<p>The target.</p>"""
    load_balancer_target_group: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The target group.</p>"""
    load_balancer_target_groups: NotRequired[
        "capo_ec2.types.analysis_component_list.AnalysisComponentList"
    ]
    """<p>The target groups.</p>"""
    load_balancer_target_port: NotRequired["capo_ec2.types.port.Port"]
    """<p>The target port.</p>"""
    elastic_load_balancer_listener: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The load balancer listener.</p>"""
    missing_component: NotRequired["capo_ec2.types.string.String"]
    """<p>The missing component.</p>"""
    nat_gateway: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The NAT gateway.</p>"""
    network_interface: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The network interface.</p>"""
    packet_field: NotRequired["capo_ec2.types.string.String"]
    """<p>The packet field.</p>"""
    vpc_peering_connection: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The VPC peering connection.</p>"""
    port: NotRequired["capo_ec2.types.port.Port"]
    """<p>The port.</p>"""
    port_ranges: NotRequired["capo_ec2.types.port_range_list.PortRangeList"]
    """<p>The port ranges.</p>"""
    prefix_list: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The prefix list.</p>"""
    protocols: NotRequired["capo_ec2.types.string_list.StringList"]
    """<p>The protocols.</p>"""
    route_table_route: NotRequired[
        "capo_ec2.types.analysis_route_table_route.AnalysisRouteTableRoute"
    ]
    """<p>The route table route.</p>"""
    route_table: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The route table.</p>"""
    security_group: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The security group.</p>"""
    security_group_rule: NotRequired[
        "capo_ec2.types.analysis_security_group_rule.AnalysisSecurityGroupRule"
    ]
    """<p>The security group rule.</p>"""
    security_groups: NotRequired[
        "capo_ec2.types.analysis_component_list.AnalysisComponentList"
    ]
    """<p>The security groups.</p>"""
    source_vpc: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The source VPC.</p>"""
    state: NotRequired["capo_ec2.types.string.String"]
    """<p>The state.</p>"""
    subnet: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The subnet.</p>"""
    subnet_route_table: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The route table for the subnet.</p>"""
    vpc: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The component VPC.</p>"""
    vpc_endpoint: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The VPC endpoint.</p>"""
    vpn_connection: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The VPN connection.</p>"""
    vpn_gateway: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The VPN gateway.</p>"""
    transit_gateway: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The transit gateway.</p>"""
    transit_gateway_route_table: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The transit gateway route table.</p>"""
    transit_gateway_route_table_route: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_route.TransitGatewayRouteTableRoute"
    ]
    """<p>The transit gateway route table route.</p>"""
    transit_gateway_attachment: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The transit gateway attachment.</p>"""
    component_account: NotRequired["capo_ec2.types.component_account.ComponentAccount"]
    """<p>The Amazon Web Services account for the component.</p>"""
    component_region: NotRequired["capo_ec2.types.component_region.ComponentRegion"]
    """<p>The Region for the component.</p>"""
    firewall_stateless_rule: NotRequired[
        "capo_ec2.types.firewall_stateless_rule.FirewallStatelessRule"
    ]
    """<p>The Network Firewall stateless rule.</p>"""
    firewall_stateful_rule: NotRequired[
        "capo_ec2.types.firewall_stateful_rule.FirewallStatefulRule"
    ]
    """<p>The Network Firewall stateful rule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Explanation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "acl" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["acl"], pairs, f"{prefix}.Acl"
        )
    if "acl_rule" in value:
        import capo_ec2.types.analysis_acl_rule

        capo_ec2.types.analysis_acl_rule.serialize_ec2_query(
            value["acl_rule"], pairs, f"{prefix}.AclRule"
        )
    if "address" in value:
        pairs.append((f"{prefix}.Address", str(value["address"])))
    if "addresses" in value:
        import capo_ec2.types.ip_address_list

        capo_ec2.types.ip_address_list.serialize_ec2_query(
            value["addresses"], pairs, f"{prefix}.AddressSet"
        )
    if "attached_to" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["attached_to"], pairs, f"{prefix}.AttachedTo"
        )
    if "availability_zones" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["availability_zones"], pairs, f"{prefix}.AvailabilityZoneSet"
        )
    if "availability_zone_ids" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["availability_zone_ids"], pairs, f"{prefix}.AvailabilityZoneIdSet"
        )
    if "cidrs" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["cidrs"], pairs, f"{prefix}.CidrSet"
        )
    if "component" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["component"], pairs, f"{prefix}.Component"
        )
    if "customer_gateway" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["customer_gateway"], pairs, f"{prefix}.CustomerGateway"
        )
    if "destination" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["destination"], pairs, f"{prefix}.Destination"
        )
    if "destination_vpc" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["destination_vpc"], pairs, f"{prefix}.DestinationVpc"
        )
    if "direction" in value:
        pairs.append((f"{prefix}.Direction", str(value["direction"])))
    if "explanation_code" in value:
        pairs.append((f"{prefix}.ExplanationCode", str(value["explanation_code"])))
    if "ingress_route_table" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["ingress_route_table"], pairs, f"{prefix}.IngressRouteTable"
        )
    if "internet_gateway" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["internet_gateway"], pairs, f"{prefix}.InternetGateway"
        )
    if "load_balancer_arn" in value:
        pairs.append((f"{prefix}.LoadBalancerArn", str(value["load_balancer_arn"])))
    if "classic_load_balancer_listener" in value:
        import capo_ec2.types.analysis_load_balancer_listener

        capo_ec2.types.analysis_load_balancer_listener.serialize_ec2_query(
            value["classic_load_balancer_listener"],
            pairs,
            f"{prefix}.ClassicLoadBalancerListener",
        )
    if "load_balancer_listener_port" in value:
        pairs.append(
            (
                f"{prefix}.LoadBalancerListenerPort",
                str(value["load_balancer_listener_port"]),
            )
        )
    if "load_balancer_target" in value:
        import capo_ec2.types.analysis_load_balancer_target

        capo_ec2.types.analysis_load_balancer_target.serialize_ec2_query(
            value["load_balancer_target"], pairs, f"{prefix}.LoadBalancerTarget"
        )
    if "load_balancer_target_group" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["load_balancer_target_group"],
            pairs,
            f"{prefix}.LoadBalancerTargetGroup",
        )
    if "load_balancer_target_groups" in value:
        import capo_ec2.types.analysis_component_list

        capo_ec2.types.analysis_component_list.serialize_ec2_query(
            value["load_balancer_target_groups"],
            pairs,
            f"{prefix}.LoadBalancerTargetGroupSet",
        )
    if "load_balancer_target_port" in value:
        pairs.append(
            (
                f"{prefix}.LoadBalancerTargetPort",
                str(value["load_balancer_target_port"]),
            )
        )
    if "elastic_load_balancer_listener" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["elastic_load_balancer_listener"],
            pairs,
            f"{prefix}.ElasticLoadBalancerListener",
        )
    if "missing_component" in value:
        pairs.append((f"{prefix}.MissingComponent", str(value["missing_component"])))
    if "nat_gateway" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["nat_gateway"], pairs, f"{prefix}.NatGateway"
        )
    if "network_interface" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["network_interface"], pairs, f"{prefix}.NetworkInterface"
        )
    if "packet_field" in value:
        pairs.append((f"{prefix}.PacketField", str(value["packet_field"])))
    if "vpc_peering_connection" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["vpc_peering_connection"], pairs, f"{prefix}.VpcPeeringConnection"
        )
    if "port" in value:
        pairs.append((f"{prefix}.Port", str(value["port"])))
    if "port_ranges" in value:
        import capo_ec2.types.port_range_list

        capo_ec2.types.port_range_list.serialize_ec2_query(
            value["port_ranges"], pairs, f"{prefix}.PortRangeSet"
        )
    if "prefix_list" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["prefix_list"], pairs, f"{prefix}.PrefixList"
        )
    if "protocols" in value:
        import capo_ec2.types.string_list

        capo_ec2.types.string_list.serialize_ec2_query(
            value["protocols"], pairs, f"{prefix}.ProtocolSet"
        )
    if "route_table_route" in value:
        import capo_ec2.types.analysis_route_table_route

        capo_ec2.types.analysis_route_table_route.serialize_ec2_query(
            value["route_table_route"], pairs, f"{prefix}.RouteTableRoute"
        )
    if "route_table" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["route_table"], pairs, f"{prefix}.RouteTable"
        )
    if "security_group" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["security_group"], pairs, f"{prefix}.SecurityGroup"
        )
    if "security_group_rule" in value:
        import capo_ec2.types.analysis_security_group_rule

        capo_ec2.types.analysis_security_group_rule.serialize_ec2_query(
            value["security_group_rule"], pairs, f"{prefix}.SecurityGroupRule"
        )
    if "security_groups" in value:
        import capo_ec2.types.analysis_component_list

        capo_ec2.types.analysis_component_list.serialize_ec2_query(
            value["security_groups"], pairs, f"{prefix}.SecurityGroupSet"
        )
    if "source_vpc" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["source_vpc"], pairs, f"{prefix}.SourceVpc"
        )
    if "state" in value:
        pairs.append((f"{prefix}.State", str(value["state"])))
    if "subnet" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["subnet"], pairs, f"{prefix}.Subnet"
        )
    if "subnet_route_table" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["subnet_route_table"], pairs, f"{prefix}.SubnetRouteTable"
        )
    if "vpc" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["vpc"], pairs, f"{prefix}.Vpc"
        )
    if "vpc_endpoint" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["vpc_endpoint"], pairs, f"{prefix}.VpcEndpoint"
        )
    if "vpn_connection" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["vpn_connection"], pairs, f"{prefix}.VpnConnection"
        )
    if "vpn_gateway" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["vpn_gateway"], pairs, f"{prefix}.VpnGateway"
        )
    if "transit_gateway" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["transit_gateway"], pairs, f"{prefix}.TransitGateway"
        )
    if "transit_gateway_route_table" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["transit_gateway_route_table"],
            pairs,
            f"{prefix}.TransitGatewayRouteTable",
        )
    if "transit_gateway_route_table_route" in value:
        import capo_ec2.types.transit_gateway_route_table_route

        capo_ec2.types.transit_gateway_route_table_route.serialize_ec2_query(
            value["transit_gateway_route_table_route"],
            pairs,
            f"{prefix}.TransitGatewayRouteTableRoute",
        )
    if "transit_gateway_attachment" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["transit_gateway_attachment"],
            pairs,
            f"{prefix}.TransitGatewayAttachment",
        )
    if "component_account" in value:
        pairs.append((f"{prefix}.ComponentAccount", str(value["component_account"])))
    if "component_region" in value:
        pairs.append((f"{prefix}.ComponentRegion", str(value["component_region"])))
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


def deserialize_ec2_query(el: Element) -> Explanation:
    out: Explanation = {}  # type: ignore[typeddict-item]
    child_acl = el.find("Acl")
    if child_acl is not None:
        import capo_ec2.types.analysis_component

        out["acl"] = capo_ec2.types.analysis_component.deserialize_ec2_query(child_acl)
    child_acl_rule = el.find("AclRule")
    if child_acl_rule is not None:
        import capo_ec2.types.analysis_acl_rule

        out["acl_rule"] = capo_ec2.types.analysis_acl_rule.deserialize_ec2_query(
            child_acl_rule
        )
    child_address = el.find("Address")
    if child_address is not None:
        out["address"] = str(child_address.text or "")
    if el.find("AddressSet") is not None:
        import capo_ec2.types.ip_address_list

        out["addresses"] = capo_ec2.types.ip_address_list.deserialize_ec2_query(
            el, "AddressSet"
        )
    child_attached_to = el.find("AttachedTo")
    if child_attached_to is not None:
        import capo_ec2.types.analysis_component

        out["attached_to"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_attached_to
        )
    if el.find("AvailabilityZoneSet") is not None:
        import capo_ec2.types.value_string_list

        out["availability_zones"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "AvailabilityZoneSet"
            )
        )
    if el.find("AvailabilityZoneIdSet") is not None:
        import capo_ec2.types.value_string_list

        out["availability_zone_ids"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "AvailabilityZoneIdSet"
            )
        )
    if el.find("CidrSet") is not None:
        import capo_ec2.types.value_string_list

        out["cidrs"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "CidrSet"
        )
    child_component = el.find("Component")
    if child_component is not None:
        import capo_ec2.types.analysis_component

        out["component"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_component
        )
    child_customer_gateway = el.find("CustomerGateway")
    if child_customer_gateway is not None:
        import capo_ec2.types.analysis_component

        out["customer_gateway"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_customer_gateway
            )
        )
    child_destination = el.find("Destination")
    if child_destination is not None:
        import capo_ec2.types.analysis_component

        out["destination"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_destination
        )
    child_destination_vpc = el.find("DestinationVpc")
    if child_destination_vpc is not None:
        import capo_ec2.types.analysis_component

        out["destination_vpc"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_destination_vpc
            )
        )
    child_direction = el.find("Direction")
    if child_direction is not None:
        out["direction"] = str(child_direction.text or "")
    child_explanation_code = el.find("ExplanationCode")
    if child_explanation_code is not None:
        out["explanation_code"] = str(child_explanation_code.text or "")
    child_ingress_route_table = el.find("IngressRouteTable")
    if child_ingress_route_table is not None:
        import capo_ec2.types.analysis_component

        out["ingress_route_table"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_ingress_route_table
            )
        )
    child_internet_gateway = el.find("InternetGateway")
    if child_internet_gateway is not None:
        import capo_ec2.types.analysis_component

        out["internet_gateway"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_internet_gateway
            )
        )
    child_load_balancer_arn = el.find("LoadBalancerArn")
    if child_load_balancer_arn is not None:
        out["load_balancer_arn"] = str(child_load_balancer_arn.text or "")
    child_classic_load_balancer_listener = el.find("ClassicLoadBalancerListener")
    if child_classic_load_balancer_listener is not None:
        import capo_ec2.types.analysis_load_balancer_listener

        out["classic_load_balancer_listener"] = (
            capo_ec2.types.analysis_load_balancer_listener.deserialize_ec2_query(
                child_classic_load_balancer_listener
            )
        )
    child_load_balancer_listener_port = el.find("LoadBalancerListenerPort")
    if child_load_balancer_listener_port is not None:
        out["load_balancer_listener_port"] = int(
            child_load_balancer_listener_port.text or ""
        )
    child_load_balancer_target = el.find("LoadBalancerTarget")
    if child_load_balancer_target is not None:
        import capo_ec2.types.analysis_load_balancer_target

        out["load_balancer_target"] = (
            capo_ec2.types.analysis_load_balancer_target.deserialize_ec2_query(
                child_load_balancer_target
            )
        )
    child_load_balancer_target_group = el.find("LoadBalancerTargetGroup")
    if child_load_balancer_target_group is not None:
        import capo_ec2.types.analysis_component

        out["load_balancer_target_group"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_load_balancer_target_group
            )
        )
    if el.find("LoadBalancerTargetGroupSet") is not None:
        import capo_ec2.types.analysis_component_list

        out["load_balancer_target_groups"] = (
            capo_ec2.types.analysis_component_list.deserialize_ec2_query(
                el, "LoadBalancerTargetGroupSet"
            )
        )
    child_load_balancer_target_port = el.find("LoadBalancerTargetPort")
    if child_load_balancer_target_port is not None:
        out["load_balancer_target_port"] = int(
            child_load_balancer_target_port.text or ""
        )
    child_elastic_load_balancer_listener = el.find("ElasticLoadBalancerListener")
    if child_elastic_load_balancer_listener is not None:
        import capo_ec2.types.analysis_component

        out["elastic_load_balancer_listener"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_elastic_load_balancer_listener
            )
        )
    child_missing_component = el.find("MissingComponent")
    if child_missing_component is not None:
        out["missing_component"] = str(child_missing_component.text or "")
    child_nat_gateway = el.find("NatGateway")
    if child_nat_gateway is not None:
        import capo_ec2.types.analysis_component

        out["nat_gateway"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_nat_gateway
        )
    child_network_interface = el.find("NetworkInterface")
    if child_network_interface is not None:
        import capo_ec2.types.analysis_component

        out["network_interface"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_network_interface
            )
        )
    child_packet_field = el.find("PacketField")
    if child_packet_field is not None:
        out["packet_field"] = str(child_packet_field.text or "")
    child_vpc_peering_connection = el.find("VpcPeeringConnection")
    if child_vpc_peering_connection is not None:
        import capo_ec2.types.analysis_component

        out["vpc_peering_connection"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_vpc_peering_connection
            )
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    if el.find("PortRangeSet") is not None:
        import capo_ec2.types.port_range_list

        out["port_ranges"] = capo_ec2.types.port_range_list.deserialize_ec2_query(
            el, "PortRangeSet"
        )
    child_prefix_list = el.find("PrefixList")
    if child_prefix_list is not None:
        import capo_ec2.types.analysis_component

        out["prefix_list"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_prefix_list
        )
    if el.find("ProtocolSet") is not None:
        import capo_ec2.types.string_list

        out["protocols"] = capo_ec2.types.string_list.deserialize_ec2_query(
            el, "ProtocolSet"
        )
    child_route_table_route = el.find("RouteTableRoute")
    if child_route_table_route is not None:
        import capo_ec2.types.analysis_route_table_route

        out["route_table_route"] = (
            capo_ec2.types.analysis_route_table_route.deserialize_ec2_query(
                child_route_table_route
            )
        )
    child_route_table = el.find("RouteTable")
    if child_route_table is not None:
        import capo_ec2.types.analysis_component

        out["route_table"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_route_table
        )
    child_security_group = el.find("SecurityGroup")
    if child_security_group is not None:
        import capo_ec2.types.analysis_component

        out["security_group"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_security_group
        )
    child_security_group_rule = el.find("SecurityGroupRule")
    if child_security_group_rule is not None:
        import capo_ec2.types.analysis_security_group_rule

        out["security_group_rule"] = (
            capo_ec2.types.analysis_security_group_rule.deserialize_ec2_query(
                child_security_group_rule
            )
        )
    if el.find("SecurityGroupSet") is not None:
        import capo_ec2.types.analysis_component_list

        out["security_groups"] = (
            capo_ec2.types.analysis_component_list.deserialize_ec2_query(
                el, "SecurityGroupSet"
            )
        )
    child_source_vpc = el.find("SourceVpc")
    if child_source_vpc is not None:
        import capo_ec2.types.analysis_component

        out["source_vpc"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_source_vpc
        )
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_subnet = el.find("Subnet")
    if child_subnet is not None:
        import capo_ec2.types.analysis_component

        out["subnet"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_subnet
        )
    child_subnet_route_table = el.find("SubnetRouteTable")
    if child_subnet_route_table is not None:
        import capo_ec2.types.analysis_component

        out["subnet_route_table"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_subnet_route_table
            )
        )
    child_vpc = el.find("Vpc")
    if child_vpc is not None:
        import capo_ec2.types.analysis_component

        out["vpc"] = capo_ec2.types.analysis_component.deserialize_ec2_query(child_vpc)
    child_vpc_endpoint = el.find("VpcEndpoint")
    if child_vpc_endpoint is not None:
        import capo_ec2.types.analysis_component

        out["vpc_endpoint"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_vpc_endpoint
        )
    child_vpn_connection = el.find("VpnConnection")
    if child_vpn_connection is not None:
        import capo_ec2.types.analysis_component

        out["vpn_connection"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_vpn_connection
        )
    child_vpn_gateway = el.find("VpnGateway")
    if child_vpn_gateway is not None:
        import capo_ec2.types.analysis_component

        out["vpn_gateway"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_vpn_gateway
        )
    child_transit_gateway = el.find("TransitGateway")
    if child_transit_gateway is not None:
        import capo_ec2.types.analysis_component

        out["transit_gateway"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_transit_gateway
            )
        )
    child_transit_gateway_route_table = el.find("TransitGatewayRouteTable")
    if child_transit_gateway_route_table is not None:
        import capo_ec2.types.analysis_component

        out["transit_gateway_route_table"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_transit_gateway_route_table
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
    child_transit_gateway_attachment = el.find("TransitGatewayAttachment")
    if child_transit_gateway_attachment is not None:
        import capo_ec2.types.analysis_component

        out["transit_gateway_attachment"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_transit_gateway_attachment
            )
        )
    child_component_account = el.find("ComponentAccount")
    if child_component_account is not None:
        out["component_account"] = str(child_component_account.text or "")
    child_component_region = el.find("ComponentRegion")
    if child_component_region is not None:
        out["component_region"] = str(child_component_region.text or "")
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
    return out
