"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.dns_entry_set
    import aws_sdk_ec2.types.dns_options
    import aws_sdk_ec2.types.group_identifier_set
    import aws_sdk_ec2.types.ip_address_type
    import aws_sdk_ec2.types.last_error
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.resource_configuration_arn
    import aws_sdk_ec2.types.service_network_arn
    import aws_sdk_ec2.types.state
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_ip_prefixes_list
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.value_string_list
    import aws_sdk_ec2.types.vpc_endpoint_type


class VpcEndpoint(TypedDict, closed=True):
    vpc_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the endpoint.</p>"""
    vpc_endpoint_type: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_type.VpcEndpointType"
    ]
    """<p>The type of endpoint.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC to which the endpoint is associated.</p>"""
    service_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the service to which the endpoint is associated.</p>"""
    state: NotRequired["aws_sdk_ec2.types.state.State"]
    """<p>The state of the endpoint.</p>"""
    policy_document: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The policy document associated with the endpoint, if applicable.</p>"""
    route_table_ids: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>(Gateway endpoint) The IDs of the route tables associated with the endpoint.</p>"""
    subnet_ids: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>(Interface endpoint) The subnets for the endpoint.</p>"""
    groups: NotRequired["aws_sdk_ec2.types.group_identifier_set.GroupIdentifierSet"]
    """<p>(Interface endpoint) Information about the security groups that are associated with the network interface.</p>"""
    ip_address_type: NotRequired["aws_sdk_ec2.types.ip_address_type.IpAddressType"]
    """<p>The IP address type for the endpoint.</p>"""
    dns_options: NotRequired["aws_sdk_ec2.types.dns_options.DnsOptions"]
    """<p>The DNS options for the endpoint.</p>"""
    private_dns_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>(Interface endpoint) Indicates whether the VPC is associated with a private hosted zone.</p>"""
    requester_managed: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the endpoint is being managed by its service.</p>"""
    network_interface_ids: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>(Interface endpoint) The network interfaces for the endpoint.</p>"""
    dns_entries: NotRequired["aws_sdk_ec2.types.dns_entry_set.DnsEntrySet"]
    """<p>(Interface endpoint) The DNS entries for the endpoint.</p>"""
    creation_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time that the endpoint was created.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the endpoint.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the endpoint.</p>"""
    last_error: NotRequired["aws_sdk_ec2.types.last_error.LastError"]
    """<p>The last error that occurred for endpoint.</p>"""
    ipv4_prefixes: NotRequired[
        "aws_sdk_ec2.types.subnet_ip_prefixes_list.SubnetIpPrefixesList"
    ]
    """<p>Array of IPv4 prefixes.</p>"""
    ipv6_prefixes: NotRequired[
        "aws_sdk_ec2.types.subnet_ip_prefixes_list.SubnetIpPrefixesList"
    ]
    """<p>Array of IPv6 prefixes.</p>"""
    failure_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reason for the failure.</p>"""
    service_network_arn: NotRequired[
        "aws_sdk_ec2.types.service_network_arn.ServiceNetworkArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the service network.</p>"""
    resource_configuration_arn: NotRequired[
        "aws_sdk_ec2.types.resource_configuration_arn.ResourceConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource configuration.</p>"""
    service_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region where the service is hosted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEndpoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpc_endpoint_id" in value:
        pairs.append((f"{prefix}.VpcEndpointId", str(value["vpc_endpoint_id"])))
    if "vpc_endpoint_type" in value:
        import aws_sdk_ec2.types.vpc_endpoint_type

        aws_sdk_ec2.types.vpc_endpoint_type.serialize_ec2_query(
            value["vpc_endpoint_type"], pairs, f"{prefix}.VpcEndpointType"
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "service_name" in value:
        pairs.append((f"{prefix}.ServiceName", str(value["service_name"])))
    if "state" in value:
        import aws_sdk_ec2.types.state

        aws_sdk_ec2.types.state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "policy_document" in value:
        pairs.append((f"{prefix}.PolicyDocument", str(value["policy_document"])))
    if "route_table_ids" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["route_table_ids"], pairs, f"{prefix}.RouteTableIdSet"
        )
    if "subnet_ids" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIdSet"
        )
    if "groups" in value:
        import aws_sdk_ec2.types.group_identifier_set

        aws_sdk_ec2.types.group_identifier_set.serialize_ec2_query(
            value["groups"], pairs, f"{prefix}.GroupSet"
        )
    if "ip_address_type" in value:
        import aws_sdk_ec2.types.ip_address_type

        aws_sdk_ec2.types.ip_address_type.serialize_ec2_query(
            value["ip_address_type"], pairs, f"{prefix}.IpAddressType"
        )
    if "dns_options" in value:
        import aws_sdk_ec2.types.dns_options

        aws_sdk_ec2.types.dns_options.serialize_ec2_query(
            value["dns_options"], pairs, f"{prefix}.DnsOptions"
        )
    if "private_dns_enabled" in value:
        pairs.append(
            (
                f"{prefix}.PrivateDnsEnabled",
                "true" if value["private_dns_enabled"] else "false",
            )
        )
    if "requester_managed" in value:
        pairs.append(
            (
                f"{prefix}.RequesterManaged",
                "true" if value["requester_managed"] else "false",
            )
        )
    if "network_interface_ids" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["network_interface_ids"], pairs, f"{prefix}.NetworkInterfaceIdSet"
        )
    if "dns_entries" in value:
        import aws_sdk_ec2.types.dns_entry_set

        aws_sdk_ec2.types.dns_entry_set.serialize_ec2_query(
            value["dns_entries"], pairs, f"{prefix}.DnsEntrySet"
        )
    if "creation_timestamp" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["creation_timestamp"], pairs, f"{prefix}.CreationTimestamp"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "last_error" in value:
        import aws_sdk_ec2.types.last_error

        aws_sdk_ec2.types.last_error.serialize_ec2_query(
            value["last_error"], pairs, f"{prefix}.LastError"
        )
    if "ipv4_prefixes" in value:
        import aws_sdk_ec2.types.subnet_ip_prefixes_list

        aws_sdk_ec2.types.subnet_ip_prefixes_list.serialize_ec2_query(
            value["ipv4_prefixes"], pairs, f"{prefix}.Ipv4PrefixSet"
        )
    if "ipv6_prefixes" in value:
        import aws_sdk_ec2.types.subnet_ip_prefixes_list

        aws_sdk_ec2.types.subnet_ip_prefixes_list.serialize_ec2_query(
            value["ipv6_prefixes"], pairs, f"{prefix}.Ipv6PrefixSet"
        )
    if "failure_reason" in value:
        pairs.append((f"{prefix}.FailureReason", str(value["failure_reason"])))
    if "service_network_arn" in value:
        pairs.append((f"{prefix}.ServiceNetworkArn", str(value["service_network_arn"])))
    if "resource_configuration_arn" in value:
        pairs.append(
            (
                f"{prefix}.ResourceConfigurationArn",
                str(value["resource_configuration_arn"]),
            )
        )
    if "service_region" in value:
        pairs.append((f"{prefix}.ServiceRegion", str(value["service_region"])))


def deserialize_ec2_query(el: Element) -> VpcEndpoint:
    out: VpcEndpoint = {}  # type: ignore[typeddict-item]
    child_vpc_endpoint_id = el.find("VpcEndpointId")
    if child_vpc_endpoint_id is not None:
        out["vpc_endpoint_id"] = str(child_vpc_endpoint_id.text or "")
    child_vpc_endpoint_type = el.find("VpcEndpointType")
    if child_vpc_endpoint_type is not None:
        import aws_sdk_ec2.types.vpc_endpoint_type

        out["vpc_endpoint_type"] = (
            aws_sdk_ec2.types.vpc_endpoint_type.deserialize_ec2_query(
                child_vpc_endpoint_type
            )
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_service_name = el.find("ServiceName")
    if child_service_name is not None:
        out["service_name"] = str(child_service_name.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.state

        out["state"] = aws_sdk_ec2.types.state.deserialize_ec2_query(child_state)
    child_policy_document = el.find("PolicyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    if el.find("RouteTableIdSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["route_table_ids"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "RouteTableIdSet"
            )
        )
    if el.find("SubnetIdSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["subnet_ids"] = aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
            el, "SubnetIdSet"
        )
    if el.find("GroupSet") is not None:
        import aws_sdk_ec2.types.group_identifier_set

        out["groups"] = aws_sdk_ec2.types.group_identifier_set.deserialize_ec2_query(
            el, "GroupSet"
        )
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import aws_sdk_ec2.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_ec2.types.ip_address_type.deserialize_ec2_query(
                child_ip_address_type
            )
        )
    child_dns_options = el.find("DnsOptions")
    if child_dns_options is not None:
        import aws_sdk_ec2.types.dns_options

        out["dns_options"] = aws_sdk_ec2.types.dns_options.deserialize_ec2_query(
            child_dns_options
        )
    child_private_dns_enabled = el.find("PrivateDnsEnabled")
    if child_private_dns_enabled is not None:
        out["private_dns_enabled"] = (
            child_private_dns_enabled.text or ""
        ).lower() == "true"
    child_requester_managed = el.find("RequesterManaged")
    if child_requester_managed is not None:
        out["requester_managed"] = (
            child_requester_managed.text or ""
        ).lower() == "true"
    if el.find("NetworkInterfaceIdSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["network_interface_ids"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "NetworkInterfaceIdSet"
            )
        )
    if el.find("DnsEntrySet") is not None:
        import aws_sdk_ec2.types.dns_entry_set

        out["dns_entries"] = aws_sdk_ec2.types.dns_entry_set.deserialize_ec2_query(
            el, "DnsEntrySet"
        )
    child_creation_timestamp = el.find("CreationTimestamp")
    if child_creation_timestamp is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["creation_timestamp"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_creation_timestamp
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_last_error = el.find("LastError")
    if child_last_error is not None:
        import aws_sdk_ec2.types.last_error

        out["last_error"] = aws_sdk_ec2.types.last_error.deserialize_ec2_query(
            child_last_error
        )
    if el.find("Ipv4PrefixSet") is not None:
        import aws_sdk_ec2.types.subnet_ip_prefixes_list

        out["ipv4_prefixes"] = (
            aws_sdk_ec2.types.subnet_ip_prefixes_list.deserialize_ec2_query(
                el, "Ipv4PrefixSet"
            )
        )
    if el.find("Ipv6PrefixSet") is not None:
        import aws_sdk_ec2.types.subnet_ip_prefixes_list

        out["ipv6_prefixes"] = (
            aws_sdk_ec2.types.subnet_ip_prefixes_list.deserialize_ec2_query(
                el, "Ipv6PrefixSet"
            )
        )
    child_failure_reason = el.find("FailureReason")
    if child_failure_reason is not None:
        out["failure_reason"] = str(child_failure_reason.text or "")
    child_service_network_arn = el.find("ServiceNetworkArn")
    if child_service_network_arn is not None:
        out["service_network_arn"] = str(child_service_network_arn.text or "")
    child_resource_configuration_arn = el.find("ResourceConfigurationArn")
    if child_resource_configuration_arn is not None:
        out["resource_configuration_arn"] = str(
            child_resource_configuration_arn.text or ""
        )
    child_service_region = el.find("ServiceRegion")
    if child_service_region is not None:
        out["service_region"] = str(child_service_region.text or "")
    return out
