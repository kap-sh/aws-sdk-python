"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareCapacityLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer
    import capo_batch.types.string


class QuotaShareCapacityLimit(TypedDict, closed=True):
    max_capacity: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The maximum capacity available for the quota share. This value represents the maximum quantity of a resource that can be allocated to jobs in the quota share without borrowing.</p>"""
    capacity_unit: NotRequired["capo_batch.types.string.String"]
    """<p>The unit of compute capacity for the capacityLimit. For example, <code>ml.m5.large</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuotaShareCapacityLimit) -> dict:
    out: dict = {}
    if "max_capacity" in value:
        out["maxCapacity"] = value["max_capacity"]
    if "capacity_unit" in value:
        out["capacityUnit"] = value["capacity_unit"]
    return out


def deserialize_json(data: dict) -> QuotaShareCapacityLimit:
    out: QuotaShareCapacityLimit = {}  # type: ignore[typeddict-item]
    if "maxCapacity" in data:
        out["max_capacity"] = data["maxCapacity"]
    if "capacityUnit" in data:
        out["capacity_unit"] = data["capacityUnit"]
    return out
