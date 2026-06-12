"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server_group

GameServerGroups: TypeAlias = list[
    "aws_sdk_gamelift.types.game_server_group.GameServerGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerGroups) -> list:
    import aws_sdk_gamelift.types.game_server_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.game_server_group.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GameServerGroups:
    import aws_sdk_gamelift.types.game_server_group

    out: GameServerGroups = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.game_server_group.deserialize_aws_json_1_1(item)
        )
    return out
