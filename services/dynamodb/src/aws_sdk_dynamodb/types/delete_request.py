"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.key


class DeleteRequest(TypedDict):
    key: "aws_sdk_dynamodb.types.key.Key"
    """<p>A map of attribute name to attribute values, representing the primary key of the item to delete. All of the table's primary key attributes must be specified, and their data types must match those of the table's key schema.</p>"""
