"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchStatementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_map
    import aws_sdk_dynamodb.types.batch_statement_error
    import aws_sdk_dynamodb.types.table_name


class BatchStatementResponse(TypedDict, closed=True):
    error: NotRequired[
        "aws_sdk_dynamodb.types.batch_statement_error.BatchStatementError"
    ]
    """<p> The error associated with a failed PartiQL batch statement. </p>"""
    table_name: NotRequired["aws_sdk_dynamodb.types.table_name.TableName"]
    """<p> The table name associated with a failed PartiQL batch statement. </p>"""
    item: NotRequired["aws_sdk_dynamodb.types.attribute_map.AttributeMap"]
    """<p> A DynamoDB item associated with a BatchStatementResponse </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchStatementResponse) -> dict:
    out: dict = {}
    if "error" in value:
        import aws_sdk_dynamodb.types.batch_statement_error

        out["Error"] = (
            aws_sdk_dynamodb.types.batch_statement_error.serialize_aws_json_1_0(
                value["error"]
            )
        )
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "item" in value:
        import aws_sdk_dynamodb.types.attribute_map

        out["Item"] = aws_sdk_dynamodb.types.attribute_map.serialize_aws_json_1_0(
            value["item"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchStatementResponse:
    out: BatchStatementResponse = {}  # type: ignore[typeddict-item]
    if "Error" in data:
        import aws_sdk_dynamodb.types.batch_statement_error

        out["error"] = (
            aws_sdk_dynamodb.types.batch_statement_error.deserialize_aws_json_1_0(
                data["Error"]
            )
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "Item" in data:
        import aws_sdk_dynamodb.types.attribute_map

        out["item"] = aws_sdk_dynamodb.types.attribute_map.deserialize_aws_json_1_0(
            data["Item"]
        )
    return out
