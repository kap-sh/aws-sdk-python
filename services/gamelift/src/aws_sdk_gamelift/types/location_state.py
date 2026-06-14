"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_status
    import aws_sdk_gamelift.types.location_string_model
    import aws_sdk_gamelift.types.player_gateway_status


class LocationState(TypedDict):
    location: NotRequired[
        "aws_sdk_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The fleet location, expressed as an Amazon Web Services Region code such as <code>us-west-2</code>. </p>"""
    status: NotRequired["aws_sdk_gamelift.types.fleet_status.FleetStatus"]
    """<p>The life-cycle status of a fleet location. </p>"""
    player_gateway_status: NotRequired[
        "aws_sdk_gamelift.types.player_gateway_status.PlayerGatewayStatus"
    ]
    r"""<p>The current status of player gateway in this location for this fleet. Note, even if a fleet has PlayerGatewayMode configured as <code>ENABLED</code>, player gateway might not be available in a specific location. For more information about locations where player gateway is supported, see <a href=\"https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html\">Amazon GameLift Servers service locations</a>.</p> <p>Possible values include:</p> <ul> <li> <p> <code>ENABLED</code> -- Player gateway is available for this fleet location.</p> </li> <li> <p> <code>DISABLED</code> -- Player gateway is not available for this fleet location.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationState) -> dict:
    out: dict = {}
    if "location" in value:
        out["Location"] = value["location"]
    if "status" in value:
        import aws_sdk_gamelift.types.fleet_status

        out["Status"] = aws_sdk_gamelift.types.fleet_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "player_gateway_status" in value:
        import aws_sdk_gamelift.types.player_gateway_status

        out["PlayerGatewayStatus"] = (
            aws_sdk_gamelift.types.player_gateway_status.serialize_aws_json_1_1(
                value["player_gateway_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LocationState:
    out: LocationState = {}  # type: ignore[typeddict-item]
    if "Location" in data:
        out["location"] = data["Location"]
    if "Status" in data:
        import aws_sdk_gamelift.types.fleet_status

        out["status"] = aws_sdk_gamelift.types.fleet_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "PlayerGatewayStatus" in data:
        import aws_sdk_gamelift.types.player_gateway_status

        out["player_gateway_status"] = (
            aws_sdk_gamelift.types.player_gateway_status.deserialize_aws_json_1_1(
                data["PlayerGatewayStatus"]
            )
        )
    return out
