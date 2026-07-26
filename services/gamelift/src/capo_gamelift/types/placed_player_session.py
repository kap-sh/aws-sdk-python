"""Generated from Smithy shape ``com.amazonaws.gamelift#PlacedPlayerSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.player_id
    import capo_gamelift.types.player_session_id


class PlacedPlayerSession(TypedDict, closed=True):
    player_id: NotRequired["capo_gamelift.types.player_id.PlayerId"]
    """<p>A unique identifier for a player that is associated with this player session.</p>"""
    player_session_id: NotRequired[
        "capo_gamelift.types.player_session_id.PlayerSessionId"
    ]
    """<p>A unique identifier for a player session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacedPlayerSession) -> dict:
    out: dict = {}
    if "player_id" in value:
        out["PlayerId"] = value["player_id"]
    if "player_session_id" in value:
        out["PlayerSessionId"] = value["player_session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PlacedPlayerSession:
    out: PlacedPlayerSession = {}  # type: ignore[typeddict-item]
    if "PlayerId" in data:
        out["player_id"] = data["PlayerId"]
    if "PlayerSessionId" in data:
        out["player_session_id"] = data["PlayerSessionId"]
    return out
