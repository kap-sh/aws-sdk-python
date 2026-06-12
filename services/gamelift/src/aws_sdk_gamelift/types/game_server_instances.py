"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerInstances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server_instance

GameServerInstances: TypeAlias = list[
    "aws_sdk_gamelift.types.game_server_instance.GameServerInstance"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerInstances) -> list:
    import aws_sdk_gamelift.types.game_server_instance

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.game_server_instance.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GameServerInstances:
    import aws_sdk_gamelift.types.game_server_instance

    out: GameServerInstances = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.game_server_instance.deserialize_aws_json_1_1(item)
        )
    return out
