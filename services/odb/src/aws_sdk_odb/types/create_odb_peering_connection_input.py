"""Generated from Smithy shape ``com.amazonaws.odb#CreateOdbPeeringConnectionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.general_input_string
    import aws_sdk_odb.types.peer_network_route_table_id_list
    import aws_sdk_odb.types.peered_cidr_list
    import aws_sdk_odb.types.request_tag_map
    import aws_sdk_odb.types.resource_display_name
    import aws_sdk_odb.types.resource_id_or_arn


class CreateOdbPeeringConnectionInput(TypedDict):
    odb_network_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the ODB network that initiates the peering connection.</p>"""
    peer_network_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the peer network. This can be either a VPC ID or another ODB network ID.</p>"""
    display_name: NotRequired[
        "aws_sdk_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>The display name for the ODB peering connection.</p>"""
    peer_network_cidrs_to_be_added: NotRequired[
        "aws_sdk_odb.types.peered_cidr_list.PeeredCidrList"
    ]
    """<p>A list of CIDR blocks to add to the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection.</p>"""
    peer_network_route_table_ids: NotRequired[
        "aws_sdk_odb.types.peer_network_route_table_id_list.PeerNetworkRouteTableIdList"
    ]
    """<p>The unique identifier of the VPC route table for which a route to the ODB network is automatically created during peering connection establishment.</p>"""
    client_token: NotRequired[
        "aws_sdk_odb.types.general_input_string.GeneralInputString"
    ]
    """<p>The client token for the ODB peering connection request.</p> <p>Constraints:</p> <ul> <li> <p>Must be unique for each request.</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_odb.types.request_tag_map.RequestTagMap"]
    """<p>The tags to assign to the ODB peering connection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateOdbPeeringConnectionInput) -> dict:
    out: dict = {}
    out["odbNetworkId"] = value["odb_network_id"]
    out["peerNetworkId"] = value["peer_network_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "peer_network_cidrs_to_be_added" in value:
        import aws_sdk_odb.types.peered_cidr_list

        out["peerNetworkCidrsToBeAdded"] = (
            aws_sdk_odb.types.peered_cidr_list.serialize_aws_json_1_0(
                value["peer_network_cidrs_to_be_added"]
            )
        )
    if "peer_network_route_table_ids" in value:
        import aws_sdk_odb.types.peer_network_route_table_id_list

        out["peerNetworkRouteTableIds"] = (
            aws_sdk_odb.types.peer_network_route_table_id_list.serialize_aws_json_1_0(
                value["peer_network_route_table_ids"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_odb.types.request_tag_map

        out["tags"] = aws_sdk_odb.types.request_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateOdbPeeringConnectionInput:
    out: CreateOdbPeeringConnectionInput = {}  # type: ignore[typeddict-item]
    if "odbNetworkId" in data:
        out["odb_network_id"] = data["odbNetworkId"]
    else:
        raise DeserializationError(
            "CreateOdbPeeringConnectionInput.odb_network_id required"
        )
    if "peerNetworkId" in data:
        out["peer_network_id"] = data["peerNetworkId"]
    else:
        raise DeserializationError(
            "CreateOdbPeeringConnectionInput.peer_network_id required"
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "peerNetworkCidrsToBeAdded" in data:
        import aws_sdk_odb.types.peered_cidr_list

        out["peer_network_cidrs_to_be_added"] = (
            aws_sdk_odb.types.peered_cidr_list.deserialize_aws_json_1_0(
                data["peerNetworkCidrsToBeAdded"]
            )
        )
    if "peerNetworkRouteTableIds" in data:
        import aws_sdk_odb.types.peer_network_route_table_id_list

        out["peer_network_route_table_ids"] = (
            aws_sdk_odb.types.peer_network_route_table_id_list.deserialize_aws_json_1_0(
                data["peerNetworkRouteTableIds"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_odb.types.request_tag_map

        out["tags"] = aws_sdk_odb.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
