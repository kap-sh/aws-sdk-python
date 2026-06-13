"""Generated from Smithy shape ``com.amazonaws.wisdom#Highlight``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.highlight_offset


class Highlight(TypedDict):
    begin_offset_inclusive: "aws_sdk_wisdom.types.highlight_offset.HighlightOffset"
    """<p>The offset for the start of the highlight.</p>"""
    end_offset_exclusive: "aws_sdk_wisdom.types.highlight_offset.HighlightOffset"
    """<p>The offset for the end of the highlight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Highlight) -> dict:
    out: dict = {}
    out["beginOffsetInclusive"] = value.get("begin_offset_inclusive", 0)
    out["endOffsetExclusive"] = value.get("end_offset_exclusive", 0)
    return out


def deserialize_json(data: dict) -> Highlight:
    out: Highlight = {}  # type: ignore[typeddict-item]
    if "beginOffsetInclusive" in data:
        out["begin_offset_inclusive"] = data["beginOffsetInclusive"]
    else:
        out["begin_offset_inclusive"] = 0
    if "endOffsetExclusive" in data:
        out["end_offset_exclusive"] = data["endOffsetExclusive"]
    else:
        out["end_offset_exclusive"] = 0
    return out
