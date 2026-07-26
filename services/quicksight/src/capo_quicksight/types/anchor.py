"""Generated from Smithy shape ``com.amazonaws.quicksight#Anchor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.anchor_type
    import capo_quicksight.types.integer
    import capo_quicksight.types.time_granularity


class Anchor(TypedDict, closed=True):
    anchor_type: NotRequired["capo_quicksight.types.anchor_type.AnchorType"]
    """<p>The <code>AnchorType</code> for the Anchor.</p>"""
    time_granularity: NotRequired[
        "capo_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The <code>TimeGranularity</code> of the Anchor.</p>"""
    offset: "capo_quicksight.types.integer.Integer"
    """<p>The offset of the Anchor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Anchor) -> dict:
    out: dict = {}
    if "anchor_type" in value:
        import capo_quicksight.types.anchor_type

        out["AnchorType"] = capo_quicksight.types.anchor_type.serialize_json(
            value["anchor_type"]
        )
    if "time_granularity" in value:
        import capo_quicksight.types.time_granularity

        out["TimeGranularity"] = capo_quicksight.types.time_granularity.serialize_json(
            value["time_granularity"]
        )
    out["Offset"] = value.get("offset", 0)
    return out


def deserialize_json(data: dict) -> Anchor:
    out: Anchor = {}  # type: ignore[typeddict-item]
    if "AnchorType" in data:
        import capo_quicksight.types.anchor_type

        out["anchor_type"] = capo_quicksight.types.anchor_type.deserialize_json(
            data["AnchorType"]
        )
    if "TimeGranularity" in data:
        import capo_quicksight.types.time_granularity

        out["time_granularity"] = (
            capo_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if "Offset" in data:
        out["offset"] = data["Offset"]
    else:
        out["offset"] = 0
    return out
