"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdBreakOpportunity``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__long


class AdBreakOpportunity(TypedDict):
    offset_millis: "aws_sdk_mediatailor.types.__long.__long"
    """<p>The offset in milliseconds from the start of the VOD source at which an ad marker was detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdBreakOpportunity) -> dict:
    out: dict = {}
    out["OffsetMillis"] = value.get("offset_millis", 0)
    return out


def deserialize_json(data: dict) -> AdBreakOpportunity:
    out: AdBreakOpportunity = {}  # type: ignore[typeddict-item]
    if "OffsetMillis" in data:
        out["offset_millis"] = data["OffsetMillis"]
    else:
        out["offset_millis"] = 0
    return out
