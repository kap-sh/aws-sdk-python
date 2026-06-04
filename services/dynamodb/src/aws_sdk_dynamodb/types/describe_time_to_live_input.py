"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeTimeToLiveInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_arn


class DescribeTimeToLiveInput(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table to be described. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeTimeToLiveInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeTimeToLiveInput:
    out: DescribeTimeToLiveInput = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("DescribeTimeToLiveInput.table_name required")
    return out
