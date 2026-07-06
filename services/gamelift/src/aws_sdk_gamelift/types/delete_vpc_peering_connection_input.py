"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteVpcPeeringConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_id
    import aws_sdk_gamelift.types.non_zero_and_max_string


class DeleteVpcPeeringConnectionInput(TypedDict, closed=True):
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet. This fleet specified must match the fleet referenced in the VPC peering connection record. You can use either the fleet ID or ARN value.</p>"""
    vpc_peering_connection_id: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A unique identifier for a VPC peering connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteVpcPeeringConnectionInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "vpc_peering_connection_id" in value:
        out["VpcPeeringConnectionId"] = value["vpc_peering_connection_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteVpcPeeringConnectionInput:
    out: DeleteVpcPeeringConnectionInput = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "VpcPeeringConnectionId" in data:
        out["vpc_peering_connection_id"] = data["VpcPeeringConnectionId"]
    return out
