"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server

GameServers: TypeAlias = list["aws_sdk_gamelift.types.game_server.GameServer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServers) -> list:
    import aws_sdk_gamelift.types.game_server

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.game_server.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GameServers:
    import aws_sdk_gamelift.types.game_server

    out: GameServers = []
    for item in data:
        out.append(aws_sdk_gamelift.types.game_server.deserialize_aws_json_1_1(item))
    return out
