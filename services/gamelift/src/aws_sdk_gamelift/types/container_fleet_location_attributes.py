"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerFleetLocationAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_fleet_location_status
    import aws_sdk_gamelift.types.location_string_model
    import aws_sdk_gamelift.types.player_gateway_status


class ContainerFleetLocationAttributes(TypedDict):
    location: NotRequired[
        "aws_sdk_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>A location identifier.</p>"""
    status: NotRequired[
        "aws_sdk_gamelift.types.container_fleet_location_status.ContainerFleetLocationStatus"
    ]
    """<p>The status of fleet activity in the location. </p> <ul> <li> <p> <code>PENDING</code> -- A new container fleet has been requested.</p> </li> <li> <p> <code>CREATING</code> -- A new container fleet resource is being created. </p> </li> <li> <p> <code>CREATED</code> -- A new container fleet resource has been created. No fleet instances have been deployed.</p> </li> <li> <p> <code>ACTIVATING</code> -- New container fleet instances are being deployed.</p> </li> <li> <p> <code>ACTIVE</code> -- The container fleet has been deployed and is ready to host game sessions.</p> </li> <li> <p> <code>UPDATING</code> -- Updates to the container fleet is being updated. A deployment is in progress.</p> </li> </ul>"""
    player_gateway_status: NotRequired[
        "aws_sdk_gamelift.types.player_gateway_status.PlayerGatewayStatus"
    ]
    r"""<p>The current status of player gateway in this location for this container fleet. Note, even if a container fleet has PlayerGatewayMode configured as <code>ENABLED</code>, player gateway might not be available in a specific location. For more information about locations where player gateway is supported, see <a href=\"https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html\">Amazon GameLift Servers service locations</a>.</p> <p>Possible values include:</p> <ul> <li> <p> <code>ENABLED</code> -- Player gateway is available for this container fleet location.</p> </li> <li> <p> <code>DISABLED</code> -- Player gateway is not available for this container fleet location.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerFleetLocationAttributes) -> dict:
    out: dict = {}
    if "location" in value:
        out["Location"] = value["location"]
    if "status" in value:
        import aws_sdk_gamelift.types.container_fleet_location_status

        out["Status"] = (
            aws_sdk_gamelift.types.container_fleet_location_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "player_gateway_status" in value:
        import aws_sdk_gamelift.types.player_gateway_status

        out["PlayerGatewayStatus"] = (
            aws_sdk_gamelift.types.player_gateway_status.serialize_aws_json_1_1(
                value["player_gateway_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerFleetLocationAttributes:
    out: ContainerFleetLocationAttributes = {}  # type: ignore[typeddict-item]
    if "Location" in data:
        out["location"] = data["Location"]
    if "Status" in data:
        import aws_sdk_gamelift.types.container_fleet_location_status

        out["status"] = (
            aws_sdk_gamelift.types.container_fleet_location_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "PlayerGatewayStatus" in data:
        import aws_sdk_gamelift.types.player_gateway_status

        out["player_gateway_status"] = (
            aws_sdk_gamelift.types.player_gateway_status.deserialize_aws_json_1_1(
                data["PlayerGatewayStatus"]
            )
        )
    return out
