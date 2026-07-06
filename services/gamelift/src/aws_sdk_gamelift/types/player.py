"""Generated from Smithy shape ``com.amazonaws.gamelift#Player``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.latency_map
    import aws_sdk_gamelift.types.non_zero_and_max_string
    import aws_sdk_gamelift.types.player_attribute_map
    import aws_sdk_gamelift.types.player_id


class Player(TypedDict, closed=True):
    player_id: NotRequired["aws_sdk_gamelift.types.player_id.PlayerId"]
    """<p>A unique identifier for a player</p>"""
    player_attributes: NotRequired[
        "aws_sdk_gamelift.types.player_attribute_map.PlayerAttributeMap"
    ]
    r"""<p>A collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the <i>playerAttributes</i> used in a matchmaking rule set. Example: <code>\"PlayerAttributes\": {\"skill\": {\"N\": \"23\"}, \"gameMode\": {\"S\": \"deathmatch\"}}</code>.</p> <p>You can provide up to 10 <code>PlayerAttributes</code>.</p>"""
    team: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.</p>"""
    latency_in_ms: NotRequired["aws_sdk_gamelift.types.latency_map.LatencyMap"]
    """<p>A set of values, expressed in milliseconds, that indicates the amount of latency that a player experiences when connected to Amazon Web Services Regions. If this property is present, FlexMatch considers placing the match only in Regions for which latency is reported. </p> <p>If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no Regions are available to the player and the ticket is not matchable. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Player) -> dict:
    out: dict = {}
    if "player_id" in value:
        out["PlayerId"] = value["player_id"]
    if "player_attributes" in value:
        import aws_sdk_gamelift.types.player_attribute_map

        out["PlayerAttributes"] = (
            aws_sdk_gamelift.types.player_attribute_map.serialize_aws_json_1_1(
                value["player_attributes"]
            )
        )
    if "team" in value:
        out["Team"] = value["team"]
    if "latency_in_ms" in value:
        import aws_sdk_gamelift.types.latency_map

        out["LatencyInMs"] = aws_sdk_gamelift.types.latency_map.serialize_aws_json_1_1(
            value["latency_in_ms"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Player:
    out: Player = {}  # type: ignore[typeddict-item]
    if "PlayerId" in data:
        out["player_id"] = data["PlayerId"]
    if "PlayerAttributes" in data:
        import aws_sdk_gamelift.types.player_attribute_map

        out["player_attributes"] = (
            aws_sdk_gamelift.types.player_attribute_map.deserialize_aws_json_1_1(
                data["PlayerAttributes"]
            )
        )
    if "Team" in data:
        out["team"] = data["Team"]
    if "LatencyInMs" in data:
        import aws_sdk_gamelift.types.latency_map

        out["latency_in_ms"] = (
            aws_sdk_gamelift.types.latency_map.deserialize_aws_json_1_1(
                data["LatencyInMs"]
            )
        )
    return out
