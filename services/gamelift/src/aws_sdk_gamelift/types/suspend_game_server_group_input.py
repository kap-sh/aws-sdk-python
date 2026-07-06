"""Generated from Smithy shape ``com.amazonaws.gamelift#SuspendGameServerGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server_group_actions
    import aws_sdk_gamelift.types.game_server_group_name_or_arn


class SuspendGameServerGroupInput(TypedDict, closed=True):
    game_server_group_name: NotRequired[
        "aws_sdk_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
    ]
    """<p>A unique identifier for the game server group. Use either the name or ARN value.</p>"""
    suspend_actions: NotRequired[
        "aws_sdk_gamelift.types.game_server_group_actions.GameServerGroupActions"
    ]
    """<p>The activity to suspend for this game server group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuspendGameServerGroupInput) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "suspend_actions" in value:
        import aws_sdk_gamelift.types.game_server_group_actions

        out["SuspendActions"] = (
            aws_sdk_gamelift.types.game_server_group_actions.serialize_aws_json_1_1(
                value["suspend_actions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SuspendGameServerGroupInput:
    out: SuspendGameServerGroupInput = {}  # type: ignore[typeddict-item]
    if "GameServerGroupName" in data:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if "SuspendActions" in data:
        import aws_sdk_gamelift.types.game_server_group_actions

        out["suspend_actions"] = (
            aws_sdk_gamelift.types.game_server_group_actions.deserialize_aws_json_1_1(
                data["SuspendActions"]
            )
        )
    return out
