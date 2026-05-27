"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndexInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.key_schema
    import aws_sdk_dynamodb.types.on_demand_throughput
    import aws_sdk_dynamodb.types.projection
    import aws_sdk_dynamodb.types.provisioned_throughput


class GlobalSecondaryIndexInfo(TypedDict):
    index_name: NotRequired["aws_sdk_dynamodb.types.index_name.IndexName"]
    """<p>The name of the global secondary index.</p>"""
    key_schema: NotRequired["aws_sdk_dynamodb.types.key_schema.KeySchema"]
    """<p>The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:</p> <ul> <li> <p> <code>HASH</code> - partition key</p> </li> <li> <p> <code>RANGE</code> - sort key</p> </li> </ul> <note> <p>The partition key of an item is also known as its <i>hash attribute</i>. The term \"hash attribute\" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.</p> <p>The sort key of an item is also known as its <i>range attribute</i>. The term \"range attribute\" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.</p> </note>"""
    projection: NotRequired["aws_sdk_dynamodb.types.projection.Projection"]
    """<p>Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. </p>"""
    provisioned_throughput: NotRequired[
        "aws_sdk_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    ]
    """<p>Represents the provisioned throughput settings for the specified global secondary index. </p>"""
    on_demand_throughput: NotRequired[
        "aws_sdk_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
