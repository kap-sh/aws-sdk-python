"""Generated from Smithy shape ``com.amazonaws.gamelift#RegisterGameServerInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server_connection_info
    import aws_sdk_gamelift.types.game_server_data
    import aws_sdk_gamelift.types.game_server_group_name_or_arn
    import aws_sdk_gamelift.types.game_server_id
    import aws_sdk_gamelift.types.game_server_instance_id


class RegisterGameServerInput(TypedDict):
    game_server_group_name: NotRequired[
        "aws_sdk_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
    ]
    """<p>A unique identifier for the game server group where the game server is running.</p>"""
    game_server_id: NotRequired["aws_sdk_gamelift.types.game_server_id.GameServerId"]
    """<p>A custom string that uniquely identifies the game server to register. Game server IDs are developer-defined and must be unique across all game server groups in your Amazon Web Services account.</p>"""
    instance_id: NotRequired[
        "aws_sdk_gamelift.types.game_server_instance_id.GameServerInstanceId"
    ]
    """<p>The unique identifier for the instance where the game server is running. This ID is available in the instance metadata. EC2 instance IDs use a 17-character format, for example: <code>i-1234567890abcdef0</code>.</p>"""
    connection_info: NotRequired[
        "aws_sdk_gamelift.types.game_server_connection_info.GameServerConnectionInfo"
    ]
    """<p>Information that is needed to make inbound client connections to the game server. This might include the IP address and port, DNS name, and other information.</p>"""
    game_server_data: NotRequired[
        "aws_sdk_gamelift.types.game_server_data.GameServerData"
    ]
    """<p>A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on game servers. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterGameServerInput) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "game_server_id" in value:
        out["GameServerId"] = value["game_server_id"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "connection_info" in value:
        out["ConnectionInfo"] = value["connection_info"]
    if "game_server_data" in value:
        out["GameServerData"] = value["game_server_data"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterGameServerInput:
    out: RegisterGameServerInput = {}  # type: ignore[typeddict-item]
    if "GameServerGroupName" in data:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if "GameServerId" in data:
        out["game_server_id"] = data["GameServerId"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "ConnectionInfo" in data:
        out["connection_info"] = data["ConnectionInfo"]
    if "GameServerData" in data:
        out["game_server_data"] = data["GameServerData"]
    return out
