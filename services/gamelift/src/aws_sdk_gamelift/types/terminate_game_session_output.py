"""Generated from Smithy shape ``com.amazonaws.gamelift#TerminateGameSessionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_session


class TerminateGameSessionOutput(TypedDict):
    game_session: NotRequired["aws_sdk_gamelift.types.game_session.GameSession"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateGameSessionOutput) -> dict:
    out: dict = {}
    if "game_session" in value:
        import aws_sdk_gamelift.types.game_session

        out["GameSession"] = aws_sdk_gamelift.types.game_session.serialize_aws_json_1_1(
            value["game_session"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateGameSessionOutput:
    out: TerminateGameSessionOutput = {}  # type: ignore[typeddict-item]
    if "GameSession" in data:
        import aws_sdk_gamelift.types.game_session

        out["game_session"] = (
            aws_sdk_gamelift.types.game_session.deserialize_aws_json_1_1(
                data["GameSession"]
            )
        )
    return out
