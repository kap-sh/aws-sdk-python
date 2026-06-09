"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.payer_responsibility
    import aws_sdk_ec2.types.private_dns_name_configuration
    import aws_sdk_ec2.types.service_state
    import aws_sdk_ec2.types.service_type_detail_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.supported_ip_address_types
    import aws_sdk_ec2.types.supported_region_set
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.value_string_list


class ServiceConfiguration(TypedDict):
    service_type: NotRequired[
        "aws_sdk_ec2.types.service_type_detail_set.ServiceTypeDetailSet"
    ]
    """<p>The type of service.</p>"""
    service_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the service.</p>"""
    service_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the service.</p>"""
    service_state: NotRequired["aws_sdk_ec2.types.service_state.ServiceState"]
    """<p>The service state.</p>"""
    availability_zone_ids: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IDs of the Availability Zones in which the service is available.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    availability_zones: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Availability Zones in which the service is available.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    acceptance_required: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether requests from other Amazon Web Services accounts to create an endpoint to the service must first be accepted.</p>"""
    manages_vpc_endpoints: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the service manages its VPC endpoints. Management of the service VPC endpoints using the VPC endpoint API is restricted.</p>"""
    network_load_balancer_arns: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the Network Load Balancers for the service.</p>"""
    gateway_load_balancer_arns: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the Gateway Load Balancers for the service.</p>"""
    supported_ip_address_types: NotRequired[
        "aws_sdk_ec2.types.supported_ip_address_types.SupportedIpAddressTypes"
    ]
    """<p>The supported IP address types.</p>"""
    base_endpoint_dns_names: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The DNS names for the service.</p>"""
    private_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private DNS name for the service.</p>"""
    private_dns_name_configuration: NotRequired[
        "aws_sdk_ec2.types.private_dns_name_configuration.PrivateDnsNameConfiguration"
    ]
    """<p>Information about the endpoint service private DNS name configuration.</p>"""
    payer_responsibility: NotRequired[
        "aws_sdk_ec2.types.payer_responsibility.PayerResponsibility"
    ]
    """<p>The payer responsibility.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the service.</p>"""
    supported_regions: NotRequired[
        "aws_sdk_ec2.types.supported_region_set.SupportedRegionSet"
    ]
    """<p>The supported Regions.</p>"""
    remote_access_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether consumers can access the service from a Region other than the Region where the service is hosted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ServiceConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "service_type" in value:
        import aws_sdk_ec2.types.service_type_detail_set

        aws_sdk_ec2.types.service_type_detail_set.serialize_ec2_query(
            value["service_type"], pairs, f"{prefix}.ServiceType"
        )
    if "service_id" in value:
        pairs.append((f"{prefix}.ServiceId", str(value["service_id"])))
    if "service_name" in value:
        pairs.append((f"{prefix}.ServiceName", str(value["service_name"])))
    if "service_state" in value:
        import aws_sdk_ec2.types.service_state

        aws_sdk_ec2.types.service_state.serialize_ec2_query(
            value["service_state"], pairs, f"{prefix}.ServiceState"
        )
    if "availability_zone_ids" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["availability_zone_ids"], pairs, f"{prefix}.AvailabilityZoneIdSet"
        )
    if "availability_zones" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["availability_zones"], pairs, f"{prefix}.AvailabilityZoneSet"
        )
    if "acceptance_required" in value:
        pairs.append(
            (
                f"{prefix}.AcceptanceRequired",
                "true" if value["acceptance_required"] else "false",
            )
        )
    if "manages_vpc_endpoints" in value:
        pairs.append(
            (
                f"{prefix}.ManagesVpcEndpoints",
                "true" if value["manages_vpc_endpoints"] else "false",
            )
        )
    if "network_load_balancer_arns" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["network_load_balancer_arns"],
            pairs,
            f"{prefix}.NetworkLoadBalancerArnSet",
        )
    if "gateway_load_balancer_arns" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["gateway_load_balancer_arns"],
            pairs,
            f"{prefix}.GatewayLoadBalancerArnSet",
        )
    if "supported_ip_address_types" in value:
        import aws_sdk_ec2.types.supported_ip_address_types

        aws_sdk_ec2.types.supported_ip_address_types.serialize_ec2_query(
            value["supported_ip_address_types"],
            pairs,
            f"{prefix}.SupportedIpAddressTypeSet",
        )
    if "base_endpoint_dns_names" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["base_endpoint_dns_names"], pairs, f"{prefix}.BaseEndpointDnsNameSet"
        )
    if "private_dns_name" in value:
        pairs.append((f"{prefix}.PrivateDnsName", str(value["private_dns_name"])))
    if "private_dns_name_configuration" in value:
        import aws_sdk_ec2.types.private_dns_name_configuration

        aws_sdk_ec2.types.private_dns_name_configuration.serialize_ec2_query(
            value["private_dns_name_configuration"],
            pairs,
            f"{prefix}.PrivateDnsNameConfiguration",
        )
    if "payer_responsibility" in value:
        import aws_sdk_ec2.types.payer_responsibility

        aws_sdk_ec2.types.payer_responsibility.serialize_ec2_query(
            value["payer_responsibility"], pairs, f"{prefix}.PayerResponsibility"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "supported_regions" in value:
        import aws_sdk_ec2.types.supported_region_set

        aws_sdk_ec2.types.supported_region_set.serialize_ec2_query(
            value["supported_regions"], pairs, f"{prefix}.SupportedRegionSet"
        )
    if "remote_access_enabled" in value:
        pairs.append(
            (
                f"{prefix}.RemoteAccessEnabled",
                "true" if value["remote_access_enabled"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> ServiceConfiguration:
    out: ServiceConfiguration = {}  # type: ignore[typeddict-item]
    if el.find("ServiceType") is not None:
        import aws_sdk_ec2.types.service_type_detail_set

        out["service_type"] = (
            aws_sdk_ec2.types.service_type_detail_set.deserialize_ec2_query(
                el, "ServiceType"
            )
        )
    child_service_id = el.find("ServiceId")
    if child_service_id is not None:
        out["service_id"] = str(child_service_id.text or "")
    child_service_name = el.find("ServiceName")
    if child_service_name is not None:
        out["service_name"] = str(child_service_name.text or "")
    child_service_state = el.find("ServiceState")
    if child_service_state is not None:
        import aws_sdk_ec2.types.service_state

        out["service_state"] = aws_sdk_ec2.types.service_state.deserialize_ec2_query(
            child_service_state
        )
    if el.find("AvailabilityZoneIdSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["availability_zone_ids"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "AvailabilityZoneIdSet"
            )
        )
    if el.find("AvailabilityZoneSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["availability_zones"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "AvailabilityZoneSet"
            )
        )
    child_acceptance_required = el.find("AcceptanceRequired")
    if child_acceptance_required is not None:
        out["acceptance_required"] = (
            child_acceptance_required.text or ""
        ).lower() == "true"
    child_manages_vpc_endpoints = el.find("ManagesVpcEndpoints")
    if child_manages_vpc_endpoints is not None:
        out["manages_vpc_endpoints"] = (
            child_manages_vpc_endpoints.text or ""
        ).lower() == "true"
    if el.find("NetworkLoadBalancerArnSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["network_load_balancer_arns"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "NetworkLoadBalancerArnSet"
            )
        )
    if el.find("GatewayLoadBalancerArnSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["gateway_load_balancer_arns"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "GatewayLoadBalancerArnSet"
            )
        )
    if el.find("SupportedIpAddressTypeSet") is not None:
        import aws_sdk_ec2.types.supported_ip_address_types

        out["supported_ip_address_types"] = (
            aws_sdk_ec2.types.supported_ip_address_types.deserialize_ec2_query(
                el, "SupportedIpAddressTypeSet"
            )
        )
    if el.find("BaseEndpointDnsNameSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["base_endpoint_dns_names"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "BaseEndpointDnsNameSet"
            )
        )
    child_private_dns_name = el.find("PrivateDnsName")
    if child_private_dns_name is not None:
        out["private_dns_name"] = str(child_private_dns_name.text or "")
    child_private_dns_name_configuration = el.find("PrivateDnsNameConfiguration")
    if child_private_dns_name_configuration is not None:
        import aws_sdk_ec2.types.private_dns_name_configuration

        out["private_dns_name_configuration"] = (
            aws_sdk_ec2.types.private_dns_name_configuration.deserialize_ec2_query(
                child_private_dns_name_configuration
            )
        )
    child_payer_responsibility = el.find("PayerResponsibility")
    if child_payer_responsibility is not None:
        import aws_sdk_ec2.types.payer_responsibility

        out["payer_responsibility"] = (
            aws_sdk_ec2.types.payer_responsibility.deserialize_ec2_query(
                child_payer_responsibility
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    if el.find("SupportedRegionSet") is not None:
        import aws_sdk_ec2.types.supported_region_set

        out["supported_regions"] = (
            aws_sdk_ec2.types.supported_region_set.deserialize_ec2_query(
                el, "SupportedRegionSet"
            )
        )
    child_remote_access_enabled = el.find("RemoteAccessEnabled")
    if child_remote_access_enabled is not None:
        out["remote_access_enabled"] = (
            child_remote_access_enabled.text or ""
        ).lower() == "true"
    return out
