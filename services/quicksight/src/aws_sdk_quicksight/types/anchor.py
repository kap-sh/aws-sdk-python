"""Generated from Smithy shape ``com.amazonaws.quicksight#Anchor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.anchor_type
    import aws_sdk_quicksight.types.integer
    import aws_sdk_quicksight.types.time_granularity


class Anchor(TypedDict):
    anchor_type: NotRequired["aws_sdk_quicksight.types.anchor_type.AnchorType"]
    """<p>The <code>AnchorType</code> for the Anchor.</p>"""
    time_granularity: NotRequired[
        "aws_sdk_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The <code>TimeGranularity</code> of the Anchor.</p>"""
    offset: "aws_sdk_quicksight.types.integer.Integer"
    """<p>The offset of the Anchor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Anchor) -> dict:
    out: dict = {}
    if "anchor_type" in value:
        import aws_sdk_quicksight.types.anchor_type

        out["AnchorType"] = aws_sdk_quicksight.types.anchor_type.serialize_json(
            value["anchor_type"]
        )
    if "time_granularity" in value:
        import aws_sdk_quicksight.types.time_granularity

        out["TimeGranularity"] = (
            aws_sdk_quicksight.types.time_granularity.serialize_json(
                value["time_granularity"]
            )
        )
    out["Offset"] = value.get("offset", 0)
    return out


def deserialize_json(data: dict) -> Anchor:
    out: Anchor = {}  # type: ignore[typeddict-item]
    if "AnchorType" in data:
        import aws_sdk_quicksight.types.anchor_type

        out["anchor_type"] = aws_sdk_quicksight.types.anchor_type.deserialize_json(
            data["AnchorType"]
        )
    if "TimeGranularity" in data:
        import aws_sdk_quicksight.types.time_granularity

        out["time_granularity"] = (
            aws_sdk_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if "Offset" in data:
        out["offset"] = data["Offset"]
    else:
        out["offset"] = 0
    return out
