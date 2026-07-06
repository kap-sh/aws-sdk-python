"""Generated from Smithy shape ``com.amazonaws.timestreamquery#QueryTemporalRangeMax``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.amazon_resource_name
    import aws_sdk_timestream_query.types.long


class QueryTemporalRangeMax(TypedDict, closed=True):
    value: "aws_sdk_timestream_query.types.long.Long"
    """<p>The maximum duration in nanoseconds between the start and end of the query.</p>"""
    table_arn: NotRequired[
        "aws_sdk_timestream_query.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the table which is queried with the largest time range.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueryTemporalRangeMax) -> dict:
    out: dict = {}
    out["Value"] = value.get("value", 0)
    if "table_arn" in value:
        out["TableArn"] = value["table_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> QueryTemporalRangeMax:
    out: QueryTemporalRangeMax = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    if "TableArn" in data:
        out["table_arn"] = data["TableArn"]
    return out
