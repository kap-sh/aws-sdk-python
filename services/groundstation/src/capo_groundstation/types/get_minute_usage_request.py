"""Generated from Smithy shape ``com.amazonaws.groundstation#GetMinuteUsageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.month
    import capo_groundstation.types.year


class GetMinuteUsageRequest(TypedDict, closed=True):
    month: "capo_groundstation.types.month.Month"
    """<p>The month being requested, with a value of 1-12.</p>"""
    year: "capo_groundstation.types.year.Year"
    """<p>The year being requested, in the format of YYYY.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMinuteUsageRequest) -> dict:
    out: dict = {}
    out["month"] = value["month"]
    out["year"] = value["year"]
    return out


def deserialize_json(data: dict) -> GetMinuteUsageRequest:
    out: GetMinuteUsageRequest = {}  # type: ignore[typeddict-item]
    if "month" in data:
        out["month"] = data["month"]
    else:
        raise DeserializationError("GetMinuteUsageRequest.month required")
    if "year" in data:
        out["year"] = data["year"]
    else:
        raise DeserializationError("GetMinuteUsageRequest.year required")
    return out
