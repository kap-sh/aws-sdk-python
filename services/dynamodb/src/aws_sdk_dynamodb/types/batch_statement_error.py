"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchStatementError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_map
    import aws_sdk_dynamodb.types.batch_statement_error_code_enum
    import aws_sdk_dynamodb.types.string


class BatchStatementError(TypedDict):
    code: NotRequired[
        "aws_sdk_dynamodb.types.batch_statement_error_code_enum.BatchStatementErrorCodeEnum"
    ]
    """<p> The error code associated with the failed PartiQL batch statement. </p>"""
    message: NotRequired["aws_sdk_dynamodb.types.string.String"]
    """<p> The error message associated with the PartiQL batch response. </p>"""
    item: NotRequired["aws_sdk_dynamodb.types.attribute_map.AttributeMap"]
    """<p>The item which caused the condition check to fail. This will be set if ReturnValuesOnConditionCheckFailure is specified as <code>ALL_OLD</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchStatementError) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_dynamodb.types.batch_statement_error_code_enum

        out["Code"] = (
            aws_sdk_dynamodb.types.batch_statement_error_code_enum.serialize_aws_json_1_0(
                value["code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "item" in value:
        import aws_sdk_dynamodb.types.attribute_map

        out["Item"] = aws_sdk_dynamodb.types.attribute_map.serialize_aws_json_1_0(
            value["item"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchStatementError:
    out: BatchStatementError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_dynamodb.types.batch_statement_error_code_enum

        out["code"] = (
            aws_sdk_dynamodb.types.batch_statement_error_code_enum.deserialize_aws_json_1_0(
                data["Code"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "Item" in data:
        import aws_sdk_dynamodb.types.attribute_map

        out["item"] = aws_sdk_dynamodb.types.attribute_map.deserialize_aws_json_1_0(
            data["Item"]
        )
    return out
