"""Generated from Smithy shape ``com.amazonaws.lightsail#MonthlyTransfer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.integer


class MonthlyTransfer(TypedDict, closed=True):
    gb_per_month_allocated: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The amount allocated per month (in GB).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonthlyTransfer) -> dict:
    out: dict = {}
    if "gb_per_month_allocated" in value:
        out["gbPerMonthAllocated"] = value["gb_per_month_allocated"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MonthlyTransfer:
    out: MonthlyTransfer = {}  # type: ignore[typeddict-item]
    if "gbPerMonthAllocated" in data:
        out["gb_per_month_allocated"] = data["gbPerMonthAllocated"]
    return out
