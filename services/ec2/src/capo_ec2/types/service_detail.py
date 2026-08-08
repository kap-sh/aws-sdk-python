"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.dns_name_state
    import capo_ec2.types.payer_responsibility
    import capo_ec2.types.private_dns_details_set
    import capo_ec2.types.service_type_detail_set
    import capo_ec2.types.string
    import capo_ec2.types.supported_ip_address_types
    import capo_ec2.types.tag_list
    import capo_ec2.types.value_string_list


class ServiceDetail(TypedDict, closed=True):
    service_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the service.</p>"""
    service_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the endpoint service.</p>"""
    service_type: NotRequired[
        "capo_ec2.types.service_type_detail_set.ServiceTypeDetailSet"
    ]
    """<p>The type of service.</p>"""
    service_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region where the service is hosted.</p>"""
    availability_zone_ids: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IDs of the Availability Zones in which the service is available.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    availability_zones: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The Availability Zones in which the service is available.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    owner: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the service owner.</p>"""
    base_endpoint_dns_names: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The DNS names for the service.</p>"""
    private_dns_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The private DNS name for the service.</p>"""
    private_dns_names: NotRequired[
        "capo_ec2.types.private_dns_details_set.PrivateDnsDetailsSet"
    ]
    """<p>The private DNS names assigned to the VPC endpoint service.</p>"""
    vpc_endpoint_policy_supported: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the service supports endpoint policies.</p>"""
    acceptance_required: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether VPC endpoint connection requests to the service must be accepted by the service owner.</p>"""
    manages_vpc_endpoints: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the service manages its VPC endpoints. Management of the service VPC endpoints using the VPC endpoint API is restricted.</p>"""
    payer_responsibility: NotRequired[
        "capo_ec2.types.payer_responsibility.PayerResponsibility"
    ]
    """<p>The payer responsibility.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the service.</p>"""
    private_dns_name_verification_state: NotRequired[
        "capo_ec2.types.dns_name_state.DnsNameState"
    ]
    """<p>The verification state of the VPC endpoint service.</p> <p>Consumers of the endpoint service cannot use the private name when the state is not <code>verified</code>.</p>"""
    supported_ip_address_types: NotRequired[
        "capo_ec2.types.supported_ip_address_types.SupportedIpAddressTypes"
    ]
    """<p>The supported IP address types.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ServiceDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "service_name" in value:
        pairs.append((f"{key_prefix}ServiceName", str(value["service_name"])))
    if "service_id" in value:
        pairs.append((f"{key_prefix}ServiceId", str(value["service_id"])))
    if "service_type" in value:
        import capo_ec2.types.service_type_detail_set

        capo_ec2.types.service_type_detail_set.serialize_ec2_query(
            value["service_type"], pairs, f"{key_prefix}ServiceType"
        )
    if "service_region" in value:
        pairs.append((f"{key_prefix}ServiceRegion", str(value["service_region"])))
    if "availability_zone_ids" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["availability_zone_ids"], pairs, f"{key_prefix}AvailabilityZoneIdSet"
        )
    if "availability_zones" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZoneSet"
        )
    if "owner" in value:
        pairs.append((f"{key_prefix}Owner", str(value["owner"])))
    if "base_endpoint_dns_names" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["base_endpoint_dns_names"],
            pairs,
            f"{key_prefix}BaseEndpointDnsNameSet",
        )
    if "private_dns_name" in value:
        pairs.append((f"{key_prefix}PrivateDnsName", str(value["private_dns_name"])))
    if "private_dns_names" in value:
        import capo_ec2.types.private_dns_details_set

        capo_ec2.types.private_dns_details_set.serialize_ec2_query(
            value["private_dns_names"], pairs, f"{key_prefix}PrivateDnsNameSet"
        )
    if "vpc_endpoint_policy_supported" in value:
        pairs.append(
            (
                f"{key_prefix}VpcEndpointPolicySupported",
                "true" if value["vpc_endpoint_policy_supported"] else "false",
            )
        )
    if "acceptance_required" in value:
        pairs.append(
            (
                f"{key_prefix}AcceptanceRequired",
                "true" if value["acceptance_required"] else "false",
            )
        )
    if "manages_vpc_endpoints" in value:
        pairs.append(
            (
                f"{key_prefix}ManagesVpcEndpoints",
                "true" if value["manages_vpc_endpoints"] else "false",
            )
        )
    if "payer_responsibility" in value:
        import capo_ec2.types.payer_responsibility

        capo_ec2.types.payer_responsibility.serialize_ec2_query(
            value["payer_responsibility"], pairs, f"{key_prefix}PayerResponsibility"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "private_dns_name_verification_state" in value:
        import capo_ec2.types.dns_name_state

        capo_ec2.types.dns_name_state.serialize_ec2_query(
            value["private_dns_name_verification_state"],
            pairs,
            f"{key_prefix}PrivateDnsNameVerificationState",
        )
    if "supported_ip_address_types" in value:
        import capo_ec2.types.supported_ip_address_types

        capo_ec2.types.supported_ip_address_types.serialize_ec2_query(
            value["supported_ip_address_types"],
            pairs,
            f"{key_prefix}SupportedIpAddressTypeSet",
        )


def deserialize_ec2_query(el: Element) -> ServiceDetail:
    out: ServiceDetail = {}  # type: ignore[typeddict-item]
    child_service_name = el.find("serviceName")
    if child_service_name is not None:
        out["service_name"] = str(child_service_name.text or "")
    child_service_id = el.find("serviceId")
    if child_service_id is not None:
        out["service_id"] = str(child_service_id.text or "")
    if el.find("serviceType") is not None:
        import capo_ec2.types.service_type_detail_set

        out["service_type"] = (
            capo_ec2.types.service_type_detail_set.deserialize_ec2_query(
                el, "serviceType"
            )
        )
    child_service_region = el.find("serviceRegion")
    if child_service_region is not None:
        out["service_region"] = str(child_service_region.text or "")
    if el.find("availabilityZoneIdSet") is not None:
        import capo_ec2.types.value_string_list

        out["availability_zone_ids"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "availabilityZoneIdSet"
            )
        )
    if el.find("availabilityZoneSet") is not None:
        import capo_ec2.types.value_string_list

        out["availability_zones"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "availabilityZoneSet"
            )
        )
    child_owner = el.find("owner")
    if child_owner is not None:
        out["owner"] = str(child_owner.text or "")
    if el.find("baseEndpointDnsNameSet") is not None:
        import capo_ec2.types.value_string_list

        out["base_endpoint_dns_names"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "baseEndpointDnsNameSet"
            )
        )
    child_private_dns_name = el.find("privateDnsName")
    if child_private_dns_name is not None:
        out["private_dns_name"] = str(child_private_dns_name.text or "")
    if el.find("privateDnsNameSet") is not None:
        import capo_ec2.types.private_dns_details_set

        out["private_dns_names"] = (
            capo_ec2.types.private_dns_details_set.deserialize_ec2_query(
                el, "privateDnsNameSet"
            )
        )
    child_vpc_endpoint_policy_supported = el.find("vpcEndpointPolicySupported")
    if child_vpc_endpoint_policy_supported is not None:
        out["vpc_endpoint_policy_supported"] = (
            child_vpc_endpoint_policy_supported.text or ""
        ).lower() == "true"
    child_acceptance_required = el.find("acceptanceRequired")
    if child_acceptance_required is not None:
        out["acceptance_required"] = (
            child_acceptance_required.text or ""
        ).lower() == "true"
    child_manages_vpc_endpoints = el.find("managesVpcEndpoints")
    if child_manages_vpc_endpoints is not None:
        out["manages_vpc_endpoints"] = (
            child_manages_vpc_endpoints.text or ""
        ).lower() == "true"
    child_payer_responsibility = el.find("payerResponsibility")
    if child_payer_responsibility is not None:
        import capo_ec2.types.payer_responsibility

        out["payer_responsibility"] = (
            capo_ec2.types.payer_responsibility.deserialize_ec2_query(
                child_payer_responsibility
            )
        )
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    child_private_dns_name_verification_state = el.find(
        "privateDnsNameVerificationState"
    )
    if child_private_dns_name_verification_state is not None:
        import capo_ec2.types.dns_name_state

        out["private_dns_name_verification_state"] = (
            capo_ec2.types.dns_name_state.deserialize_ec2_query(
                child_private_dns_name_verification_state
            )
        )
    if el.find("supportedIpAddressTypeSet") is not None:
        import capo_ec2.types.supported_ip_address_types

        out["supported_ip_address_types"] = (
            capo_ec2.types.supported_ip_address_types.deserialize_ec2_query(
                el, "supportedIpAddressTypeSet"
            )
        )
    return out
