"""Generated from Smithy shape ``com.amazonaws.dynamodb#WriteRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.delete_request
    import aws_sdk_dynamodb.types.put_request


class WriteRequest(TypedDict):
    put_request: NotRequired["aws_sdk_dynamodb.types.put_request.PutRequest"]
    """<p>A request to perform a <code>PutItem</code> operation.</p>"""
    delete_request: NotRequired["aws_sdk_dynamodb.types.delete_request.DeleteRequest"]
    """<p>A request to perform a <code>DeleteItem</code> operation.</p>"""
