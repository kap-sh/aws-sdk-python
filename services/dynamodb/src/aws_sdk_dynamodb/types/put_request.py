"""Generated from Smithy shape ``com.amazonaws.dynamodb#PutRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.put_item_input_attribute_map


class PutRequest(TypedDict):
    item: "aws_sdk_dynamodb.types.put_item_input_attribute_map.PutItemInputAttributeMap"
    """<p>A map of attribute name to attribute values, representing the primary key of an item to be processed by <code>PutItem</code>. All of the table's primary key attributes must be specified, and their data types must match those of the table's key schema. If any attributes are present in the item that are part of an index key schema for the table, their types must match the index key schema.</p>"""
