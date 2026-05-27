"""Generated from Smithy shape ``com.amazonaws.dynamodb#LocalSecondaryIndexDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.key_schema
    import aws_sdk_dynamodb.types.long_object
    import aws_sdk_dynamodb.types.projection
    import aws_sdk_dynamodb.types.string


class LocalSecondaryIndexDescription(TypedDict):
    index_name: NotRequired["aws_sdk_dynamodb.types.index_name.IndexName"]
    """<p>Represents the name of the local secondary index.</p>"""
    key_schema: NotRequired["aws_sdk_dynamodb.types.key_schema.KeySchema"]
    """<p>The complete key schema for the local secondary index, consisting of one or more pairs of attribute names and key types:</p> <ul> <li> <p> <code>HASH</code> - partition key</p> </li> <li> <p> <code>RANGE</code> - sort key</p> </li> </ul> <note> <p>The partition key of an item is also known as its <i>hash attribute</i>. The term \"hash attribute\" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.</p> <p>The sort key of an item is also known as its <i>range attribute</i>. The term \"range attribute\" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.</p> </note>"""
    projection: NotRequired["aws_sdk_dynamodb.types.projection.Projection"]
    """<p>Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. </p>"""
    index_size_bytes: NotRequired["aws_sdk_dynamodb.types.long_object.LongObject"]
    """<p>The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.</p>"""
    item_count: NotRequired["aws_sdk_dynamodb.types.long_object.LongObject"]
    """<p>The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.</p>"""
    index_arn: NotRequired["aws_sdk_dynamodb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the index.</p>"""
