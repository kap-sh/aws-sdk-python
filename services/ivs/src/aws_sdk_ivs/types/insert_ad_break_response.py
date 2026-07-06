"""Generated from Smithy shape ``com.amazonaws.ivs#InsertAdBreakResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs.types.ad_break_id


class InsertAdBreakResponse(TypedDict, closed=True):
    ad_break_id: NotRequired["aws_sdk_ivs.types.ad_break_id.AdBreakId"]
    """<p>Unique identifier for the ad break that was inserted into the playlist.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsertAdBreakResponse) -> dict:
    out: dict = {}
    if "ad_break_id" in value:
        out["adBreakId"] = value["ad_break_id"]
    return out


def deserialize_json(data: dict) -> InsertAdBreakResponse:
    out: InsertAdBreakResponse = {}  # type: ignore[typeddict-item]
    if "adBreakId" in data:
        out["ad_break_id"] = data["adBreakId"]
    return out
