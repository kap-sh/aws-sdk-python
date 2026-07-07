"""Generated from Smithy shape ``com.amazonaws.odb#OdbPeeringConnectionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_odb.types.peered_cidr_list
    import aws_sdk_odb.types.resource_id_or_arn
    import aws_sdk_odb.types.resource_status


class OdbPeeringConnectionSummary(TypedDict, closed=True):
    odb_peering_connection_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the ODB peering connection. A sample ID is <code>odbpcx-abcdefgh12345678</code>.</p>"""
    display_name: NotRequired["str"]
    """<p>The display name of the ODB peering connection.</p>"""
    status: NotRequired["aws_sdk_odb.types.resource_status.ResourceStatus"]
    """<p>The status of the ODB peering connection.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current status of the ODB peering connection.</p>"""
    odb_peering_connection_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the ODB peering connection.</p>"""
    odb_network_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the ODB network that initiated the peering connection.</p>"""
    peer_network_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the peer network.</p>"""
    odb_peering_connection_type: NotRequired["str"]
    """<p>The type of the ODB peering connection.</p> <p>Valid Values: <code>ODB-VPC | ODB-ODB</code> </p>"""
    peer_network_cidrs: NotRequired["aws_sdk_odb.types.peered_cidr_list.PeeredCidrList"]
    """<p>The CIDR blocks associated with the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the ODB peering connection was created.</p>"""
    percent_progress: NotRequired["float"]
    """<p>The percentage progress of the ODB peering connection creation or deletion.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OdbPeeringConnectionSummary) -> dict:
    out: dict = {}
    out["odbPeeringConnectionId"] = value["odb_peering_connection_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import aws_sdk_odb.types.resource_status

        out["status"] = aws_sdk_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "odb_peering_connection_arn" in value:
        out["odbPeeringConnectionArn"] = value["odb_peering_connection_arn"]
    if "odb_network_arn" in value:
        out["odbNetworkArn"] = value["odb_network_arn"]
    if "peer_network_arn" in value:
        out["peerNetworkArn"] = value["peer_network_arn"]
    if "odb_peering_connection_type" in value:
        out["odbPeeringConnectionType"] = value["odb_peering_connection_type"]
    if "peer_network_cidrs" in value:
        import aws_sdk_odb.types.peered_cidr_list

        out["peerNetworkCidrs"] = (
            aws_sdk_odb.types.peered_cidr_list.serialize_aws_json_1_0(
                value["peer_network_cidrs"]
            )
        )
    if "created_at" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["createdAt"] = aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "percent_progress" in value:
        out["percentProgress"] = value["percent_progress"]
    return out


def deserialize_aws_json_1_0(data: dict) -> OdbPeeringConnectionSummary:
    out: OdbPeeringConnectionSummary = {}  # type: ignore[typeddict-item]
    if "odbPeeringConnectionId" in data:
        out["odb_peering_connection_id"] = data["odbPeeringConnectionId"]
    else:
        raise DeserializationError(
            "OdbPeeringConnectionSummary.odb_peering_connection_id required"
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "status" in data:
        import aws_sdk_odb.types.resource_status

        out["status"] = aws_sdk_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "odbPeeringConnectionArn" in data:
        out["odb_peering_connection_arn"] = data["odbPeeringConnectionArn"]
    if "odbNetworkArn" in data:
        out["odb_network_arn"] = data["odbNetworkArn"]
    if "peerNetworkArn" in data:
        out["peer_network_arn"] = data["peerNetworkArn"]
    if "odbPeeringConnectionType" in data:
        out["odb_peering_connection_type"] = data["odbPeeringConnectionType"]
    if "peerNetworkCidrs" in data:
        import aws_sdk_odb.types.peered_cidr_list

        out["peer_network_cidrs"] = (
            aws_sdk_odb.types.peered_cidr_list.deserialize_aws_json_1_0(
                data["peerNetworkCidrs"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "percentProgress" in data:
        out["percent_progress"] = data["percentProgress"]
    return out
