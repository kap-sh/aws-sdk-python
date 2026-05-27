"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactGetItem``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.get


class TransactGetItem(TypedDict):
    get: "aws_sdk_dynamodb.types.get.Get"
    """<p>Contains the primary key that identifies the item to get, together with the name of the table that contains the item, and optionally the specific attributes of the item to retrieve.</p>"""
