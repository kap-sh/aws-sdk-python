"""Generated from Smithy shape ``com.amazonaws.ec2#GetSpotPlacementScoresResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.spot_placement_scores
    import capo_ec2.types.string


class GetSpotPlacementScoresResult(TypedDict, closed=True):
    spot_placement_scores: NotRequired[
        "capo_ec2.types.spot_placement_scores.SpotPlacementScores"
    ]
    """<p>The Spot placement score for the top 10 Regions or Availability Zones, scored on a scale from 1 to 10. Each score reflects how likely it is that each Region or Availability Zone will succeed at fulfilling the specified target capacity <i>at the time of the Spot placement score request</i>. A score of <code>10</code> means that your Spot capacity request is highly likely to succeed in that Region or Availability Zone. </p> <p>If you request a Spot placement score for Regions, a high score assumes that your fleet request will be configured to use all Availability Zones and the <code>capacity-optimized</code> allocation strategy. If you request a Spot placement score for Availability Zones, a high score assumes that your fleet request will be configured to use a single Availability Zone and the <code>capacity-optimized</code> allocation strategy.</p> <p>Different Regions or Availability Zones might return the same score.</p> <note> <p>The Spot placement score serves as a recommendation only. No score guarantees that your Spot request will be fully or partially fulfilled.</p> </note>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetSpotPlacementScoresResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "spot_placement_scores" in value:
        import capo_ec2.types.spot_placement_scores

        capo_ec2.types.spot_placement_scores.serialize_ec2_query(
            value["spot_placement_scores"], pairs, f"{key_prefix}SpotPlacementScoreSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetSpotPlacementScoresResult:
    out: GetSpotPlacementScoresResult = {}  # type: ignore[typeddict-item]
    if el.find("spotPlacementScoreSet") is not None:
        import capo_ec2.types.spot_placement_scores

        out["spot_placement_scores"] = (
            capo_ec2.types.spot_placement_scores.deserialize_ec2_query(
                el, "spotPlacementScoreSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
