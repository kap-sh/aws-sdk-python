"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerInstanceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server_instance_id

GameServerInstanceIds: TypeAlias = list[
    "aws_sdk_gamelift.types.game_server_instance_id.GameServerInstanceId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerInstanceIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GameServerInstanceIds:
    return list(data)
