"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateGameSessionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_session


class UpdateGameSessionOutput(TypedDict, closed=True):
    game_session: NotRequired["aws_sdk_gamelift.types.game_session.GameSession"]
    """<p>The updated game session properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGameSessionOutput) -> dict:
    out: dict = {}
    if "game_session" in value:
        import aws_sdk_gamelift.types.game_session

        out["GameSession"] = aws_sdk_gamelift.types.game_session.serialize_aws_json_1_1(
            value["game_session"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGameSessionOutput:
    out: UpdateGameSessionOutput = {}  # type: ignore[typeddict-item]
    if "GameSession" in data:
        import aws_sdk_gamelift.types.game_session

        out["game_session"] = (
            aws_sdk_gamelift.types.game_session.deserialize_aws_json_1_1(
                data["GameSession"]
            )
        )
    return out
