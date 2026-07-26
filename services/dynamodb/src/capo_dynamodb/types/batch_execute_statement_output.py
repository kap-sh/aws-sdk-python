"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchExecuteStatementOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.consumed_capacity_multiple
    import capo_dynamodb.types.parti_ql_batch_response


class BatchExecuteStatementOutput(TypedDict, closed=True):
    responses: NotRequired[
        "capo_dynamodb.types.parti_ql_batch_response.PartiQLBatchResponse"
    ]
    """<p>The response to each PartiQL statement in the batch. The values of the list are ordered according to the ordering of the request statements.</p>"""
    consumed_capacity: NotRequired[
        "capo_dynamodb.types.consumed_capacity_multiple.ConsumedCapacityMultiple"
    ]
    """<p>The capacity units consumed by the entire operation. The values of the list are ordered according to the ordering of the statements.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchExecuteStatementOutput) -> dict:
    out: dict = {}
    if "responses" in value:
        import capo_dynamodb.types.parti_ql_batch_response

        out["Responses"] = (
            capo_dynamodb.types.parti_ql_batch_response.serialize_aws_json_1_0(
                value["responses"]
            )
        )
    if "consumed_capacity" in value:
        import capo_dynamodb.types.consumed_capacity_multiple

        out["ConsumedCapacity"] = (
            capo_dynamodb.types.consumed_capacity_multiple.serialize_aws_json_1_0(
                value["consumed_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchExecuteStatementOutput:
    out: BatchExecuteStatementOutput = {}  # type: ignore[typeddict-item]
    if "Responses" in data:
        import capo_dynamodb.types.parti_ql_batch_response

        out["responses"] = (
            capo_dynamodb.types.parti_ql_batch_response.deserialize_aws_json_1_0(
                data["Responses"]
            )
        )
    if "ConsumedCapacity" in data:
        import capo_dynamodb.types.consumed_capacity_multiple

        out["consumed_capacity"] = (
            capo_dynamodb.types.consumed_capacity_multiple.deserialize_aws_json_1_0(
                data["ConsumedCapacity"]
            )
        )
    return out
