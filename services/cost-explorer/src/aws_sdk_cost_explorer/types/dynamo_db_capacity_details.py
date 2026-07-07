"""Generated from Smithy shape ``com.amazonaws.costexplorer#DynamoDBCapacityDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class DynamoDBCapacityDetails(TypedDict, closed=True):
    capacity_units: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The capacity unit of the recommended reservation.</p>"""
    region: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The Amazon Web Services Region of the recommended reservation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DynamoDBCapacityDetails) -> dict:
    out: dict = {}
    if "capacity_units" in value:
        out["CapacityUnits"] = value["capacity_units"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DynamoDBCapacityDetails:
    out: DynamoDBCapacityDetails = {}  # type: ignore[typeddict-item]
    if "CapacityUnits" in data:
        out["capacity_units"] = data["CapacityUnits"]
    if "Region" in data:
        out["region"] = data["Region"]
    return out
