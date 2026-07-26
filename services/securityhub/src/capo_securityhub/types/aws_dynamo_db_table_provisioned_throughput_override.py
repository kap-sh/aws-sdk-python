"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableProvisionedThroughputOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer


class AwsDynamoDbTableProvisionedThroughputOverride(TypedDict, closed=True):
    read_capacity_units: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The read capacity units for the replica.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableProvisionedThroughputOverride) -> dict:
    out: dict = {}
    if "read_capacity_units" in value:
        out["ReadCapacityUnits"] = value["read_capacity_units"]
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableProvisionedThroughputOverride:
    out: AwsDynamoDbTableProvisionedThroughputOverride = {}  # type: ignore[typeddict-item]
    if "ReadCapacityUnits" in data:
        out["read_capacity_units"] = data["ReadCapacityUnits"]
    return out
