"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeContinuousBackupsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_arn


class DescribeContinuousBackupsInput(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>Name of the table for which the customer wants to check the continuous backups and point in time recovery settings.</p> <p>You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeContinuousBackupsInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeContinuousBackupsInput:
    out: DescribeContinuousBackupsInput = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("DescribeContinuousBackupsInput.table_name required")
    return out
