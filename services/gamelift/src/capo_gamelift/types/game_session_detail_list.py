"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.game_session_detail

GameSessionDetailList: TypeAlias = list[
    "capo_gamelift.types.game_session_detail.GameSessionDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionDetailList) -> list:
    import capo_gamelift.types.game_session_detail

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.game_session_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GameSessionDetailList:
    import capo_gamelift.types.game_session_detail

    out: GameSessionDetailList = []
    for item in data:
        out.append(
            capo_gamelift.types.game_session_detail.deserialize_aws_json_1_1(item)
        )
    return out
