"""Generated from Smithy shape ``com.amazonaws.iotsitewise#RetentionPeriod``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.number_of_days
    import aws_sdk_iotsitewise.types.unlimited


class RetentionPeriod(TypedDict):
    number_of_days: NotRequired["aws_sdk_iotsitewise.types.number_of_days.NumberOfDays"]
    """<p>The number of days that your data is kept.</p> <note> <p>If you specified a value for this parameter, the <code>unlimited</code> parameter must be <code>false</code>.</p> </note>"""
    unlimited: NotRequired["aws_sdk_iotsitewise.types.unlimited.Unlimited"]
    """<p>If true, your data is kept indefinitely.</p> <note> <p>If configured to <code>true</code>, you must not specify a value for the <code>numberOfDays</code> parameter.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetentionPeriod) -> dict:
    out: dict = {}
    if "number_of_days" in value:
        out["numberOfDays"] = value["number_of_days"]
    if "unlimited" in value:
        out["unlimited"] = value["unlimited"]
    return out


def deserialize_json(data: dict) -> RetentionPeriod:
    out: RetentionPeriod = {}  # type: ignore[typeddict-item]
    if "numberOfDays" in data:
        out["number_of_days"] = data["numberOfDays"]
    if "unlimited" in data:
        out["unlimited"] = data["unlimited"]
    return out
