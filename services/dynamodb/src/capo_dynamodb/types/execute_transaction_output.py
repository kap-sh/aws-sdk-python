"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExecuteTransactionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.consumed_capacity_multiple
    import capo_dynamodb.types.item_response_list


class ExecuteTransactionOutput(TypedDict, closed=True):
    responses: NotRequired["capo_dynamodb.types.item_response_list.ItemResponseList"]
    """<p>The response to a PartiQL transaction.</p>"""
    consumed_capacity: NotRequired[
        "capo_dynamodb.types.consumed_capacity_multiple.ConsumedCapacityMultiple"
    ]
    """<p>The capacity units consumed by the entire operation. The values of the list are ordered according to the ordering of the statements.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecuteTransactionOutput) -> dict:
    out: dict = {}
    if "responses" in value:
        import capo_dynamodb.types.item_response_list

        out["Responses"] = (
            capo_dynamodb.types.item_response_list.serialize_aws_json_1_0(
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


def deserialize_aws_json_1_0(data: dict) -> ExecuteTransactionOutput:
    out: ExecuteTransactionOutput = {}  # type: ignore[typeddict-item]
    if "Responses" in data:
        import capo_dynamodb.types.item_response_list

        out["responses"] = (
            capo_dynamodb.types.item_response_list.deserialize_aws_json_1_0(
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
