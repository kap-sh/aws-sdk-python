"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerLatency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.float
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.player_id


class PlayerLatency(TypedDict, closed=True):
    player_id: NotRequired["capo_gamelift.types.player_id.PlayerId"]
    """<p>A unique identifier for a player associated with the latency data.</p>"""
    region_identifier: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Name of the Region that is associated with the latency value.</p>"""
    latency_in_milliseconds: NotRequired["capo_gamelift.types.float.Float"]
    """<p>Amount of time that represents the time lag experienced by the player when connected to the specified Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerLatency) -> dict:
    out: dict = {}
    if "player_id" in value:
        out["PlayerId"] = value["player_id"]
    if "region_identifier" in value:
        out["RegionIdentifier"] = value["region_identifier"]
    if "latency_in_milliseconds" in value:
        out["LatencyInMilliseconds"] = value["latency_in_milliseconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PlayerLatency:
    out: PlayerLatency = {}  # type: ignore[typeddict-item]
    if "PlayerId" in data:
        out["player_id"] = data["PlayerId"]
    if "RegionIdentifier" in data:
        out["region_identifier"] = data["RegionIdentifier"]
    if "LatencyInMilliseconds" in data:
        out["latency_in_milliseconds"] = data["LatencyInMilliseconds"]
    return out
