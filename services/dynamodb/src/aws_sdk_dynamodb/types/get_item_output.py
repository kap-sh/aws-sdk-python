"""Generated from Smithy shape ``com.amazonaws.dynamodb#GetItemOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_map
    import aws_sdk_dynamodb.types.consumed_capacity


class GetItemOutput(TypedDict):
    item: NotRequired["aws_sdk_dynamodb.types.attribute_map.AttributeMap"]
    """<p>A map of attribute names to <code>AttributeValue</code> objects, as specified by <code>ProjectionExpression</code>.</p>"""
    consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.consumed_capacity.ConsumedCapacity"
    ]
    """<p>The capacity units consumed by the <code>GetItem</code> operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. <code>ConsumedCapacity</code> is only returned if the <code>ReturnConsumedCapacity</code> parameter was specified. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/read-write-operations.html#read-operation-consumption\">Capacity unit consumption for read operations</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetItemOutput) -> dict:
    out: dict = {}
    if "item" in value:
        import aws_sdk_dynamodb.types.attribute_map

        out["Item"] = aws_sdk_dynamodb.types.attribute_map.serialize_aws_json_1_0(
            value["item"]
        )
    if "consumed_capacity" in value:
        import aws_sdk_dynamodb.types.consumed_capacity

        out["ConsumedCapacity"] = (
            aws_sdk_dynamodb.types.consumed_capacity.serialize_aws_json_1_0(
                value["consumed_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetItemOutput:
    out: GetItemOutput = {}  # type: ignore[typeddict-item]
    if "Item" in data:
        import aws_sdk_dynamodb.types.attribute_map

        out["item"] = aws_sdk_dynamodb.types.attribute_map.deserialize_aws_json_1_0(
            data["Item"]
        )
    if "ConsumedCapacity" in data:
        import aws_sdk_dynamodb.types.consumed_capacity

        out["consumed_capacity"] = (
            aws_sdk_dynamodb.types.consumed_capacity.deserialize_aws_json_1_0(
                data["ConsumedCapacity"]
            )
        )
    return out
