"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteFleetLocationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_arn
    import aws_sdk_gamelift.types.fleet_id_or_arn
    import aws_sdk_gamelift.types.location_state_list


class DeleteFleetLocationsOutput(TypedDict):
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet that location attributes are being deleted for.</p>"""
    fleet_arn: NotRequired["aws_sdk_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html\">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    location_states: NotRequired[
        "aws_sdk_gamelift.types.location_state_list.LocationStateList"
    ]
    """<p>The remote locations that are being deleted, with each location status set to <code>DELETING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFleetLocationsOutput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "location_states" in value:
        import aws_sdk_gamelift.types.location_state_list

        out["LocationStates"] = (
            aws_sdk_gamelift.types.location_state_list.serialize_aws_json_1_1(
                value["location_states"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFleetLocationsOutput:
    out: DeleteFleetLocationsOutput = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "FleetArn" in data:
        out["fleet_arn"] = data["FleetArn"]
    if "LocationStates" in data:
        import aws_sdk_gamelift.types.location_state_list

        out["location_states"] = (
            aws_sdk_gamelift.types.location_state_list.deserialize_aws_json_1_1(
                data["LocationStates"]
            )
        )
    return out
