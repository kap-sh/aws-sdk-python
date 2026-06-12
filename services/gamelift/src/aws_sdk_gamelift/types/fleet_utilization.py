"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetUtilization``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_arn
    import aws_sdk_gamelift.types.fleet_id
    import aws_sdk_gamelift.types.location_string_model
    import aws_sdk_gamelift.types.whole_number


class FleetUtilization(TypedDict):
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet associated with the location.</p>"""
    fleet_arn: NotRequired["aws_sdk_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html\">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    active_server_process_count: NotRequired[
        "aws_sdk_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The number of server processes in <code>ACTIVE</code> status that are currently running across all instances in the fleet location. </p>"""
    active_game_session_count: NotRequired[
        "aws_sdk_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The number of active game sessions that are currently being hosted across all instances in the fleet location.</p>"""
    current_player_session_count: NotRequired[
        "aws_sdk_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The number of active player sessions that are currently being hosted across all instances in the fleet location.</p>"""
    maximum_player_session_count: NotRequired[
        "aws_sdk_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The maximum number of players allowed across all game sessions that are currently being hosted across all instances in the fleet location.</p>"""
    location: NotRequired[
        "aws_sdk_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The fleet location for the fleet utilization information, expressed as an Amazon Web Services Region code, such as <code>us-west-2</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetUtilization) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "active_server_process_count" in value:
        out["ActiveServerProcessCount"] = value["active_server_process_count"]
    if "active_game_session_count" in value:
        out["ActiveGameSessionCount"] = value["active_game_session_count"]
    if "current_player_session_count" in value:
        out["CurrentPlayerSessionCount"] = value["current_player_session_count"]
    if "maximum_player_session_count" in value:
        out["MaximumPlayerSessionCount"] = value["maximum_player_session_count"]
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FleetUtilization:
    out: FleetUtilization = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "FleetArn" in data:
        out["fleet_arn"] = data["FleetArn"]
    if "ActiveServerProcessCount" in data:
        out["active_server_process_count"] = data["ActiveServerProcessCount"]
    if "ActiveGameSessionCount" in data:
        out["active_game_session_count"] = data["ActiveGameSessionCount"]
    if "CurrentPlayerSessionCount" in data:
        out["current_player_session_count"] = data["CurrentPlayerSessionCount"]
    if "MaximumPlayerSessionCount" in data:
        out["maximum_player_session_count"] = data["MaximumPlayerSessionCount"]
    if "Location" in data:
        out["location"] = data["Location"]
    return out
