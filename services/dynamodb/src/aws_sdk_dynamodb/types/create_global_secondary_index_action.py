"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateGlobalSecondaryIndexAction``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.key_schema
    import aws_sdk_dynamodb.types.on_demand_throughput
    import aws_sdk_dynamodb.types.projection
    import aws_sdk_dynamodb.types.provisioned_throughput
    import aws_sdk_dynamodb.types.warm_throughput


class CreateGlobalSecondaryIndexAction(TypedDict):
    index_name: "aws_sdk_dynamodb.types.index_name.IndexName"
    """<p>The name of the global secondary index to be created.</p>"""
    key_schema: "aws_sdk_dynamodb.types.key_schema.KeySchema"
    """<p>The key schema for the global secondary index. Global secondary index supports up to 4 partition and up to 4 sort keys.</p>"""
    projection: "aws_sdk_dynamodb.types.projection.Projection"
    """<p>Represents attributes that are copied (projected) from the table into an index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.</p>"""
    provisioned_throughput: NotRequired[
        "aws_sdk_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    ]
    """<p>Represents the provisioned throughput settings for the specified global secondary index.</p> <p>For current minimum and maximum provisioned throughput values, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html\">Service, Account, and Table Quotas</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    on_demand_throughput: NotRequired[
        "aws_sdk_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
    """<p>The maximum number of read and write units for the global secondary index being created. If you use this parameter, you must specify <code>MaxReadRequestUnits</code>, <code>MaxWriteRequestUnits</code>, or both. You must use either <code>OnDemand Throughput</code> or <code>ProvisionedThroughput</code> based on your table's capacity mode.</p>"""
    warm_throughput: NotRequired[
        "aws_sdk_dynamodb.types.warm_throughput.WarmThroughput"
    ]
    """<p>Represents the warm throughput value (in read units per second and write units per second) when creating a secondary index.</p>"""
