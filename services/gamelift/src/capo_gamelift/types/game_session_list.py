"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.game_session

GameSessionList: TypeAlias = list["capo_gamelift.types.game_session.GameSession"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionList) -> list:
    import capo_gamelift.types.game_session

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.game_session.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GameSessionList:
    import capo_gamelift.types.game_session

    out: GameSessionList = []
    for item in data:
        out.append(capo_gamelift.types.game_session.deserialize_aws_json_1_1(item))
    return out
