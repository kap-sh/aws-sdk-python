"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteGameServerGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server_group_delete_option
    import aws_sdk_gamelift.types.game_server_group_name_or_arn


class DeleteGameServerGroupInput(TypedDict, closed=True):
    game_server_group_name: NotRequired[
        "aws_sdk_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
    ]
    """<p>A unique identifier for the game server group. Use either the name or ARN value.</p>"""
    delete_option: NotRequired[
        "aws_sdk_gamelift.types.game_server_group_delete_option.GameServerGroupDeleteOption"
    ]
    """<p>The type of delete to perform. Options include the following:</p> <ul> <li> <p> <code>SAFE_DELETE</code> – (default) Terminates the game server group and Amazon EC2 Auto Scaling group only when it has no game servers that are in <code>UTILIZED</code> status.</p> </li> <li> <p> <code>FORCE_DELETE</code> – Terminates the game server group, including all active game servers regardless of their utilization status, and the Amazon EC2 Auto Scaling group. </p> </li> <li> <p> <code>RETAIN</code> – Does a safe delete of the game server group but retains the Amazon EC2 Auto Scaling group as is.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGameServerGroupInput) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "delete_option" in value:
        import aws_sdk_gamelift.types.game_server_group_delete_option

        out["DeleteOption"] = (
            aws_sdk_gamelift.types.game_server_group_delete_option.serialize_aws_json_1_1(
                value["delete_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGameServerGroupInput:
    out: DeleteGameServerGroupInput = {}  # type: ignore[typeddict-item]
    if "GameServerGroupName" in data:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if "DeleteOption" in data:
        import aws_sdk_gamelift.types.game_server_group_delete_option

        out["delete_option"] = (
            aws_sdk_gamelift.types.game_server_group_delete_option.deserialize_aws_json_1_1(
                data["DeleteOption"]
            )
        )
    return out
