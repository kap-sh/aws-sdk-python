"""Generated from Smithy shape ``com.amazonaws.gamelift#VpcPeeringConnection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_arn
    import aws_sdk_gamelift.types.fleet_id
    import aws_sdk_gamelift.types.non_zero_and_max_string
    import aws_sdk_gamelift.types.vpc_peering_connection_status


class VpcPeeringConnection(TypedDict):
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet. This ID determines the ID of the Amazon GameLift Servers VPC for your fleet.</p>"""
    fleet_arn: NotRequired["aws_sdk_gamelift.types.fleet_arn.FleetArn"]
    r"""<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html\">ARN</a>) associated with the GameLift fleet resource for this connection. </p>"""
    ip_v4_cidr_block: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>CIDR block of IPv4 addresses assigned to the VPC peering connection for the GameLift VPC. The peered VPC also has an IPv4 CIDR block associated with it; these blocks cannot overlap or the peering connection cannot be created. </p>"""
    vpc_peering_connection_id: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A unique identifier that is automatically assigned to the connection record. This ID is referenced in VPC peering connection events, and is used when deleting a connection.</p>"""
    status: NotRequired[
        "aws_sdk_gamelift.types.vpc_peering_connection_status.VpcPeeringConnectionStatus"
    ]
    """<p>The status information about the connection. Status indicates if a connection is pending, successful, or failed.</p>"""
    peer_vpc_id: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    r"""<p>A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the <a href=\"https://console.aws.amazon.com/vpc/\">VPC Dashboard</a> in the Amazon Web Services Management Console. Learn more about VPC peering in <a href=\"https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html\">VPC Peering with Amazon GameLift Servers Fleets</a>.</p>"""
    game_lift_vpc_id: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A unique identifier for the VPC that contains the Amazon GameLift Servers fleet for this connection. This VPC is managed by Amazon GameLift Servers and does not appear in your Amazon Web Services account. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcPeeringConnection) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "ip_v4_cidr_block" in value:
        out["IpV4CidrBlock"] = value["ip_v4_cidr_block"]
    if "vpc_peering_connection_id" in value:
        out["VpcPeeringConnectionId"] = value["vpc_peering_connection_id"]
    if "status" in value:
        import aws_sdk_gamelift.types.vpc_peering_connection_status

        out["Status"] = (
            aws_sdk_gamelift.types.vpc_peering_connection_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "peer_vpc_id" in value:
        out["PeerVpcId"] = value["peer_vpc_id"]
    if "game_lift_vpc_id" in value:
        out["GameLiftVpcId"] = value["game_lift_vpc_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcPeeringConnection:
    out: VpcPeeringConnection = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "FleetArn" in data:
        out["fleet_arn"] = data["FleetArn"]
    if "IpV4CidrBlock" in data:
        out["ip_v4_cidr_block"] = data["IpV4CidrBlock"]
    if "VpcPeeringConnectionId" in data:
        out["vpc_peering_connection_id"] = data["VpcPeeringConnectionId"]
    if "Status" in data:
        import aws_sdk_gamelift.types.vpc_peering_connection_status

        out["status"] = (
            aws_sdk_gamelift.types.vpc_peering_connection_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "PeerVpcId" in data:
        out["peer_vpc_id"] = data["PeerVpcId"]
    if "GameLiftVpcId" in data:
        out["game_lift_vpc_id"] = data["GameLiftVpcId"]
    return out
