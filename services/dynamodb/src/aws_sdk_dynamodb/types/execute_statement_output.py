"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExecuteStatementOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.consumed_capacity
    import aws_sdk_dynamodb.types.item_list
    import aws_sdk_dynamodb.types.key
    import aws_sdk_dynamodb.types.parti_ql_next_token


class ExecuteStatementOutput(TypedDict):
    items: NotRequired["aws_sdk_dynamodb.types.item_list.ItemList"]
    """<p>If a read operation was used, this property will contain the result of the read operation; a map of attribute names and their values. For the write operations this value will be empty.</p>"""
    next_token: NotRequired[
        "aws_sdk_dynamodb.types.parti_ql_next_token.PartiQLNextToken"
    ]
    """<p>If the response of a read request exceeds the response payload limit DynamoDB will set this value in the response. If set, you can use that this value in the subsequent request to get the remaining results.</p>"""
    consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.consumed_capacity.ConsumedCapacity"
    ]
    last_evaluated_key: NotRequired["aws_sdk_dynamodb.types.key.Key"]
    """<p>The primary key of the item where the operation stopped, inclusive of the previous result set. Use this value to start a new operation, excluding this value in the new request. If <code>LastEvaluatedKey</code> is empty, then the \"last page\" of results has been processed and there is no more data to be retrieved. If <code>LastEvaluatedKey</code> is not empty, it does not necessarily mean that there is more data in the result set. The only way to know when you have reached the end of the result set is when <code>LastEvaluatedKey</code> is empty. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecuteStatementOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_dynamodb.types.item_list

        out["Items"] = aws_sdk_dynamodb.types.item_list.serialize_aws_json_1_0(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "consumed_capacity" in value:
        import aws_sdk_dynamodb.types.consumed_capacity

        out["ConsumedCapacity"] = (
            aws_sdk_dynamodb.types.consumed_capacity.serialize_aws_json_1_0(
                value["consumed_capacity"]
            )
        )
    if "last_evaluated_key" in value:
        import aws_sdk_dynamodb.types.key

        out["LastEvaluatedKey"] = aws_sdk_dynamodb.types.key.serialize_aws_json_1_0(
            value["last_evaluated_key"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecuteStatementOutput:
    out: ExecuteStatementOutput = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_dynamodb.types.item_list

        out["items"] = aws_sdk_dynamodb.types.item_list.deserialize_aws_json_1_0(
            data["Items"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ConsumedCapacity" in data:
        import aws_sdk_dynamodb.types.consumed_capacity

        out["consumed_capacity"] = (
            aws_sdk_dynamodb.types.consumed_capacity.deserialize_aws_json_1_0(
                data["ConsumedCapacity"]
            )
        )
    if "LastEvaluatedKey" in data:
        import aws_sdk_dynamodb.types.key

        out["last_evaluated_key"] = aws_sdk_dynamodb.types.key.deserialize_aws_json_1_0(
            data["LastEvaluatedKey"]
        )
    return out
