"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchExecuteStatementOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.consumed_capacity_multiple
    import aws_sdk_dynamodb.types.parti_ql_batch_response


class BatchExecuteStatementOutput(TypedDict):
    responses: NotRequired[
        "aws_sdk_dynamodb.types.parti_ql_batch_response.PartiQLBatchResponse"
    ]
    """<p>The response to each PartiQL statement in the batch. The values of the list are ordered according to the ordering of the request statements.</p>"""
    consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.consumed_capacity_multiple.ConsumedCapacityMultiple"
    ]
    """<p>The capacity units consumed by the entire operation. The values of the list are ordered according to the ordering of the statements.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchExecuteStatementOutput) -> dict:
    out: dict = {}
    if "responses" in value:
        import aws_sdk_dynamodb.types.parti_ql_batch_response

        out["Responses"] = (
            aws_sdk_dynamodb.types.parti_ql_batch_response.serialize_aws_json_1_0(
                value["responses"]
            )
        )
    if "consumed_capacity" in value:
        import aws_sdk_dynamodb.types.consumed_capacity_multiple

        out["ConsumedCapacity"] = (
            aws_sdk_dynamodb.types.consumed_capacity_multiple.serialize_aws_json_1_0(
                value["consumed_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchExecuteStatementOutput:
    out: BatchExecuteStatementOutput = {}  # type: ignore[typeddict-item]
    if "Responses" in data:
        import aws_sdk_dynamodb.types.parti_ql_batch_response

        out["responses"] = (
            aws_sdk_dynamodb.types.parti_ql_batch_response.deserialize_aws_json_1_0(
                data["Responses"]
            )
        )
    if "ConsumedCapacity" in data:
        import aws_sdk_dynamodb.types.consumed_capacity_multiple

        out["consumed_capacity"] = (
            aws_sdk_dynamodb.types.consumed_capacity_multiple.deserialize_aws_json_1_0(
                data["ConsumedCapacity"]
            )
        )
    return out
