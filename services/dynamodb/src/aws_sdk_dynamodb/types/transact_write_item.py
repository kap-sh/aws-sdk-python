"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactWriteItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.condition_check
    import aws_sdk_dynamodb.types.delete
    import aws_sdk_dynamodb.types.put
    import aws_sdk_dynamodb.types.update


class TransactWriteItem(TypedDict):
    condition_check: NotRequired[
        "aws_sdk_dynamodb.types.condition_check.ConditionCheck"
    ]
    """<p>A request to perform a check item operation.</p>"""
    put: NotRequired["aws_sdk_dynamodb.types.put.Put"]
    """<p>A request to perform a <code>PutItem</code> operation.</p>"""
    delete: NotRequired["aws_sdk_dynamodb.types.delete.Delete"]
    """<p>A request to perform a <code>DeleteItem</code> operation.</p>"""
    update: NotRequired["aws_sdk_dynamodb.types.update.Update"]
    """<p>A request to perform an <code>UpdateItem</code> operation.</p>"""
