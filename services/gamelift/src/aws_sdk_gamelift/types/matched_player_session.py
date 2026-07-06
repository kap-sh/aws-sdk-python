"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchedPlayerSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.player_id
    import aws_sdk_gamelift.types.player_session_id


class MatchedPlayerSession(TypedDict, closed=True):
    player_id: NotRequired["aws_sdk_gamelift.types.player_id.PlayerId"]
    """<p>A unique identifier for a player </p>"""
    player_session_id: NotRequired[
        "aws_sdk_gamelift.types.player_session_id.PlayerSessionId"
    ]
    """<p>A unique identifier for a player session. PlayerSessionId will only be populated for player sessions that are in ACTIVE or RESERVED status when the ticket is completed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchedPlayerSession) -> dict:
    out: dict = {}
    if "player_id" in value:
        out["PlayerId"] = value["player_id"]
    if "player_session_id" in value:
        out["PlayerSessionId"] = value["player_session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MatchedPlayerSession:
    out: MatchedPlayerSession = {}  # type: ignore[typeddict-item]
    if "PlayerId" in data:
        out["player_id"] = data["PlayerId"]
    if "PlayerSessionId" in data:
        out["player_session_id"] = data["PlayerSessionId"]
    return out
