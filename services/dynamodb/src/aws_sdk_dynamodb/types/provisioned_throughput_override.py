"""Generated from Smithy shape ``com.amazonaws.dynamodb#ProvisionedThroughputOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.positive_long_object


class ProvisionedThroughputOverride(TypedDict, closed=True):
    read_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>Replica-specific read capacity units. If not specified, uses the source table's read capacity settings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProvisionedThroughputOverride) -> dict:
    out: dict = {}
    if "read_capacity_units" in value:
        out["ReadCapacityUnits"] = value["read_capacity_units"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProvisionedThroughputOverride:
    out: ProvisionedThroughputOverride = {}  # type: ignore[typeddict-item]
    if "ReadCapacityUnits" in data:
        out["read_capacity_units"] = data["ReadCapacityUnits"]
    return out
