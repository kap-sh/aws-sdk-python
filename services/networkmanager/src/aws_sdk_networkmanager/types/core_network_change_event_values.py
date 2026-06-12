"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkChangeEventValues``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_id
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.external_region_code
    import aws_sdk_networkmanager.types.routing_policy_association_details_list
    import aws_sdk_networkmanager.types.routing_policy_direction


class CoreNetworkChangeEventValues(TypedDict):
    edge_location: NotRequired[
        "aws_sdk_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The edge location for the core network change event.</p>"""
    peer_edge_location: NotRequired[
        "aws_sdk_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The edge location of the peer in a core network change event.</p>"""
    routing_policy_direction: NotRequired[
        "aws_sdk_networkmanager.types.routing_policy_direction.RoutingPolicyDirection"
    ]
    """<p>The routing policy direction (inbound/outbound) in a core network change event.</p>"""
    segment_name: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The segment name if the change event is associated with a segment.</p>"""
    network_function_group_name: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The changed network function group name.</p>"""
    attachment_id: NotRequired[
        "aws_sdk_networkmanager.types.attachment_id.AttachmentId"
    ]
    """<p>The ID of the attachment if the change event is associated with an attachment. </p>"""
    cidr: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>For a <code>STATIC_ROUTE</code> event, this is the IP address.</p>"""
    routing_policy_association_details: NotRequired[
        "aws_sdk_networkmanager.types.routing_policy_association_details_list.RoutingPolicyAssociationDetailsList"
    ]
    """<p>The names of the routing policies and other association details in the core network change values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkChangeEventValues) -> dict:
    out: dict = {}
    if "edge_location" in value:
        out["EdgeLocation"] = value["edge_location"]
    if "peer_edge_location" in value:
        out["PeerEdgeLocation"] = value["peer_edge_location"]
    if "routing_policy_direction" in value:
        import aws_sdk_networkmanager.types.routing_policy_direction

        out["RoutingPolicyDirection"] = (
            aws_sdk_networkmanager.types.routing_policy_direction.serialize_json(
                value["routing_policy_direction"]
            )
        )
    if "segment_name" in value:
        out["SegmentName"] = value["segment_name"]
    if "network_function_group_name" in value:
        out["NetworkFunctionGroupName"] = value["network_function_group_name"]
    if "attachment_id" in value:
        out["AttachmentId"] = value["attachment_id"]
    if "cidr" in value:
        out["Cidr"] = value["cidr"]
    if "routing_policy_association_details" in value:
        import aws_sdk_networkmanager.types.routing_policy_association_details_list

        out["RoutingPolicyAssociationDetails"] = (
            aws_sdk_networkmanager.types.routing_policy_association_details_list.serialize_json(
                value["routing_policy_association_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoreNetworkChangeEventValues:
    out: CoreNetworkChangeEventValues = {}  # type: ignore[typeddict-item]
    if "EdgeLocation" in data:
        out["edge_location"] = data["EdgeLocation"]
    if "PeerEdgeLocation" in data:
        out["peer_edge_location"] = data["PeerEdgeLocation"]
    if "RoutingPolicyDirection" in data:
        import aws_sdk_networkmanager.types.routing_policy_direction

        out["routing_policy_direction"] = (
            aws_sdk_networkmanager.types.routing_policy_direction.deserialize_json(
                data["RoutingPolicyDirection"]
            )
        )
    if "SegmentName" in data:
        out["segment_name"] = data["SegmentName"]
    if "NetworkFunctionGroupName" in data:
        out["network_function_group_name"] = data["NetworkFunctionGroupName"]
    if "AttachmentId" in data:
        out["attachment_id"] = data["AttachmentId"]
    if "Cidr" in data:
        out["cidr"] = data["Cidr"]
    if "RoutingPolicyAssociationDetails" in data:
        import aws_sdk_networkmanager.types.routing_policy_association_details_list

        out["routing_policy_association_details"] = (
            aws_sdk_networkmanager.types.routing_policy_association_details_list.deserialize_json(
                data["RoutingPolicyAssociationDetails"]
            )
        )
    return out
