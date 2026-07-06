"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server_group_arn
    import aws_sdk_gamelift.types.game_server_group_name
    import aws_sdk_gamelift.types.game_server_instance_id
    import aws_sdk_gamelift.types.game_server_instance_status


class GameServerInstance(TypedDict, closed=True):
    game_server_group_name: NotRequired[
        "aws_sdk_gamelift.types.game_server_group_name.GameServerGroupName"
    ]
    """<p>A developer-defined identifier for the game server group that includes the game server instance. The name is unique for each Region in each Amazon Web Services account.</p>"""
    game_server_group_arn: NotRequired[
        "aws_sdk_gamelift.types.game_server_group_arn.GameServerGroupArn"
    ]
    """<p>A generated unique identifier for the game server group that includes the game server instance. </p>"""
    instance_id: NotRequired[
        "aws_sdk_gamelift.types.game_server_instance_id.GameServerInstanceId"
    ]
    """<p>The unique identifier for the instance where the game server is running. This ID is available in the instance metadata. EC2 instance IDs use a 17-character format, for example: <code>i-1234567890abcdef0</code>.</p>"""
    instance_status: NotRequired[
        "aws_sdk_gamelift.types.game_server_instance_status.GameServerInstanceStatus"
    ]
    """<p>Current status of the game server instance</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerInstance) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "game_server_group_arn" in value:
        out["GameServerGroupArn"] = value["game_server_group_arn"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "instance_status" in value:
        import aws_sdk_gamelift.types.game_server_instance_status

        out["InstanceStatus"] = (
            aws_sdk_gamelift.types.game_server_instance_status.serialize_aws_json_1_1(
                value["instance_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GameServerInstance:
    out: GameServerInstance = {}  # type: ignore[typeddict-item]
    if "GameServerGroupName" in data:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if "GameServerGroupArn" in data:
        out["game_server_group_arn"] = data["GameServerGroupArn"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "InstanceStatus" in data:
        import aws_sdk_gamelift.types.game_server_instance_status

        out["instance_status"] = (
            aws_sdk_gamelift.types.game_server_instance_status.deserialize_aws_json_1_1(
                data["InstanceStatus"]
            )
        )
    return out
