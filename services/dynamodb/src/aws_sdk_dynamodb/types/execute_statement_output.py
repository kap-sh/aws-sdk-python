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
