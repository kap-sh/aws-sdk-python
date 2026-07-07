"""Generated from Smithy shape ``com.amazonaws.wickr#GuestUserHistoryCount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string


class GuestUserHistoryCount(TypedDict, closed=True):
    month: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The month and billing period in YYYY_MM format (e.g., '2024_01').</p>"""
    count: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The number of guest users who have communicated with your Wickr network during this billing period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuestUserHistoryCount) -> dict:
    out: dict = {}
    out["month"] = value["month"]
    out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> GuestUserHistoryCount:
    out: GuestUserHistoryCount = {}  # type: ignore[typeddict-item]
    if "month" in data:
        out["month"] = data["month"]
    else:
        raise DeserializationError("GuestUserHistoryCount.month required")
    if "count" in data:
        out["count"] = data["count"]
    else:
        raise DeserializationError("GuestUserHistoryCount.count required")
    return out
