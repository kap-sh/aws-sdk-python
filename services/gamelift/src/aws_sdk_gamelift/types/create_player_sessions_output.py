"""Generated from Smithy shape ``com.amazonaws.gamelift#CreatePlayerSessionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.player_session_list


class CreatePlayerSessionsOutput(TypedDict, closed=True):
    player_sessions: NotRequired[
        "aws_sdk_gamelift.types.player_session_list.PlayerSessionList"
    ]
    """<p>A collection of player session objects created for the added players.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePlayerSessionsOutput) -> dict:
    out: dict = {}
    if "player_sessions" in value:
        import aws_sdk_gamelift.types.player_session_list

        out["PlayerSessions"] = (
            aws_sdk_gamelift.types.player_session_list.serialize_aws_json_1_1(
                value["player_sessions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePlayerSessionsOutput:
    out: CreatePlayerSessionsOutput = {}  # type: ignore[typeddict-item]
    if "PlayerSessions" in data:
        import aws_sdk_gamelift.types.player_session_list

        out["player_sessions"] = (
            aws_sdk_gamelift.types.player_session_list.deserialize_aws_json_1_1(
                data["PlayerSessions"]
            )
        )
    return out
