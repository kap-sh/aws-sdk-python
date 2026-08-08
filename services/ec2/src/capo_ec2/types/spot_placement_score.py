"""Generated from Smithy shape ``com.amazonaws.ec2#SpotPlacementScore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.string


class SpotPlacementScore(TypedDict, closed=True):
    region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    score: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The placement score, on a scale from <code>1</code> to <code>10</code>. A score of <code>10</code> indicates that your Spot request is highly likely to succeed in this Region or Availability Zone. A score of <code>1</code> indicates that your Spot request is not likely to succeed. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotPlacementScore, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "region" in value:
        pairs.append((f"{key_prefix}Region", str(value["region"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "score" in value:
        pairs.append((f"{key_prefix}Score", str(value["score"])))


def deserialize_ec2_query(el: Element) -> SpotPlacementScore:
    out: SpotPlacementScore = {}  # type: ignore[typeddict-item]
    child_region = el.find("region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_score = el.find("score")
    if child_score is not None:
        out["score"] = int(child_score.text or "")
    return out
