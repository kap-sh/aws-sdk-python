"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_session

GameSessionList: TypeAlias = list["aws_sdk_gamelift.types.game_session.GameSession"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionList) -> list:
    import aws_sdk_gamelift.types.game_session

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.game_session.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GameSessionList:
    import aws_sdk_gamelift.types.game_session

    out: GameSessionList = []
    for item in data:
        out.append(aws_sdk_gamelift.types.game_session.deserialize_aws_json_1_1(item))
    return out
