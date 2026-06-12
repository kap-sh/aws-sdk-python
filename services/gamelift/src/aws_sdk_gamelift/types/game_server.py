"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server_claim_status
    import aws_sdk_gamelift.types.game_server_connection_info
    import aws_sdk_gamelift.types.game_server_data
    import aws_sdk_gamelift.types.game_server_group_arn
    import aws_sdk_gamelift.types.game_server_group_name
    import aws_sdk_gamelift.types.game_server_id
    import aws_sdk_gamelift.types.game_server_instance_id
    import aws_sdk_gamelift.types.game_server_utilization_status
    import aws_sdk_gamelift.types.timestamp


class GameServer(TypedDict):
    game_server_group_name: NotRequired[
        "aws_sdk_gamelift.types.game_server_group_name.GameServerGroupName"
    ]
    """<p>A unique identifier for the game server group where the game server is running.</p>"""
    game_server_group_arn: NotRequired[
        "aws_sdk_gamelift.types.game_server_group_arn.GameServerGroupArn"
    ]
    """<p>The ARN identifier for the game server group where the game server is located.</p>"""
    game_server_id: NotRequired["aws_sdk_gamelift.types.game_server_id.GameServerId"]
    """<p>A custom string that uniquely identifies the game server. Game server IDs are developer-defined and are unique across all game server groups in an Amazon Web Services account.</p>"""
    instance_id: NotRequired[
        "aws_sdk_gamelift.types.game_server_instance_id.GameServerInstanceId"
    ]
    """<p>The unique identifier for the instance where the game server is running. This ID is available in the instance metadata. EC2 instance IDs use a 17-character format, for example: <code>i-1234567890abcdef0</code>.</p>"""
    connection_info: NotRequired[
        "aws_sdk_gamelift.types.game_server_connection_info.GameServerConnectionInfo"
    ]
    """<p>The port and IP address that must be used to establish a client connection to the game server.</p>"""
    game_server_data: NotRequired[
        "aws_sdk_gamelift.types.game_server_data.GameServerData"
    ]
    """<p>A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on game servers.</p>"""
    claim_status: NotRequired[
        "aws_sdk_gamelift.types.game_server_claim_status.GameServerClaimStatus"
    ]
    """<p>Indicates when an available game server has been reserved for gameplay but has not yet started hosting a game. Once it is claimed, the game server remains in <code>CLAIMED</code> status for a maximum of one minute. During this time, game clients connect to the game server to start the game and trigger the game server to update its utilization status. After one minute, the game server claim status reverts to null.</p>"""
    utilization_status: NotRequired[
        "aws_sdk_gamelift.types.game_server_utilization_status.GameServerUtilizationStatus"
    ]
    """<p>Indicates whether the game server is currently available for new games or is busy. Possible statuses include:</p> <ul> <li> <p> <code>AVAILABLE</code> - The game server is available to be claimed. A game server that has been claimed remains in this status until it reports game hosting activity. </p> </li> <li> <p> <code>UTILIZED</code> - The game server is currently hosting a game session with players. </p> </li> </ul>"""
    registration_time: NotRequired["aws_sdk_gamelift.types.timestamp.Timestamp"]
    """<p>Timestamp that indicates when the game server registered. The format is a number expressed in Unix time as milliseconds (for example <code>\"1469498468.057\"</code>).</p>"""
    last_claim_time: NotRequired["aws_sdk_gamelift.types.timestamp.Timestamp"]
    """<p>Timestamp that indicates the last time the game server was claimed. The format is a number expressed in Unix time as milliseconds (for example <code>\"1469498468.057\"</code>). This value is used to calculate when a claimed game server's status should revert to null.</p>"""
    last_health_check_time: NotRequired["aws_sdk_gamelift.types.timestamp.Timestamp"]
    """<p>Timestamp that indicates the last time the game server was updated with health status. The format is a number expressed in Unix time as milliseconds (for example <code>\"1469498468.057\"</code>). After game server registration, this property is only changed when a game server update specifies a health check value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServer) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "game_server_group_arn" in value:
        out["GameServerGroupArn"] = value["game_server_group_arn"]
    if "game_server_id" in value:
        out["GameServerId"] = value["game_server_id"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "connection_info" in value:
        out["ConnectionInfo"] = value["connection_info"]
    if "game_server_data" in value:
        out["GameServerData"] = value["game_server_data"]
    if "claim_status" in value:
        import aws_sdk_gamelift.types.game_server_claim_status

        out["ClaimStatus"] = (
            aws_sdk_gamelift.types.game_server_claim_status.serialize_aws_json_1_1(
                value["claim_status"]
            )
        )
    if "utilization_status" in value:
        import aws_sdk_gamelift.types.game_server_utilization_status

        out["UtilizationStatus"] = (
            aws_sdk_gamelift.types.game_server_utilization_status.serialize_aws_json_1_1(
                value["utilization_status"]
            )
        )
    if "registration_time" in value:
        import aws_sdk_gamelift.types.timestamp

        out["RegistrationTime"] = (
            aws_sdk_gamelift.types.timestamp.serialize_aws_json_1_1(
                value["registration_time"]
            )
        )
    if "last_claim_time" in value:
        import aws_sdk_gamelift.types.timestamp

        out["LastClaimTime"] = aws_sdk_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["last_claim_time"]
        )
    if "last_health_check_time" in value:
        import aws_sdk_gamelift.types.timestamp

        out["LastHealthCheckTime"] = (
            aws_sdk_gamelift.types.timestamp.serialize_aws_json_1_1(
                value["last_health_check_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GameServer:
    out: GameServer = {}  # type: ignore[typeddict-item]
    if "GameServerGroupName" in data:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if "GameServerGroupArn" in data:
        out["game_server_group_arn"] = data["GameServerGroupArn"]
    if "GameServerId" in data:
        out["game_server_id"] = data["GameServerId"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "ConnectionInfo" in data:
        out["connection_info"] = data["ConnectionInfo"]
    if "GameServerData" in data:
        out["game_server_data"] = data["GameServerData"]
    if "ClaimStatus" in data:
        import aws_sdk_gamelift.types.game_server_claim_status

        out["claim_status"] = (
            aws_sdk_gamelift.types.game_server_claim_status.deserialize_aws_json_1_1(
                data["ClaimStatus"]
            )
        )
    if "UtilizationStatus" in data:
        import aws_sdk_gamelift.types.game_server_utilization_status

        out["utilization_status"] = (
            aws_sdk_gamelift.types.game_server_utilization_status.deserialize_aws_json_1_1(
                data["UtilizationStatus"]
            )
        )
    if "RegistrationTime" in data:
        import aws_sdk_gamelift.types.timestamp

        out["registration_time"] = (
            aws_sdk_gamelift.types.timestamp.deserialize_aws_json_1_1(
                data["RegistrationTime"]
            )
        )
    if "LastClaimTime" in data:
        import aws_sdk_gamelift.types.timestamp

        out["last_claim_time"] = (
            aws_sdk_gamelift.types.timestamp.deserialize_aws_json_1_1(
                data["LastClaimTime"]
            )
        )
    if "LastHealthCheckTime" in data:
        import aws_sdk_gamelift.types.timestamp

        out["last_health_check_time"] = (
            aws_sdk_gamelift.types.timestamp.deserialize_aws_json_1_1(
                data["LastHealthCheckTime"]
            )
        )
    return out
