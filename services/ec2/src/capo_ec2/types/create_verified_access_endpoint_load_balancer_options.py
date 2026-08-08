"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessEndpointLoadBalancerOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.create_verified_access_endpoint_port_range_list
    import capo_ec2.types.create_verified_access_endpoint_subnet_id_list
    import capo_ec2.types.load_balancer_arn
    import capo_ec2.types.verified_access_endpoint_port_number
    import capo_ec2.types.verified_access_endpoint_protocol


class CreateVerifiedAccessEndpointLoadBalancerOptions(TypedDict, closed=True):
    protocol: NotRequired[
        "capo_ec2.types.verified_access_endpoint_protocol.VerifiedAccessEndpointProtocol"
    ]
    """<p>The IP protocol.</p>"""
    port: NotRequired[
        "capo_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The IP port number.</p>"""
    load_balancer_arn: NotRequired["capo_ec2.types.load_balancer_arn.LoadBalancerArn"]
    """<p>The ARN of the load balancer.</p>"""
    subnet_ids: NotRequired[
        "capo_ec2.types.create_verified_access_endpoint_subnet_id_list.CreateVerifiedAccessEndpointSubnetIdList"
    ]
    """<p>The IDs of the subnets. You can specify only one subnet per Availability Zone.</p>"""
    port_ranges: NotRequired[
        "capo_ec2.types.create_verified_access_endpoint_port_range_list.CreateVerifiedAccessEndpointPortRangeList"
    ]
    """<p>The port ranges.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVerifiedAccessEndpointLoadBalancerOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "protocol" in value:
        import capo_ec2.types.verified_access_endpoint_protocol

        capo_ec2.types.verified_access_endpoint_protocol.serialize_ec2_query(
            value["protocol"], pairs, f"{key_prefix}Protocol"
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "load_balancer_arn" in value:
        pairs.append((f"{key_prefix}LoadBalancerArn", str(value["load_balancer_arn"])))
    if "subnet_ids" in value:
        import capo_ec2.types.create_verified_access_endpoint_subnet_id_list

        capo_ec2.types.create_verified_access_endpoint_subnet_id_list.serialize_ec2_query(
            value["subnet_ids"], pairs, f"{key_prefix}SubnetId"
        )
    if "port_ranges" in value:
        import capo_ec2.types.create_verified_access_endpoint_port_range_list

        capo_ec2.types.create_verified_access_endpoint_port_range_list.serialize_ec2_query(
            value["port_ranges"], pairs, f"{key_prefix}PortRange"
        )


def deserialize_ec2_query(
    el: Element,
) -> CreateVerifiedAccessEndpointLoadBalancerOptions:
    out: CreateVerifiedAccessEndpointLoadBalancerOptions = {}  # type: ignore[typeddict-item]
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import capo_ec2.types.verified_access_endpoint_protocol

        out["protocol"] = (
            capo_ec2.types.verified_access_endpoint_protocol.deserialize_ec2_query(
                child_protocol
            )
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_load_balancer_arn = el.find("LoadBalancerArn")
    if child_load_balancer_arn is not None:
        out["load_balancer_arn"] = str(child_load_balancer_arn.text or "")
    if el.find("SubnetId") is not None:
        import capo_ec2.types.create_verified_access_endpoint_subnet_id_list

        out["subnet_ids"] = (
            capo_ec2.types.create_verified_access_endpoint_subnet_id_list.deserialize_ec2_query(
                el, "SubnetId"
            )
        )
    if el.find("PortRange") is not None:
        import capo_ec2.types.create_verified_access_endpoint_port_range_list

        out["port_ranges"] = (
            capo_ec2.types.create_verified_access_endpoint_port_range_list.deserialize_ec2_query(
                el, "PortRange"
            )
        )
    return out
