"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionQueueDestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_session_queue_destination

GameSessionQueueDestinationList: TypeAlias = list[
    "aws_sdk_gamelift.types.game_session_queue_destination.GameSessionQueueDestination"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionQueueDestinationList) -> list:
    import aws_sdk_gamelift.types.game_session_queue_destination

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.game_session_queue_destination.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GameSessionQueueDestinationList:
    import aws_sdk_gamelift.types.game_session_queue_destination

    out: GameSessionQueueDestinationList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.game_session_queue_destination.deserialize_aws_json_1_1(
                item
            )
        )
    return out
