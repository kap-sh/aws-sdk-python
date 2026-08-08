"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.traffic_mirror_target_type


class TrafficMirrorTarget(TypedDict, closed=True):
    traffic_mirror_target_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror target.</p>"""
    network_interface_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The network interface ID that is attached to the target.</p>"""
    network_load_balancer_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Network Load Balancer.</p>"""
    type: NotRequired[
        "capo_ec2.types.traffic_mirror_target_type.TrafficMirrorTargetType"
    ]
    """<p>The type of Traffic Mirror target.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>Information about the Traffic Mirror target.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the account that owns the Traffic Mirror target.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the Traffic Mirror target.</p>"""
    gateway_load_balancer_endpoint_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Gateway Load Balancer endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrafficMirrorTarget, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "traffic_mirror_target_id" in value:
        pairs.append(
            (
                f"{key_prefix}TrafficMirrorTargetId",
                str(value["traffic_mirror_target_id"]),
            )
        )
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "network_load_balancer_arn" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkLoadBalancerArn",
                str(value["network_load_balancer_arn"]),
            )
        )
    if "type" in value:
        import capo_ec2.types.traffic_mirror_target_type

        capo_ec2.types.traffic_mirror_target_type.serialize_ec2_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "gateway_load_balancer_endpoint_id" in value:
        pairs.append(
            (
                f"{key_prefix}GatewayLoadBalancerEndpointId",
                str(value["gateway_load_balancer_endpoint_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> TrafficMirrorTarget:
    out: TrafficMirrorTarget = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_target_id = el.find("trafficMirrorTargetId")
    if child_traffic_mirror_target_id is not None:
        out["traffic_mirror_target_id"] = str(child_traffic_mirror_target_id.text or "")
    child_network_interface_id = el.find("networkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_network_load_balancer_arn = el.find("networkLoadBalancerArn")
    if child_network_load_balancer_arn is not None:
        out["network_load_balancer_arn"] = str(
            child_network_load_balancer_arn.text or ""
        )
    child_type = el.find("type")
    if child_type is not None:
        import capo_ec2.types.traffic_mirror_target_type

        out["type"] = capo_ec2.types.traffic_mirror_target_type.deserialize_ec2_query(
            child_type
        )
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    child_gateway_load_balancer_endpoint_id = el.find("gatewayLoadBalancerEndpointId")
    if child_gateway_load_balancer_endpoint_id is not None:
        out["gateway_load_balancer_endpoint_id"] = str(
            child_gateway_load_balancer_endpoint_id.text or ""
        )
    return out
