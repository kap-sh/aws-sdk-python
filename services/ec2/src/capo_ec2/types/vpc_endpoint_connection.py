"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpointConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.dns_entry_set
    import capo_ec2.types.ip_address_type
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.state
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.value_string_list


class VpcEndpointConnection(TypedDict, closed=True):
    service_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the service to which the endpoint is connected.</p>"""
    vpc_endpoint_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC endpoint.</p>"""
    vpc_endpoint_owner: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the VPC endpoint.</p>"""
    vpc_endpoint_state: NotRequired["capo_ec2.types.state.State"]
    """<p>The state of the VPC endpoint.</p>"""
    creation_timestamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time that the VPC endpoint was created.</p>"""
    dns_entries: NotRequired["capo_ec2.types.dns_entry_set.DnsEntrySet"]
    """<p>The DNS entries for the VPC endpoint.</p>"""
    network_load_balancer_arns: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the network load balancers for the service.</p>"""
    gateway_load_balancer_arns: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the Gateway Load Balancers for the service.</p>"""
    ip_address_type: NotRequired["capo_ec2.types.ip_address_type.IpAddressType"]
    """<p>The IP address type for the endpoint.</p>"""
    vpc_endpoint_connection_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC endpoint connection.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    vpc_endpoint_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region of the endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEndpointConnection, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "service_id" in value:
        pairs.append((f"{key_prefix}ServiceId", str(value["service_id"])))
    if "vpc_endpoint_id" in value:
        pairs.append((f"{key_prefix}VpcEndpointId", str(value["vpc_endpoint_id"])))
    if "vpc_endpoint_owner" in value:
        pairs.append(
            (f"{key_prefix}VpcEndpointOwner", str(value["vpc_endpoint_owner"]))
        )
    if "vpc_endpoint_state" in value:
        import capo_ec2.types.state

        capo_ec2.types.state.serialize_ec2_query(
            value["vpc_endpoint_state"], pairs, f"{key_prefix}VpcEndpointState"
        )
    if "creation_timestamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["creation_timestamp"], pairs, f"{key_prefix}CreationTimestamp"
        )
    if "dns_entries" in value:
        import capo_ec2.types.dns_entry_set

        capo_ec2.types.dns_entry_set.serialize_ec2_query(
            value["dns_entries"], pairs, f"{key_prefix}DnsEntrySet"
        )
    if "network_load_balancer_arns" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["network_load_balancer_arns"],
            pairs,
            f"{key_prefix}NetworkLoadBalancerArnSet",
        )
    if "gateway_load_balancer_arns" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["gateway_load_balancer_arns"],
            pairs,
            f"{key_prefix}GatewayLoadBalancerArnSet",
        )
    if "ip_address_type" in value:
        import capo_ec2.types.ip_address_type

        capo_ec2.types.ip_address_type.serialize_ec2_query(
            value["ip_address_type"], pairs, f"{key_prefix}IpAddressType"
        )
    if "vpc_endpoint_connection_id" in value:
        pairs.append(
            (
                f"{key_prefix}VpcEndpointConnectionId",
                str(value["vpc_endpoint_connection_id"]),
            )
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "vpc_endpoint_region" in value:
        pairs.append(
            (f"{key_prefix}VpcEndpointRegion", str(value["vpc_endpoint_region"]))
        )


def deserialize_ec2_query(el: Element) -> VpcEndpointConnection:
    out: VpcEndpointConnection = {}  # type: ignore[typeddict-item]
    child_service_id = el.find("ServiceId")
    if child_service_id is not None:
        out["service_id"] = str(child_service_id.text or "")
    child_vpc_endpoint_id = el.find("VpcEndpointId")
    if child_vpc_endpoint_id is not None:
        out["vpc_endpoint_id"] = str(child_vpc_endpoint_id.text or "")
    child_vpc_endpoint_owner = el.find("VpcEndpointOwner")
    if child_vpc_endpoint_owner is not None:
        out["vpc_endpoint_owner"] = str(child_vpc_endpoint_owner.text or "")
    child_vpc_endpoint_state = el.find("VpcEndpointState")
    if child_vpc_endpoint_state is not None:
        import capo_ec2.types.state

        out["vpc_endpoint_state"] = capo_ec2.types.state.deserialize_ec2_query(
            child_vpc_endpoint_state
        )
    child_creation_timestamp = el.find("CreationTimestamp")
    if child_creation_timestamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["creation_timestamp"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_creation_timestamp
            )
        )
    if el.find("DnsEntrySet") is not None:
        import capo_ec2.types.dns_entry_set

        out["dns_entries"] = capo_ec2.types.dns_entry_set.deserialize_ec2_query(
            el, "DnsEntrySet"
        )
    if el.find("NetworkLoadBalancerArnSet") is not None:
        import capo_ec2.types.value_string_list

        out["network_load_balancer_arns"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "NetworkLoadBalancerArnSet"
            )
        )
    if el.find("GatewayLoadBalancerArnSet") is not None:
        import capo_ec2.types.value_string_list

        out["gateway_load_balancer_arns"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "GatewayLoadBalancerArnSet"
            )
        )
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import capo_ec2.types.ip_address_type

        out["ip_address_type"] = capo_ec2.types.ip_address_type.deserialize_ec2_query(
            child_ip_address_type
        )
    child_vpc_endpoint_connection_id = el.find("VpcEndpointConnectionId")
    if child_vpc_endpoint_connection_id is not None:
        out["vpc_endpoint_connection_id"] = str(
            child_vpc_endpoint_connection_id.text or ""
        )
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_vpc_endpoint_region = el.find("VpcEndpointRegion")
    if child_vpc_endpoint_region is not None:
        out["vpc_endpoint_region"] = str(child_vpc_endpoint_region.text or "")
    return out
