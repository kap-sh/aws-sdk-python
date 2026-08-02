"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointServiceConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.value_string_list
    import capo_ec2.types.vpc_endpoint_service_id


class ModifyVpcEndpointServiceConfigurationRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    service_id: NotRequired[
        "capo_ec2.types.vpc_endpoint_service_id.VpcEndpointServiceId"
    ]
    """<p>The ID of the service.</p>"""
    private_dns_name: NotRequired["capo_ec2.types.string.String"]
    """<p>(Interface endpoint configuration) The private DNS name to assign to the endpoint service.</p>"""
    remove_private_dns_name: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>(Interface endpoint configuration) Removes the private DNS name of the endpoint service.</p>"""
    acceptance_required: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether requests to create an endpoint to the service must be accepted.</p>"""
    add_network_load_balancer_arns: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of Network Load Balancers to add to the service configuration.</p>"""
    remove_network_load_balancer_arns: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of Network Load Balancers to remove from the service configuration.</p>"""
    add_gateway_load_balancer_arns: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of Gateway Load Balancers to add to the service configuration.</p>"""
    remove_gateway_load_balancer_arns: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of Gateway Load Balancers to remove from the service configuration.</p>"""
    add_supported_ip_address_types: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IP address types to add to the service configuration.</p>"""
    remove_supported_ip_address_types: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IP address types to remove from the service configuration.</p>"""
    add_supported_regions: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The supported Regions to add to the service configuration.</p>"""
    remove_supported_regions: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The supported Regions to remove from the service configuration.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcEndpointServiceConfigurationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "service_id" in value:
        pairs.append((f"{key_prefix}ServiceId", str(value["service_id"])))
    if "private_dns_name" in value:
        pairs.append((f"{key_prefix}PrivateDnsName", str(value["private_dns_name"])))
    if "remove_private_dns_name" in value:
        pairs.append(
            (
                f"{key_prefix}RemovePrivateDnsName",
                "true" if value["remove_private_dns_name"] else "false",
            )
        )
    if "acceptance_required" in value:
        pairs.append(
            (
                f"{key_prefix}AcceptanceRequired",
                "true" if value["acceptance_required"] else "false",
            )
        )
    if "add_network_load_balancer_arns" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["add_network_load_balancer_arns"],
            pairs,
            f"{key_prefix}AddNetworkLoadBalancerArns",
        )
    if "remove_network_load_balancer_arns" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["remove_network_load_balancer_arns"],
            pairs,
            f"{key_prefix}RemoveNetworkLoadBalancerArns",
        )
    if "add_gateway_load_balancer_arns" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["add_gateway_load_balancer_arns"],
            pairs,
            f"{key_prefix}AddGatewayLoadBalancerArns",
        )
    if "remove_gateway_load_balancer_arns" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["remove_gateway_load_balancer_arns"],
            pairs,
            f"{key_prefix}RemoveGatewayLoadBalancerArns",
        )
    if "add_supported_ip_address_types" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["add_supported_ip_address_types"],
            pairs,
            f"{key_prefix}AddSupportedIpAddressTypes",
        )
    if "remove_supported_ip_address_types" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["remove_supported_ip_address_types"],
            pairs,
            f"{key_prefix}RemoveSupportedIpAddressTypes",
        )
    if "add_supported_regions" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["add_supported_regions"], pairs, f"{key_prefix}AddSupportedRegions"
        )
    if "remove_supported_regions" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["remove_supported_regions"],
            pairs,
            f"{key_prefix}RemoveSupportedRegions",
        )


def deserialize_ec2_query(el: Element) -> ModifyVpcEndpointServiceConfigurationRequest:
    out: ModifyVpcEndpointServiceConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_service_id = el.find("ServiceId")
    if child_service_id is not None:
        out["service_id"] = str(child_service_id.text or "")
    child_private_dns_name = el.find("PrivateDnsName")
    if child_private_dns_name is not None:
        out["private_dns_name"] = str(child_private_dns_name.text or "")
    child_remove_private_dns_name = el.find("RemovePrivateDnsName")
    if child_remove_private_dns_name is not None:
        out["remove_private_dns_name"] = (
            child_remove_private_dns_name.text or ""
        ).lower() == "true"
    child_acceptance_required = el.find("AcceptanceRequired")
    if child_acceptance_required is not None:
        out["acceptance_required"] = (
            child_acceptance_required.text or ""
        ).lower() == "true"
    if el.find("AddNetworkLoadBalancerArns") is not None:
        import capo_ec2.types.value_string_list

        out["add_network_load_balancer_arns"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "AddNetworkLoadBalancerArns"
            )
        )
    if el.find("RemoveNetworkLoadBalancerArns") is not None:
        import capo_ec2.types.value_string_list

        out["remove_network_load_balancer_arns"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "RemoveNetworkLoadBalancerArns"
            )
        )
    if el.find("AddGatewayLoadBalancerArns") is not None:
        import capo_ec2.types.value_string_list

        out["add_gateway_load_balancer_arns"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "AddGatewayLoadBalancerArns"
            )
        )
    if el.find("RemoveGatewayLoadBalancerArns") is not None:
        import capo_ec2.types.value_string_list

        out["remove_gateway_load_balancer_arns"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "RemoveGatewayLoadBalancerArns"
            )
        )
    if el.find("AddSupportedIpAddressTypes") is not None:
        import capo_ec2.types.value_string_list

        out["add_supported_ip_address_types"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "AddSupportedIpAddressTypes"
            )
        )
    if el.find("RemoveSupportedIpAddressTypes") is not None:
        import capo_ec2.types.value_string_list

        out["remove_supported_ip_address_types"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "RemoveSupportedIpAddressTypes"
            )
        )
    if el.find("AddSupportedRegions") is not None:
        import capo_ec2.types.value_string_list

        out["add_supported_regions"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "AddSupportedRegions"
            )
        )
    if el.find("RemoveSupportedRegions") is not None:
        import capo_ec2.types.value_string_list

        out["remove_supported_regions"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "RemoveSupportedRegions"
            )
        )
    return out
