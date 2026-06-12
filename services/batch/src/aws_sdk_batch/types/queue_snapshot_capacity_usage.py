"""Generated from Smithy shape ``com.amazonaws.batch#QueueSnapshotCapacityUsage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.double
    import aws_sdk_batch.types.string


class QueueSnapshotCapacityUsage(TypedDict):
    capacity_unit: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The unit of measure for the capacity usage. For compute jobs, this is <code>VCPU</code> for Amazon EC2 and <code>cpu</code> for Amazon EKS. For service jobs, this is the instance type.</p>"""
    quantity: NotRequired["aws_sdk_batch.types.double.Double"]
    """<p>The quantity of capacity being used in the queue snapshot, measured in the units specified by <code>capacityUnit</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueueSnapshotCapacityUsage) -> dict:
    out: dict = {}
    if "capacity_unit" in value:
        out["capacityUnit"] = value["capacity_unit"]
    if "quantity" in value:
        out["quantity"] = value["quantity"]
    return out


def deserialize_json(data: dict) -> QueueSnapshotCapacityUsage:
    out: QueueSnapshotCapacityUsage = {}  # type: ignore[typeddict-item]
    if "capacityUnit" in data:
        out["capacity_unit"] = data["capacityUnit"]
    if "quantity" in data:
        out["quantity"] = data["quantity"]
    return out
