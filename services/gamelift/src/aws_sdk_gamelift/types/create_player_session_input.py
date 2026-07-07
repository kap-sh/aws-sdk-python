"""Generated from Smithy shape ``com.amazonaws.gamelift#CreatePlayerSessionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.arn_string_model
    import aws_sdk_gamelift.types.player_data
    import aws_sdk_gamelift.types.player_id


class CreatePlayerSessionInput(TypedDict, closed=True):
    game_session_id: NotRequired[
        "aws_sdk_gamelift.types.arn_string_model.ArnStringModel"
    ]
    """<p>An identifier for the game session that is unique across all regions to add a player to. The value is always a full ARN in the following format: <code>arn:aws:gamelift:<location>::gamesession/<fleet ID>/<ID string></code>.</p>"""
    player_id: NotRequired["aws_sdk_gamelift.types.player_id.PlayerId"]
    """<p>A unique identifier for a player. Player IDs are developer-defined.</p>"""
    player_data: NotRequired["aws_sdk_gamelift.types.player_data.PlayerData"]
    """<p>Developer-defined information related to a player. Amazon GameLift Servers does not use this data, so it can be formatted as needed for use in the game.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePlayerSessionInput) -> dict:
    out: dict = {}
    if "game_session_id" in value:
        out["GameSessionId"] = value["game_session_id"]
    if "player_id" in value:
        out["PlayerId"] = value["player_id"]
    if "player_data" in value:
        out["PlayerData"] = value["player_data"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePlayerSessionInput:
    out: CreatePlayerSessionInput = {}  # type: ignore[typeddict-item]
    if "GameSessionId" in data:
        out["game_session_id"] = data["GameSessionId"]
    if "PlayerId" in data:
        out["player_id"] = data["PlayerId"]
    if "PlayerData" in data:
        out["player_data"] = data["PlayerData"]
    return out
