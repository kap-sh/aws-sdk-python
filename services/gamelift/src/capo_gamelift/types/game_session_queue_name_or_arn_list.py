"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionQueueNameOrArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.game_session_queue_name_or_arn

GameSessionQueueNameOrArnList: TypeAlias = list[
    "capo_gamelift.types.game_session_queue_name_or_arn.GameSessionQueueNameOrArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionQueueNameOrArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GameSessionQueueNameOrArnList:
    return list(data)
