"""Generated from Smithy shape ``com.amazonaws.pinpoint#RandomSplitEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__integer
    import aws_sdk_pinpoint.types.__string


class RandomSplitEntry(TypedDict):
    next_activity: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the next activity to perform, after completing the activity for the path.</p>"""
    percentage: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The percentage of participants to send down the activity path.</p> <p>To determine which participants are sent down each path, Amazon Pinpoint applies a probability-based algorithm to the percentages that you specify for the paths. Therefore, the actual percentage of participants who are sent down a path may not be equal to the percentage that you specify.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RandomSplitEntry) -> dict:
    out: dict = {}
    if "next_activity" in value:
        out["NextActivity"] = value["next_activity"]
    if "percentage" in value:
        out["Percentage"] = value["percentage"]
    return out


def deserialize_json(data: dict) -> RandomSplitEntry:
    out: RandomSplitEntry = {}  # type: ignore[typeddict-item]
    if "NextActivity" in data:
        out["next_activity"] = data["NextActivity"]
    if "Percentage" in data:
        out["percentage"] = data["Percentage"]
    return out
