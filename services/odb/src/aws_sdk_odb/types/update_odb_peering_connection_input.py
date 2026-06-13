"""Generated from Smithy shape ``com.amazonaws.odb#UpdateOdbPeeringConnectionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_odb.types.peered_cidr_list
    import aws_sdk_odb.types.resource_display_name
    import aws_sdk_odb.types.resource_id_or_arn


class UpdateOdbPeeringConnectionInput(TypedDict):
    odb_peering_connection_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The identifier of the Oracle Database@Amazon Web Services peering connection to update.</p>"""
    display_name: NotRequired[
        "aws_sdk_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>A new display name for the peering connection.</p>"""
    peer_network_cidrs_to_be_added: NotRequired[
        "aws_sdk_odb.types.peered_cidr_list.PeeredCidrList"
    ]
    """<p>A list of CIDR blocks to add to the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection. The CIDR blocks must not overlap with existing CIDR blocks in the Oracle Database@Amazon Web Services network.</p>"""
    peer_network_cidrs_to_be_removed: NotRequired[
        "aws_sdk_odb.types.peered_cidr_list.PeeredCidrList"
    ]
    """<p>A list of CIDR blocks to remove from the peering connection. The CIDR blocks must currently exist in the peering connection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateOdbPeeringConnectionInput) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "peer_network_cidrs_to_be_added" in value:
        import aws_sdk_odb.types.peered_cidr_list

        out["peerNetworkCidrsToBeAdded"] = (
            aws_sdk_odb.types.peered_cidr_list.serialize_aws_json_1_0(
                value["peer_network_cidrs_to_be_added"]
            )
        )
    if "peer_network_cidrs_to_be_removed" in value:
        import aws_sdk_odb.types.peered_cidr_list

        out["peerNetworkCidrsToBeRemoved"] = (
            aws_sdk_odb.types.peered_cidr_list.serialize_aws_json_1_0(
                value["peer_network_cidrs_to_be_removed"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateOdbPeeringConnectionInput:
    out: UpdateOdbPeeringConnectionInput = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "peerNetworkCidrsToBeAdded" in data:
        import aws_sdk_odb.types.peered_cidr_list

        out["peer_network_cidrs_to_be_added"] = (
            aws_sdk_odb.types.peered_cidr_list.deserialize_aws_json_1_0(
                data["peerNetworkCidrsToBeAdded"]
            )
        )
    if "peerNetworkCidrsToBeRemoved" in data:
        import aws_sdk_odb.types.peered_cidr_list

        out["peer_network_cidrs_to_be_removed"] = (
            aws_sdk_odb.types.peered_cidr_list.deserialize_aws_json_1_0(
                data["peerNetworkCidrsToBeRemoved"]
            )
        )
    return out
