"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_interface_id
    import capo_ec2.types.route_server_endpoint_id
    import capo_ec2.types.route_server_endpoint_state
    import capo_ec2.types.route_server_id
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id
    import capo_ec2.types.tag_list
    import capo_ec2.types.vpc_id


class RouteServerEndpoint(TypedDict, closed=True):
    route_server_id: NotRequired["capo_ec2.types.route_server_id.RouteServerId"]
    """<p>The ID of the route server associated with this endpoint.</p>"""
    route_server_endpoint_id: NotRequired[
        "capo_ec2.types.route_server_endpoint_id.RouteServerEndpointId"
    ]
    """<p>The unique identifier of the route server endpoint.</p>"""
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC containing the endpoint.</p>"""
    subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet to place the route server endpoint into.</p>"""
    eni_id: NotRequired["capo_ec2.types.network_interface_id.NetworkInterfaceId"]
    """<p>The ID of the Elastic network interface for the endpoint.</p>"""
    eni_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address of the Elastic network interface for the endpoint.</p>"""
    state: NotRequired[
        "capo_ec2.types.route_server_endpoint_state.RouteServerEndpointState"
    ]
    """<p>The current state of the route server endpoint.</p>"""
    failure_reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason for any failure in endpoint creation or operation.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the route server endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerEndpoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route_server_id" in value:
        pairs.append((f"{prefix}.RouteServerId", str(value["route_server_id"])))
    if "route_server_endpoint_id" in value:
        pairs.append(
            (f"{prefix}.RouteServerEndpointId", str(value["route_server_endpoint_id"]))
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "eni_id" in value:
        pairs.append((f"{prefix}.EniId", str(value["eni_id"])))
    if "eni_address" in value:
        pairs.append((f"{prefix}.EniAddress", str(value["eni_address"])))
    if "state" in value:
        import capo_ec2.types.route_server_endpoint_state

        capo_ec2.types.route_server_endpoint_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "failure_reason" in value:
        pairs.append((f"{prefix}.FailureReason", str(value["failure_reason"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> RouteServerEndpoint:
    out: RouteServerEndpoint = {}  # type: ignore[typeddict-item]
    child_route_server_id = el.find("RouteServerId")
    if child_route_server_id is not None:
        out["route_server_id"] = str(child_route_server_id.text or "")
    child_route_server_endpoint_id = el.find("RouteServerEndpointId")
    if child_route_server_endpoint_id is not None:
        out["route_server_endpoint_id"] = str(child_route_server_endpoint_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_eni_id = el.find("EniId")
    if child_eni_id is not None:
        out["eni_id"] = str(child_eni_id.text or "")
    child_eni_address = el.find("EniAddress")
    if child_eni_address is not None:
        out["eni_address"] = str(child_eni_address.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.route_server_endpoint_state

        out["state"] = capo_ec2.types.route_server_endpoint_state.deserialize_ec2_query(
            child_state
        )
    child_failure_reason = el.find("FailureReason")
    if child_failure_reason is not None:
        out["failure_reason"] = str(child_failure_reason.text or "")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
