"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeFieldIndexesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.field_indexes
    import capo_cloudwatch_logs.types.next_token


class DescribeFieldIndexesResponse(TypedDict, closed=True):
    field_indexes: NotRequired["capo_cloudwatch_logs.types.field_indexes.FieldIndexes"]
    """<p>An array containing the field index information.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFieldIndexesResponse) -> dict:
    out: dict = {}
    if "field_indexes" in value:
        import capo_cloudwatch_logs.types.field_indexes

        out["fieldIndexes"] = (
            capo_cloudwatch_logs.types.field_indexes.serialize_aws_json_1_1(
                value["field_indexes"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFieldIndexesResponse:
    out: DescribeFieldIndexesResponse = {}  # type: ignore[typeddict-item]
    if "fieldIndexes" in data:
        import capo_cloudwatch_logs.types.field_indexes

        out["field_indexes"] = (
            capo_cloudwatch_logs.types.field_indexes.deserialize_aws_json_1_1(
                data["fieldIndexes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
