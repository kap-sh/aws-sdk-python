"""Generated from Smithy shape ``com.amazonaws.groundstation#GetMinuteUsageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.month
    import aws_sdk_groundstation.types.year


class GetMinuteUsageRequest(TypedDict):
    month: "aws_sdk_groundstation.types.month.Month"
    """<p>The month being requested, with a value of 1-12.</p>"""
    year: "aws_sdk_groundstation.types.year.Year"
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
