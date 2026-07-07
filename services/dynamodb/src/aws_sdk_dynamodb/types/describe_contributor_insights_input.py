"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeContributorInsightsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.table_arn


class DescribeContributorInsightsInput(TypedDict, closed=True):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table to describe. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    index_name: NotRequired["aws_sdk_dynamodb.types.index_name.IndexName"]
    """<p>The name of the global secondary index to describe, if applicable.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeContributorInsightsInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeContributorInsightsInput:
    out: DescribeContributorInsightsInput = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "DescribeContributorInsightsInput.table_name required"
        )
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    return out
