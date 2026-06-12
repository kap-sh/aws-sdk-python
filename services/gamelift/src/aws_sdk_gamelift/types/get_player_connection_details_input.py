"""Generated from Smithy shape ``com.amazonaws.gamelift#GetPlayerConnectionDetailsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.arn_string_model
    import aws_sdk_gamelift.types.player_id_list


class GetPlayerConnectionDetailsInput(TypedDict):
    game_session_id: NotRequired[
        "aws_sdk_gamelift.types.arn_string_model.ArnStringModel"
    ]
    """<p>An identifier for the game session that is unique across all regions for which to retrieve player connection details. The value is always a full ARN in the following format: <code>arn:aws:gamelift:<location>::gamesession/<fleet ID>/<ID string></code>.</p>"""
    player_ids: NotRequired["aws_sdk_gamelift.types.player_id_list.PlayerIdList"]
    """<p>List of unique identifiers for players. Connection details are returned for each player in this list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPlayerConnectionDetailsInput) -> dict:
    out: dict = {}
    if "game_session_id" in value:
        out["GameSessionId"] = value["game_session_id"]
    if "player_ids" in value:
        import aws_sdk_gamelift.types.player_id_list

        out["PlayerIds"] = aws_sdk_gamelift.types.player_id_list.serialize_aws_json_1_1(
            value["player_ids"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPlayerConnectionDetailsInput:
    out: GetPlayerConnectionDetailsInput = {}  # type: ignore[typeddict-item]
    if "GameSessionId" in data:
        out["game_session_id"] = data["GameSessionId"]
    if "PlayerIds" in data:
        import aws_sdk_gamelift.types.player_id_list

        out["player_ids"] = (
            aws_sdk_gamelift.types.player_id_list.deserialize_aws_json_1_1(
                data["PlayerIds"]
            )
        )
    return out
