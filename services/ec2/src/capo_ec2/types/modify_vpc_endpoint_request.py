"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.dns_options_specification
    import capo_ec2.types.ip_address_type
    import capo_ec2.types.string
    import capo_ec2.types.subnet_configurations_list
    import capo_ec2.types.vpc_endpoint_id
    import capo_ec2.types.vpc_endpoint_route_table_id_list
    import capo_ec2.types.vpc_endpoint_security_group_id_list
    import capo_ec2.types.vpc_endpoint_subnet_id_list


class ModifyVpcEndpointRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    vpc_endpoint_id: NotRequired["capo_ec2.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The ID of the endpoint.</p>"""
    reset_policy: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>(Gateway endpoint) Specify <code>true</code> to reset the policy document to the default policy. The default policy allows full access to the service.</p>"""
    policy_document: NotRequired["capo_ec2.types.string.String"]
    """<p>(Interface and gateway endpoints) A policy to attach to the endpoint that controls access to the service. The policy must be in valid JSON format.</p>"""
    add_route_table_ids: NotRequired[
        "capo_ec2.types.vpc_endpoint_route_table_id_list.VpcEndpointRouteTableIdList"
    ]
    """<p>(Gateway endpoint) The IDs of the route tables to associate with the endpoint.</p>"""
    remove_route_table_ids: NotRequired[
        "capo_ec2.types.vpc_endpoint_route_table_id_list.VpcEndpointRouteTableIdList"
    ]
    """<p>(Gateway endpoint) The IDs of the route tables to disassociate from the endpoint.</p>"""
    add_subnet_ids: NotRequired[
        "capo_ec2.types.vpc_endpoint_subnet_id_list.VpcEndpointSubnetIdList"
    ]
    """<p>(Interface and Gateway Load Balancer endpoints) The IDs of the subnets in which to serve the endpoint. For a Gateway Load Balancer endpoint, you can specify only one subnet.</p>"""
    remove_subnet_ids: NotRequired[
        "capo_ec2.types.vpc_endpoint_subnet_id_list.VpcEndpointSubnetIdList"
    ]
    """<p>(Interface endpoint) The IDs of the subnets from which to remove the endpoint.</p>"""
    add_security_group_ids: NotRequired[
        "capo_ec2.types.vpc_endpoint_security_group_id_list.VpcEndpointSecurityGroupIdList"
    ]
    """<p>(Interface endpoint) The IDs of the security groups to associate with the endpoint network interfaces.</p>"""
    remove_security_group_ids: NotRequired[
        "capo_ec2.types.vpc_endpoint_security_group_id_list.VpcEndpointSecurityGroupIdList"
    ]
    """<p>(Interface endpoint) The IDs of the security groups to disassociate from the endpoint network interfaces.</p>"""
    ip_address_type: NotRequired["capo_ec2.types.ip_address_type.IpAddressType"]
    """<p>The IP address type for the endpoint.</p>"""
    dns_options: NotRequired[
        "capo_ec2.types.dns_options_specification.DnsOptionsSpecification"
    ]
    """<p>The DNS options for the endpoint.</p>"""
    private_dns_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>(Interface endpoint) Indicates whether a private hosted zone is associated with the VPC.</p>"""
    subnet_configurations: NotRequired[
        "capo_ec2.types.subnet_configurations_list.SubnetConfigurationsList"
    ]
    """<p>The subnet configurations for the endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcEndpointRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "vpc_endpoint_id" in value:
        pairs.append((f"{key_prefix}VpcEndpointId", str(value["vpc_endpoint_id"])))
    if "reset_policy" in value:
        pairs.append(
            (f"{key_prefix}ResetPolicy", "true" if value["reset_policy"] else "false")
        )
    if "policy_document" in value:
        pairs.append((f"{key_prefix}PolicyDocument", str(value["policy_document"])))
    if "add_route_table_ids" in value:
        import capo_ec2.types.vpc_endpoint_route_table_id_list

        capo_ec2.types.vpc_endpoint_route_table_id_list.serialize_ec2_query(
            value["add_route_table_ids"], pairs, f"{key_prefix}AddRouteTableId"
        )
    if "remove_route_table_ids" in value:
        import capo_ec2.types.vpc_endpoint_route_table_id_list

        capo_ec2.types.vpc_endpoint_route_table_id_list.serialize_ec2_query(
            value["remove_route_table_ids"], pairs, f"{key_prefix}RemoveRouteTableId"
        )
    if "add_subnet_ids" in value:
        import capo_ec2.types.vpc_endpoint_subnet_id_list

        capo_ec2.types.vpc_endpoint_subnet_id_list.serialize_ec2_query(
            value["add_subnet_ids"], pairs, f"{key_prefix}AddSubnetId"
        )
    if "remove_subnet_ids" in value:
        import capo_ec2.types.vpc_endpoint_subnet_id_list

        capo_ec2.types.vpc_endpoint_subnet_id_list.serialize_ec2_query(
            value["remove_subnet_ids"], pairs, f"{key_prefix}RemoveSubnetId"
        )
    if "add_security_group_ids" in value:
        import capo_ec2.types.vpc_endpoint_security_group_id_list

        capo_ec2.types.vpc_endpoint_security_group_id_list.serialize_ec2_query(
            value["add_security_group_ids"], pairs, f"{key_prefix}AddSecurityGroupId"
        )
    if "remove_security_group_ids" in value:
        import capo_ec2.types.vpc_endpoint_security_group_id_list

        capo_ec2.types.vpc_endpoint_security_group_id_list.serialize_ec2_query(
            value["remove_security_group_ids"],
            pairs,
            f"{key_prefix}RemoveSecurityGroupId",
        )
    if "ip_address_type" in value:
        import capo_ec2.types.ip_address_type

        capo_ec2.types.ip_address_type.serialize_ec2_query(
            value["ip_address_type"], pairs, f"{key_prefix}IpAddressType"
        )
    if "dns_options" in value:
        import capo_ec2.types.dns_options_specification

        capo_ec2.types.dns_options_specification.serialize_ec2_query(
            value["dns_options"], pairs, f"{key_prefix}DnsOptions"
        )
    if "private_dns_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}PrivateDnsEnabled",
                "true" if value["private_dns_enabled"] else "false",
            )
        )
    if "subnet_configurations" in value:
        import capo_ec2.types.subnet_configurations_list

        capo_ec2.types.subnet_configurations_list.serialize_ec2_query(
            value["subnet_configurations"], pairs, f"{key_prefix}SubnetConfiguration"
        )


def deserialize_ec2_query(el: Element) -> ModifyVpcEndpointRequest:
    out: ModifyVpcEndpointRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_vpc_endpoint_id = el.find("VpcEndpointId")
    if child_vpc_endpoint_id is not None:
        out["vpc_endpoint_id"] = str(child_vpc_endpoint_id.text or "")
    child_reset_policy = el.find("ResetPolicy")
    if child_reset_policy is not None:
        out["reset_policy"] = (child_reset_policy.text or "").lower() == "true"
    child_policy_document = el.find("PolicyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    child_add_route_table_ids = el.find("AddRouteTableId")
    if child_add_route_table_ids is not None:
        import capo_ec2.types.vpc_endpoint_route_table_id_list

        out["add_route_table_ids"] = (
            capo_ec2.types.vpc_endpoint_route_table_id_list.deserialize_ec2_query(
                child_add_route_table_ids
            )
        )
    child_remove_route_table_ids = el.find("RemoveRouteTableId")
    if child_remove_route_table_ids is not None:
        import capo_ec2.types.vpc_endpoint_route_table_id_list

        out["remove_route_table_ids"] = (
            capo_ec2.types.vpc_endpoint_route_table_id_list.deserialize_ec2_query(
                child_remove_route_table_ids
            )
        )
    child_add_subnet_ids = el.find("AddSubnetId")
    if child_add_subnet_ids is not None:
        import capo_ec2.types.vpc_endpoint_subnet_id_list

        out["add_subnet_ids"] = (
            capo_ec2.types.vpc_endpoint_subnet_id_list.deserialize_ec2_query(
                child_add_subnet_ids
            )
        )
    child_remove_subnet_ids = el.find("RemoveSubnetId")
    if child_remove_subnet_ids is not None:
        import capo_ec2.types.vpc_endpoint_subnet_id_list

        out["remove_subnet_ids"] = (
            capo_ec2.types.vpc_endpoint_subnet_id_list.deserialize_ec2_query(
                child_remove_subnet_ids
            )
        )
    child_add_security_group_ids = el.find("AddSecurityGroupId")
    if child_add_security_group_ids is not None:
        import capo_ec2.types.vpc_endpoint_security_group_id_list

        out["add_security_group_ids"] = (
            capo_ec2.types.vpc_endpoint_security_group_id_list.deserialize_ec2_query(
                child_add_security_group_ids
            )
        )
    child_remove_security_group_ids = el.find("RemoveSecurityGroupId")
    if child_remove_security_group_ids is not None:
        import capo_ec2.types.vpc_endpoint_security_group_id_list

        out["remove_security_group_ids"] = (
            capo_ec2.types.vpc_endpoint_security_group_id_list.deserialize_ec2_query(
                child_remove_security_group_ids
            )
        )
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import capo_ec2.types.ip_address_type

        out["ip_address_type"] = capo_ec2.types.ip_address_type.deserialize_ec2_query(
            child_ip_address_type
        )
    child_dns_options = el.find("DnsOptions")
    if child_dns_options is not None:
        import capo_ec2.types.dns_options_specification

        out["dns_options"] = (
            capo_ec2.types.dns_options_specification.deserialize_ec2_query(
                child_dns_options
            )
        )
    child_private_dns_enabled = el.find("PrivateDnsEnabled")
    if child_private_dns_enabled is not None:
        out["private_dns_enabled"] = (
            child_private_dns_enabled.text or ""
        ).lower() == "true"
    child_subnet_configurations = el.find("SubnetConfiguration")
    if child_subnet_configurations is not None:
        import capo_ec2.types.subnet_configurations_list

        out["subnet_configurations"] = (
            capo_ec2.types.subnet_configurations_list.deserialize_ec2_query(
                child_subnet_configurations
            )
        )
    return out
