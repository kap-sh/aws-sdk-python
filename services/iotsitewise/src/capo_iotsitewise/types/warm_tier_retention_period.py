"""Generated from Smithy shape ``com.amazonaws.iotsitewise#WarmTierRetentionPeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.number_of_days
    import capo_iotsitewise.types.unlimited


class WarmTierRetentionPeriod(TypedDict, closed=True):
    number_of_days: NotRequired["capo_iotsitewise.types.number_of_days.NumberOfDays"]
    """<p>The number of days the data is stored in the warm tier.</p>"""
    unlimited: NotRequired["capo_iotsitewise.types.unlimited.Unlimited"]
    """<p>If set to true, the data is stored indefinitely in the warm tier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WarmTierRetentionPeriod) -> dict:
    out: dict = {}
    if "number_of_days" in value:
        out["numberOfDays"] = value["number_of_days"]
    if "unlimited" in value:
        out["unlimited"] = value["unlimited"]
    return out


def deserialize_json(data: dict) -> WarmTierRetentionPeriod:
    out: WarmTierRetentionPeriod = {}  # type: ignore[typeddict-item]
    if "numberOfDays" in data:
        out["number_of_days"] = data["numberOfDays"]
    if "unlimited" in data:
        out["unlimited"] = data["unlimited"]
    return out
