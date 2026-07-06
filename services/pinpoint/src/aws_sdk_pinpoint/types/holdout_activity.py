"""Generated from Smithy shape ``com.amazonaws.pinpoint#HoldoutActivity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__integer
    import aws_sdk_pinpoint.types.__string


class HoldoutActivity(TypedDict, closed=True):
    next_activity: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the next activity to perform, after performing the holdout activity.</p>"""
    percentage: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The percentage of participants who shouldn't continue the journey.</p> <p>To determine which participants are held out, Amazon Pinpoint applies a probability-based algorithm to the percentage that you specify. Therefore, the actual percentage of participants who are held out may not be equal to the percentage that you specify.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HoldoutActivity) -> dict:
    out: dict = {}
    if "next_activity" in value:
        out["NextActivity"] = value["next_activity"]
    if "percentage" in value:
        out["Percentage"] = value["percentage"]
    return out


def deserialize_json(data: dict) -> HoldoutActivity:
    out: HoldoutActivity = {}  # type: ignore[typeddict-item]
    if "NextActivity" in data:
        out["next_activity"] = data["NextActivity"]
    if "Percentage" in data:
        out["percentage"] = data["Percentage"]
    return out
