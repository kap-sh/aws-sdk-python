"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeLimitsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.positive_long_object


class DescribeLimitsOutput(TypedDict):
    account_max_read_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum total read capacity units that your account allows you to provision across all of your tables in this Region.</p>"""
    account_max_write_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum total write capacity units that your account allows you to provision across all of your tables in this Region.</p>"""
    table_max_read_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum read capacity units that your account allows you to provision for a new table that you are creating in this Region, including the read capacity units provisioned for its global secondary indexes (GSIs).</p>"""
    table_max_write_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum write capacity units that your account allows you to provision for a new table that you are creating in this Region, including the write capacity units provisioned for its global secondary indexes (GSIs).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeLimitsOutput) -> dict:
    out: dict = {}
    if "account_max_read_capacity_units" in value:
        out["AccountMaxReadCapacityUnits"] = value["account_max_read_capacity_units"]
    if "account_max_write_capacity_units" in value:
        out["AccountMaxWriteCapacityUnits"] = value["account_max_write_capacity_units"]
    if "table_max_read_capacity_units" in value:
        out["TableMaxReadCapacityUnits"] = value["table_max_read_capacity_units"]
    if "table_max_write_capacity_units" in value:
        out["TableMaxWriteCapacityUnits"] = value["table_max_write_capacity_units"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeLimitsOutput:
    out: DescribeLimitsOutput = {}  # type: ignore[typeddict-item]
    if "AccountMaxReadCapacityUnits" in data:
        out["account_max_read_capacity_units"] = data["AccountMaxReadCapacityUnits"]
    if "AccountMaxWriteCapacityUnits" in data:
        out["account_max_write_capacity_units"] = data["AccountMaxWriteCapacityUnits"]
    if "TableMaxReadCapacityUnits" in data:
        out["table_max_read_capacity_units"] = data["TableMaxReadCapacityUnits"]
    if "TableMaxWriteCapacityUnits" in data:
        out["table_max_write_capacity_units"] = data["TableMaxWriteCapacityUnits"]
    return out
