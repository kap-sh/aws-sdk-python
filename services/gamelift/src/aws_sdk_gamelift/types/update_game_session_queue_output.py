"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateGameSessionQueueOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_session_queue


class UpdateGameSessionQueueOutput(TypedDict, closed=True):
    game_session_queue: NotRequired[
        "aws_sdk_gamelift.types.game_session_queue.GameSessionQueue"
    ]
    """<p>An object that describes the newly updated game session queue.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGameSessionQueueOutput) -> dict:
    out: dict = {}
    if "game_session_queue" in value:
        import aws_sdk_gamelift.types.game_session_queue

        out["GameSessionQueue"] = (
            aws_sdk_gamelift.types.game_session_queue.serialize_aws_json_1_1(
                value["game_session_queue"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGameSessionQueueOutput:
    out: UpdateGameSessionQueueOutput = {}  # type: ignore[typeddict-item]
    if "GameSessionQueue" in data:
        import aws_sdk_gamelift.types.game_session_queue

        out["game_session_queue"] = (
            aws_sdk_gamelift.types.game_session_queue.deserialize_aws_json_1_1(
                data["GameSessionQueue"]
            )
        )
    return out
