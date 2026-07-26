"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanResultThreat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detection_source
    import capo_guardduty.types.item_details_list
    import capo_guardduty.types.non_empty_string
    import capo_guardduty.types.positive_long


class ScanResultThreat(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.non_empty_string.NonEmptyString"]
    """<p>The name of the detected threat.</p>"""
    source: NotRequired["capo_guardduty.types.detection_source.DetectionSource"]
    """<p>The source that detected this threat.</p>"""
    count: NotRequired["capo_guardduty.types.positive_long.PositiveLong"]
    """<p>The number of instances of this threat that were detected.</p>"""
    hash: NotRequired["capo_guardduty.types.non_empty_string.NonEmptyString"]
    """<p>The hash value associated with the detected threat.</p>"""
    item_details: NotRequired["capo_guardduty.types.item_details_list.ItemDetailsList"]
    """<p>Additional information about where this threat was detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanResultThreat) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "source" in value:
        import capo_guardduty.types.detection_source

        out["source"] = capo_guardduty.types.detection_source.serialize_json(
            value["source"]
        )
    if "count" in value:
        out["count"] = value["count"]
    if "hash" in value:
        out["hash"] = value["hash"]
    if "item_details" in value:
        import capo_guardduty.types.item_details_list

        out["itemDetails"] = capo_guardduty.types.item_details_list.serialize_json(
            value["item_details"]
        )
    return out


def deserialize_json(data: dict) -> ScanResultThreat:
    out: ScanResultThreat = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "source" in data:
        import capo_guardduty.types.detection_source

        out["source"] = capo_guardduty.types.detection_source.deserialize_json(
            data["source"]
        )
    if "count" in data:
        out["count"] = data["count"]
    if "hash" in data:
        out["hash"] = data["hash"]
    if "itemDetails" in data:
        import capo_guardduty.types.item_details_list

        out["item_details"] = capo_guardduty.types.item_details_list.deserialize_json(
            data["itemDetails"]
        )
    return out
