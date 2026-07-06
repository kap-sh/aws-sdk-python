"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactGetItemsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.consumed_capacity_multiple
    import aws_sdk_dynamodb.types.item_response_list


class TransactGetItemsOutput(TypedDict, closed=True):
    consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.consumed_capacity_multiple.ConsumedCapacityMultiple"
    ]
    """<p>If the <i>ReturnConsumedCapacity</i> value was <code>TOTAL</code>, this is an array of <code>ConsumedCapacity</code> objects, one for each table addressed by <code>TransactGetItem</code> objects in the <i>TransactItems</i> parameter. These <code>ConsumedCapacity</code> objects report the read-capacity units consumed by the <code>TransactGetItems</code> call in that table.</p>"""
    responses: NotRequired["aws_sdk_dynamodb.types.item_response_list.ItemResponseList"]
    """<p>An ordered array of up to 100 <code>ItemResponse</code> objects, each of which corresponds to the <code>TransactGetItem</code> object in the same position in the <i>TransactItems</i> array. Each <code>ItemResponse</code> object contains a Map of the name-value pairs that are the projected attributes of the requested item.</p> <p>If a requested item could not be retrieved, the corresponding <code>ItemResponse</code> object is Null, or if the requested item has no projected attributes, the corresponding <code>ItemResponse</code> object is an empty Map. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransactGetItemsOutput) -> dict:
    out: dict = {}
    if "consumed_capacity" in value:
        import aws_sdk_dynamodb.types.consumed_capacity_multiple

        out["ConsumedCapacity"] = (
            aws_sdk_dynamodb.types.consumed_capacity_multiple.serialize_aws_json_1_0(
                value["consumed_capacity"]
            )
        )
    if "responses" in value:
        import aws_sdk_dynamodb.types.item_response_list

        out["Responses"] = (
            aws_sdk_dynamodb.types.item_response_list.serialize_aws_json_1_0(
                value["responses"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TransactGetItemsOutput:
    out: TransactGetItemsOutput = {}  # type: ignore[typeddict-item]
    if "ConsumedCapacity" in data:
        import aws_sdk_dynamodb.types.consumed_capacity_multiple

        out["consumed_capacity"] = (
            aws_sdk_dynamodb.types.consumed_capacity_multiple.deserialize_aws_json_1_0(
                data["ConsumedCapacity"]
            )
        )
    if "Responses" in data:
        import aws_sdk_dynamodb.types.item_response_list

        out["responses"] = (
            aws_sdk_dynamodb.types.item_response_list.deserialize_aws_json_1_0(
                data["Responses"]
            )
        )
    return out
