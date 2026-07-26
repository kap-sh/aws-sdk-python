"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisCharacterInterval``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_offset


class RealTimeContactAnalysisCharacterInterval(TypedDict, closed=True):
    begin_offset_char: "capo_connect.types.real_time_contact_analysis_offset.RealTimeContactAnalysisOffset"
    """<p>The beginning of the character interval.</p>"""
    end_offset_char: "capo_connect.types.real_time_contact_analysis_offset.RealTimeContactAnalysisOffset"
    """<p>The end of the character interval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisCharacterInterval) -> dict:
    out: dict = {}
    out["BeginOffsetChar"] = value.get("begin_offset_char", 0)
    out["EndOffsetChar"] = value.get("end_offset_char", 0)
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisCharacterInterval:
    out: RealTimeContactAnalysisCharacterInterval = {}  # type: ignore[typeddict-item]
    if "BeginOffsetChar" in data:
        out["begin_offset_char"] = data["BeginOffsetChar"]
    else:
        out["begin_offset_char"] = 0
    if "EndOffsetChar" in data:
        out["end_offset_char"] = data["EndOffsetChar"]
    else:
        out["end_offset_char"] = 0
    return out
