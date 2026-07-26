"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionQueueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.game_session_queue

GameSessionQueueList: TypeAlias = list[
    "capo_gamelift.types.game_session_queue.GameSessionQueue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionQueueList) -> list:
    import capo_gamelift.types.game_session_queue

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.game_session_queue.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GameSessionQueueList:
    import capo_gamelift.types.game_session_queue

    out: GameSessionQueueList = []
    for item in data:
        out.append(
            capo_gamelift.types.game_session_queue.deserialize_aws_json_1_1(item)
        )
    return out
