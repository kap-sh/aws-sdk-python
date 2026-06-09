"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteTableInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_arn


class DeleteTableInput(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table to delete. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteTableInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteTableInput:
    out: DeleteTableInput = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("DeleteTableInput.table_name required")
    return out
