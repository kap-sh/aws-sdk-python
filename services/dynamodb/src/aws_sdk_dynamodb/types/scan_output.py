"""Generated from Smithy shape ``com.amazonaws.dynamodb#ScanOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.consumed_capacity
    import aws_sdk_dynamodb.types.integer
    import aws_sdk_dynamodb.types.item_list
    import aws_sdk_dynamodb.types.key


class ScanOutput(TypedDict):
    items: NotRequired["aws_sdk_dynamodb.types.item_list.ItemList"]
    """<p>An array of item attributes that match the scan criteria. Each element in this array consists of an attribute name and the value for that attribute.</p>"""
    count: "aws_sdk_dynamodb.types.integer.Integer"
    """<p>The number of items in the response.</p> <p>If you set <code>ScanFilter</code> in the request, then <code>Count</code> is the number of items returned after the filter was applied, and <code>ScannedCount</code> is the number of matching items before the filter was applied.</p> <p>If you did not use a filter in the request, then <code>Count</code> is the same as <code>ScannedCount</code>.</p>"""
    scanned_count: "aws_sdk_dynamodb.types.integer.Integer"
    """<p>The number of items evaluated, before any <code>ScanFilter</code> is applied. A high <code>ScannedCount</code> value with few, or no, <code>Count</code> results indicates an inefficient <code>Scan</code> operation. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html#Count\">Count and ScannedCount</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p>If you did not use a filter in the request, then <code>ScannedCount</code> is the same as <code>Count</code>.</p>"""
    last_evaluated_key: NotRequired["aws_sdk_dynamodb.types.key.Key"]
    """<p>The primary key of the item where the operation stopped, inclusive of the previous result set. Use this value to start a new operation, excluding this value in the new request.</p> <p>If <code>LastEvaluatedKey</code> is empty, then the \"last page\" of results has been processed and there is no more data to be retrieved.</p> <p>If <code>LastEvaluatedKey</code> is not empty, it does not necessarily mean that there is more data in the result set. The only way to know when you have reached the end of the result set is when <code>LastEvaluatedKey</code> is empty.</p>"""
    consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.consumed_capacity.ConsumedCapacity"
    ]
    """<p>The capacity units consumed by the <code>Scan</code> operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. <code>ConsumedCapacity</code> is only returned if the <code>ReturnConsumedCapacity</code> parameter was specified. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/read-write-operations.html#read-operation-consumption\">Capacity unit consumption for read operations</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScanOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_dynamodb.types.item_list

        out["Items"] = aws_sdk_dynamodb.types.item_list.serialize_aws_json_1_0(
            value["items"]
        )
    out["Count"] = value.get("count", 0)
    out["ScannedCount"] = value.get("scanned_count", 0)
    if "last_evaluated_key" in value:
        import aws_sdk_dynamodb.types.key

        out["LastEvaluatedKey"] = aws_sdk_dynamodb.types.key.serialize_aws_json_1_0(
            value["last_evaluated_key"]
        )
    if "consumed_capacity" in value:
        import aws_sdk_dynamodb.types.consumed_capacity

        out["ConsumedCapacity"] = (
            aws_sdk_dynamodb.types.consumed_capacity.serialize_aws_json_1_0(
                value["consumed_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ScanOutput:
    out: ScanOutput = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_dynamodb.types.item_list

        out["items"] = aws_sdk_dynamodb.types.item_list.deserialize_aws_json_1_0(
            data["Items"]
        )
    if "Count" in data:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    if "ScannedCount" in data:
        out["scanned_count"] = data["ScannedCount"]
    else:
        out["scanned_count"] = 0
    if "LastEvaluatedKey" in data:
        import aws_sdk_dynamodb.types.key

        out["last_evaluated_key"] = aws_sdk_dynamodb.types.key.deserialize_aws_json_1_0(
            data["LastEvaluatedKey"]
        )
    if "ConsumedCapacity" in data:
        import aws_sdk_dynamodb.types.consumed_capacity

        out["consumed_capacity"] = (
            aws_sdk_dynamodb.types.consumed_capacity.deserialize_aws_json_1_0(
                data["ConsumedCapacity"]
            )
        )
    return out
