"""Generated from Smithy shape ``com.amazonaws.batch#JobCapacityUsageSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.double
    import aws_sdk_batch.types.string


class JobCapacityUsageSummary(TypedDict, closed=True):
    capacity_unit: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The unit of measure for the capacity usage. This is <code>VCPU</code> for Amazon EC2 and <code>cpu</code> for Amazon EKS.</p>"""
    quantity: NotRequired["aws_sdk_batch.types.double.Double"]
    """<p>The quantity of capacity being used by the job, measured in the units specified by <code>capacityUnit</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobCapacityUsageSummary) -> dict:
    out: dict = {}
    if "capacity_unit" in value:
        out["capacityUnit"] = value["capacity_unit"]
    if "quantity" in value:
        out["quantity"] = value["quantity"]
    return out


def deserialize_json(data: dict) -> JobCapacityUsageSummary:
    out: JobCapacityUsageSummary = {}  # type: ignore[typeddict-item]
    if "capacityUnit" in data:
        out["capacity_unit"] = data["capacityUnit"]
    if "quantity" in data:
        out["quantity"] = data["quantity"]
    return out
