"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerGroupActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.game_server_group_action

GameServerGroupActions: TypeAlias = list[
    "capo_gamelift.types.game_server_group_action.GameServerGroupAction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerGroupActions) -> list:
    import capo_gamelift.types.game_server_group_action

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.game_server_group_action.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GameServerGroupActions:
    import capo_gamelift.types.game_server_group_action

    out: GameServerGroupActions = []
    for item in data:
        out.append(
            capo_gamelift.types.game_server_group_action.deserialize_aws_json_1_1(item)
        )
    return out
