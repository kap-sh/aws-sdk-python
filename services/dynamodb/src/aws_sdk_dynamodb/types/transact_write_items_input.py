"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactWriteItemsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.client_request_token
    import aws_sdk_dynamodb.types.return_consumed_capacity
    import aws_sdk_dynamodb.types.return_item_collection_metrics
    import aws_sdk_dynamodb.types.transact_write_item_list


class TransactWriteItemsInput(TypedDict):
    transact_items: (
        "aws_sdk_dynamodb.types.transact_write_item_list.TransactWriteItemList"
    )
    """<p>An ordered array of up to 100 <code>TransactWriteItem</code> objects, each of which contains a <code>ConditionCheck</code>, <code>Put</code>, <code>Update</code>, or <code>Delete</code> object. These can operate on items in different tables, but the tables must reside in the same Amazon Web Services account and Region, and no two of them can operate on the same item. </p>"""
    return_consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]
    return_item_collection_metrics: NotRequired[
        "aws_sdk_dynamodb.types.return_item_collection_metrics.ReturnItemCollectionMetrics"
    ]
    """<p>Determines whether item collection metrics are returned. If set to <code>SIZE</code>, the response includes statistics about item collections (if any), that were modified during the operation and are returned in the response. If set to <code>NONE</code> (the default), no statistics are returned. </p>"""
    client_request_token: NotRequired[
        "aws_sdk_dynamodb.types.client_request_token.ClientRequestToken"
    ]
    """<p>Providing a <code>ClientRequestToken</code> makes the call to <code>TransactWriteItems</code> idempotent, meaning that multiple identical calls have the same effect as one single call.</p> <p>Although multiple identical calls using the same client request token produce the same result on the server (no side effects), the responses to the calls might not be the same. If the <code>ReturnConsumedCapacity</code> parameter is set, then the initial <code>TransactWriteItems</code> call returns the amount of write capacity units consumed in making the changes. Subsequent <code>TransactWriteItems</code> calls with the same client token return the number of read capacity units consumed in reading the item.</p> <p>A client request token is valid for 10 minutes after the first request that uses it is completed. After 10 minutes, any request with the same client token is treated as a new request. Do not resubmit the same request with the same client token for more than 10 minutes, or the result might not be idempotent.</p> <p>If you submit a request with the same client token but a change in other parameters within the 10-minute idempotency window, DynamoDB returns an <code>IdempotentParameterMismatch</code> exception.</p>"""
