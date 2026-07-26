"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#PointOfInterest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.offset_millis


class PointOfInterest(TypedDict, closed=True):
    begin_offset_millis: NotRequired[
        "capo_connect_contact_lens.types.offset_millis.OffsetMillis"
    ]
    """<p>The beginning offset in milliseconds where the category rule was detected.</p>"""
    end_offset_millis: NotRequired[
        "capo_connect_contact_lens.types.offset_millis.OffsetMillis"
    ]
    """<p>The ending offset in milliseconds where the category rule was detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PointOfInterest) -> dict:
    out: dict = {}
    if "begin_offset_millis" in value:
        out["BeginOffsetMillis"] = value["begin_offset_millis"]
    if "end_offset_millis" in value:
        out["EndOffsetMillis"] = value["end_offset_millis"]
    return out


def deserialize_json(data: dict) -> PointOfInterest:
    out: PointOfInterest = {}  # type: ignore[typeddict-item]
    if "BeginOffsetMillis" in data:
        out["begin_offset_millis"] = data["BeginOffsetMillis"]
    if "EndOffsetMillis" in data:
        out["end_offset_millis"] = data["EndOffsetMillis"]
    return out
