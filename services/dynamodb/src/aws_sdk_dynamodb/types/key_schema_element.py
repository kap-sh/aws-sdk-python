"""Generated from Smithy shape ``com.amazonaws.dynamodb#KeySchemaElement``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.key_schema_attribute_name
    import aws_sdk_dynamodb.types.key_type


class KeySchemaElement(TypedDict):
    attribute_name: (
        "aws_sdk_dynamodb.types.key_schema_attribute_name.KeySchemaAttributeName"
    )
    """<p>The name of a key attribute.</p>"""
    key_type: "aws_sdk_dynamodb.types.key_type.KeyType"
    """<p>The role that this key attribute will assume:</p> <ul> <li> <p> <code>HASH</code> - partition key</p> </li> <li> <p> <code>RANGE</code> - sort key</p> </li> </ul> <note> <p>The partition key of an item is also known as its <i>hash attribute</i>. The term \"hash attribute\" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.</p> <p>The sort key of an item is also known as its <i>range attribute</i>. The term \"range attribute\" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.</p> </note>"""
