"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndex``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.key_schema
    import aws_sdk_dynamodb.types.on_demand_throughput
    import aws_sdk_dynamodb.types.projection
    import aws_sdk_dynamodb.types.provisioned_throughput
    import aws_sdk_dynamodb.types.warm_throughput


class GlobalSecondaryIndex(TypedDict):
    index_name: "aws_sdk_dynamodb.types.index_name.IndexName"
    """<p>The name of the global secondary index. The name must be unique among all other indexes on this table.</p>"""
    key_schema: "aws_sdk_dynamodb.types.key_schema.KeySchema"
    """<p>The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:</p> <ul> <li> <p> <code>HASH</code> - partition key</p> </li> <li> <p> <code>RANGE</code> - sort key</p> </li> </ul> <note> <p>The partition key of an item is also known as its <i>hash attribute</i>. The term \"hash attribute\" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.</p> <p>The sort key of an item is also known as its <i>range attribute</i>. The term \"range attribute\" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.</p> </note>"""
    projection: "aws_sdk_dynamodb.types.projection.Projection"
    """<p>Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. </p>"""
    provisioned_throughput: NotRequired[
        "aws_sdk_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    ]
    """<p>Represents the provisioned throughput settings for the specified global secondary index. You must use either <code>OnDemandThroughput</code> or <code>ProvisionedThroughput</code> based on your table's capacity mode.</p> <p>For current minimum and maximum provisioned throughput values, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html\">Service, Account, and Table Quotas</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    on_demand_throughput: NotRequired[
        "aws_sdk_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
    """<p>The maximum number of read and write units for the specified global secondary index. If you use this parameter, you must specify <code>MaxReadRequestUnits</code>, <code>MaxWriteRequestUnits</code>, or both. You must use either <code>OnDemandThroughput</code> or <code>ProvisionedThroughput</code> based on your table's capacity mode.</p>"""
    warm_throughput: NotRequired[
        "aws_sdk_dynamodb.types.warm_throughput.WarmThroughput"
    ]
    """<p>Represents the warm throughput value (in read units per second and write units per second) for the specified secondary index. If you use this parameter, you must specify <code>ReadUnitsPerSecond</code>, <code>WriteUnitsPerSecond</code>, or both.</p>"""
