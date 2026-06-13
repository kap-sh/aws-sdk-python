"""Generated from Smithy shape ``com.amazonaws.qconnect#CitationSpan``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.citation_span_offset


class CitationSpan(TypedDict):
    begin_offset_inclusive: (
        "aws_sdk_qconnect.types.citation_span_offset.CitationSpanOffset"
    )
    """<p>Where the text with a citation starts in the generated output.</p>"""
    end_offset_exclusive: (
        "aws_sdk_qconnect.types.citation_span_offset.CitationSpanOffset"
    )
    """<p>Where the text with a citation ends in the generated output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CitationSpan) -> dict:
    out: dict = {}
    out["beginOffsetInclusive"] = value.get("begin_offset_inclusive", 0)
    out["endOffsetExclusive"] = value.get("end_offset_exclusive", 0)
    return out


def deserialize_json(data: dict) -> CitationSpan:
    out: CitationSpan = {}  # type: ignore[typeddict-item]
    if "beginOffsetInclusive" in data:
        out["begin_offset_inclusive"] = data["beginOffsetInclusive"]
    else:
        out["begin_offset_inclusive"] = 0
    if "endOffsetExclusive" in data:
        out["end_offset_exclusive"] = data["endOffsetExclusive"]
    else:
        out["end_offset_exclusive"] = 0
    return out
