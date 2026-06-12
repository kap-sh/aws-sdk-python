"""Generated from Smithy shape ``com.amazonaws.gamelift#DeregisterGameServerInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server_group_name_or_arn
    import aws_sdk_gamelift.types.game_server_id


class DeregisterGameServerInput(TypedDict):
    game_server_group_name: NotRequired[
        "aws_sdk_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
    ]
    """<p>A unique identifier for the game server group where the game server is running.</p>"""
    game_server_id: NotRequired["aws_sdk_gamelift.types.game_server_id.GameServerId"]
    """<p>A custom string that uniquely identifies the game server to deregister.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterGameServerInput) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "game_server_id" in value:
        out["GameServerId"] = value["game_server_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterGameServerInput:
    out: DeregisterGameServerInput = {}  # type: ignore[typeddict-item]
    if "GameServerGroupName" in data:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if "GameServerId" in data:
        out["game_server_id"] = data["GameServerId"]
    return out
