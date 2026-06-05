"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.dns_name_state
    import aws_sdk_ec2.types.payer_responsibility
    import aws_sdk_ec2.types.private_dns_details_set
    import aws_sdk_ec2.types.service_type_detail_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.supported_ip_address_types
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.value_string_list


class ServiceDetail(TypedDict):
    service_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the service.</p>"""
    service_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the endpoint service.</p>"""
    service_type: NotRequired[
        "aws_sdk_ec2.types.service_type_detail_set.ServiceTypeDetailSet"
    ]
    """<p>The type of service.</p>"""
    service_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region where the service is hosted.</p>"""
    availability_zone_ids: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IDs of the Availability Zones in which the service is available.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    availability_zones: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Availability Zones in which the service is available.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the service owner.</p>"""
    base_endpoint_dns_names: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The DNS names for the service.</p>"""
    private_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private DNS name for the service.</p>"""
    private_dns_names: NotRequired[
        "aws_sdk_ec2.types.private_dns_details_set.PrivateDnsDetailsSet"
    ]
    """<p>The private DNS names assigned to the VPC endpoint service.</p>"""
    vpc_endpoint_policy_supported: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the service supports endpoint policies.</p>"""
    acceptance_required: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether VPC endpoint connection requests to the service must be accepted by the service owner.</p>"""
    manages_vpc_endpoints: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the service manages its VPC endpoints. Management of the service VPC endpoints using the VPC endpoint API is restricted.</p>"""
    payer_responsibility: NotRequired[
        "aws_sdk_ec2.types.payer_responsibility.PayerResponsibility"
    ]
    """<p>The payer responsibility.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the service.</p>"""
    private_dns_name_verification_state: NotRequired[
        "aws_sdk_ec2.types.dns_name_state.DnsNameState"
    ]
    """<p>The verification state of the VPC endpoint service.</p> <p>Consumers of the endpoint service cannot use the private name when the state is not <code>verified</code>.</p>"""
    supported_ip_address_types: NotRequired[
        "aws_sdk_ec2.types.supported_ip_address_types.SupportedIpAddressTypes"
    ]
    """<p>The supported IP address types.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ServiceDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "service_name" in value:
        pairs.append((f"{prefix}.ServiceName", str(value["service_name"])))
    if "service_id" in value:
        pairs.append((f"{prefix}.ServiceId", str(value["service_id"])))
    if "service_type" in value:
        import aws_sdk_ec2.types.service_type_detail_set

        aws_sdk_ec2.types.service_type_detail_set.serialize_ec2_query(
            value["service_type"], pairs, f"{prefix}.ServiceType"
        )
    if "service_region" in value:
        pairs.append((f"{prefix}.ServiceRegion", str(value["service_region"])))
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
    if "owner" in value:
        pairs.append((f"{prefix}.Owner", str(value["owner"])))
    if "base_endpoint_dns_names" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["base_endpoint_dns_names"], pairs, f"{prefix}.BaseEndpointDnsNameSet"
        )
    if "private_dns_name" in value:
        pairs.append((f"{prefix}.PrivateDnsName", str(value["private_dns_name"])))
    if "private_dns_names" in value:
        import aws_sdk_ec2.types.private_dns_details_set

        aws_sdk_ec2.types.private_dns_details_set.serialize_ec2_query(
            value["private_dns_names"], pairs, f"{prefix}.PrivateDnsNameSet"
        )
    if "vpc_endpoint_policy_supported" in value:
        pairs.append(
            (
                f"{prefix}.VpcEndpointPolicySupported",
                "true" if value["vpc_endpoint_policy_supported"] else "false",
            )
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
    if "private_dns_name_verification_state" in value:
        import aws_sdk_ec2.types.dns_name_state

        aws_sdk_ec2.types.dns_name_state.serialize_ec2_query(
            value["private_dns_name_verification_state"],
            pairs,
            f"{prefix}.PrivateDnsNameVerificationState",
        )
    if "supported_ip_address_types" in value:
        import aws_sdk_ec2.types.supported_ip_address_types

        aws_sdk_ec2.types.supported_ip_address_types.serialize_ec2_query(
            value["supported_ip_address_types"],
            pairs,
            f"{prefix}.SupportedIpAddressTypeSet",
        )


def deserialize_ec2_query(el: Element) -> ServiceDetail:
    out: ServiceDetail = {}  # type: ignore[typeddict-item]
    child_service_name = el.find("ServiceName")
    if child_service_name is not None:
        out["service_name"] = str(child_service_name.text or "")
    child_service_id = el.find("ServiceId")
    if child_service_id is not None:
        out["service_id"] = str(child_service_id.text or "")
    if el.find("ServiceType") is not None:
        import aws_sdk_ec2.types.service_type_detail_set

        out["service_type"] = (
            aws_sdk_ec2.types.service_type_detail_set.deserialize_ec2_query(
                el, "ServiceType"
            )
        )
    child_service_region = el.find("ServiceRegion")
    if child_service_region is not None:
        out["service_region"] = str(child_service_region.text or "")
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
    child_owner = el.find("Owner")
    if child_owner is not None:
        out["owner"] = str(child_owner.text or "")
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
    if el.find("PrivateDnsNameSet") is not None:
        import aws_sdk_ec2.types.private_dns_details_set

        out["private_dns_names"] = (
            aws_sdk_ec2.types.private_dns_details_set.deserialize_ec2_query(
                el, "PrivateDnsNameSet"
            )
        )
    child_vpc_endpoint_policy_supported = el.find("VpcEndpointPolicySupported")
    if child_vpc_endpoint_policy_supported is not None:
        out["vpc_endpoint_policy_supported"] = (
            child_vpc_endpoint_policy_supported.text or ""
        ).lower() == "true"
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
    child_private_dns_name_verification_state = el.find(
        "PrivateDnsNameVerificationState"
    )
    if child_private_dns_name_verification_state is not None:
        import aws_sdk_ec2.types.dns_name_state

        out["private_dns_name_verification_state"] = (
            aws_sdk_ec2.types.dns_name_state.deserialize_ec2_query(
                child_private_dns_name_verification_state
            )
        )
    if el.find("SupportedIpAddressTypeSet") is not None:
        import aws_sdk_ec2.types.supported_ip_address_types

        out["supported_ip_address_types"] = (
            aws_sdk_ec2.types.supported_ip_address_types.deserialize_ec2_query(
                el, "SupportedIpAddressTypeSet"
            )
        )
    return out
