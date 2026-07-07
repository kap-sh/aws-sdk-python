"""Generated from Smithy shape ``com.amazonaws.guardduty#DataSourceFreeTrial``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.integer


class DataSourceFreeTrial(TypedDict, closed=True):
    free_trial_days_remaining: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>A value that specifies the number of days left to use each enabled data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceFreeTrial) -> dict:
    out: dict = {}
    if "free_trial_days_remaining" in value:
        out["freeTrialDaysRemaining"] = value["free_trial_days_remaining"]
    return out


def deserialize_json(data: dict) -> DataSourceFreeTrial:
    out: DataSourceFreeTrial = {}  # type: ignore[typeddict-item]
    if "freeTrialDaysRemaining" in data:
        out["free_trial_days_remaining"] = data["freeTrialDaysRemaining"]
    return out
