"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateGameSessionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_session


class CreateGameSessionOutput(TypedDict, closed=True):
    game_session: NotRequired["aws_sdk_gamelift.types.game_session.GameSession"]
    """<p>Object that describes the newly created game session record.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGameSessionOutput) -> dict:
    out: dict = {}
    if "game_session" in value:
        import aws_sdk_gamelift.types.game_session

        out["GameSession"] = aws_sdk_gamelift.types.game_session.serialize_aws_json_1_1(
            value["game_session"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGameSessionOutput:
    out: CreateGameSessionOutput = {}  # type: ignore[typeddict-item]
    if "GameSession" in data:
        import aws_sdk_gamelift.types.game_session

        out["game_session"] = (
            aws_sdk_gamelift.types.game_session.deserialize_aws_json_1_1(
                data["GameSession"]
            )
        )
    return out
