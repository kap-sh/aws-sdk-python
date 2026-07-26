"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareCapacityUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.double
    import capo_batch.types.string


class QuotaShareCapacityUsage(TypedDict, closed=True):
    capacity_unit: NotRequired["capo_batch.types.string.String"]
    """<p>The unit of compute capacity for the capacity usage.</p>"""
    quantity: NotRequired["capo_batch.types.double.Double"]
    """<p>The quantity of capacity being used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuotaShareCapacityUsage) -> dict:
    out: dict = {}
    if "capacity_unit" in value:
        out["capacityUnit"] = value["capacity_unit"]
    if "quantity" in value:
        out["quantity"] = value["quantity"]
    return out


def deserialize_json(data: dict) -> QuotaShareCapacityUsage:
    out: QuotaShareCapacityUsage = {}  # type: ignore[typeddict-item]
    if "capacityUnit" in data:
        out["capacity_unit"] = data["capacityUnit"]
    if "quantity" in data:
        out["quantity"] = data["quantity"]
    return out
