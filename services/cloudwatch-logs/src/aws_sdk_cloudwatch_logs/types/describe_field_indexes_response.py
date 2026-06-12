"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeFieldIndexesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.field_indexes
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeFieldIndexesResponse(TypedDict):
    field_indexes: NotRequired[
        "aws_sdk_cloudwatch_logs.types.field_indexes.FieldIndexes"
    ]
    """<p>An array containing the field index information.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFieldIndexesResponse) -> dict:
    out: dict = {}
    if "field_indexes" in value:
        import aws_sdk_cloudwatch_logs.types.field_indexes

        out["fieldIndexes"] = (
            aws_sdk_cloudwatch_logs.types.field_indexes.serialize_aws_json_1_1(
                value["field_indexes"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFieldIndexesResponse:
    out: DescribeFieldIndexesResponse = {}  # type: ignore[typeddict-item]
    if "fieldIndexes" in data:
        import aws_sdk_cloudwatch_logs.types.field_indexes

        out["field_indexes"] = (
            aws_sdk_cloudwatch_logs.types.field_indexes.deserialize_aws_json_1_1(
                data["fieldIndexes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
