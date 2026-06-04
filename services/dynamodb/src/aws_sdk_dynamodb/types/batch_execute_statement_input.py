"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchExecuteStatementInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.parti_ql_batch_request
    import aws_sdk_dynamodb.types.return_consumed_capacity


class BatchExecuteStatementInput(TypedDict):
    statements: "aws_sdk_dynamodb.types.parti_ql_batch_request.PartiQLBatchRequest"
    """<p>The list of PartiQL statements representing the batch to run.</p>"""
    return_consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchExecuteStatementInput) -> dict:
    out: dict = {}
    import aws_sdk_dynamodb.types.parti_ql_batch_request

    out["Statements"] = (
        aws_sdk_dynamodb.types.parti_ql_batch_request.serialize_aws_json_1_0(
            value["statements"]
        )
    )
    if "return_consumed_capacity" in value:
        import aws_sdk_dynamodb.types.return_consumed_capacity

        out["ReturnConsumedCapacity"] = (
            aws_sdk_dynamodb.types.return_consumed_capacity.serialize_aws_json_1_0(
                value["return_consumed_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchExecuteStatementInput:
    out: BatchExecuteStatementInput = {}  # type: ignore[typeddict-item]
    if "Statements" in data:
        import aws_sdk_dynamodb.types.parti_ql_batch_request

        out["statements"] = (
            aws_sdk_dynamodb.types.parti_ql_batch_request.deserialize_aws_json_1_0(
                data["Statements"]
            )
        )
    else:
        raise DeserializationError("BatchExecuteStatementInput.statements required")
    if "ReturnConsumedCapacity" in data:
        import aws_sdk_dynamodb.types.return_consumed_capacity

        out["return_consumed_capacity"] = (
            aws_sdk_dynamodb.types.return_consumed_capacity.deserialize_aws_json_1_0(
                data["ReturnConsumedCapacity"]
            )
        )
    return out
