"""Generated from Smithy shape ``com.amazonaws.dynamodb#SourceTableDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.billing_mode
    import aws_sdk_dynamodb.types.item_count
    import aws_sdk_dynamodb.types.key_schema
    import aws_sdk_dynamodb.types.long_object
    import aws_sdk_dynamodb.types.on_demand_throughput
    import aws_sdk_dynamodb.types.provisioned_throughput
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.table_creation_date_time
    import aws_sdk_dynamodb.types.table_id
    import aws_sdk_dynamodb.types.table_name


class SourceTableDetails(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_name.TableName"
    """<p>The name of the table for which the backup was created. </p>"""
    table_id: "aws_sdk_dynamodb.types.table_id.TableId"
    """<p>Unique identifier for the table for which the backup was created. </p>"""
    table_arn: NotRequired["aws_sdk_dynamodb.types.table_arn.TableArn"]
    """<p>ARN of the table for which backup was created. </p>"""
    table_size_bytes: NotRequired["aws_sdk_dynamodb.types.long_object.LongObject"]
    """<p>Size of the table in bytes. Note that this is an approximate value.</p>"""
    key_schema: "aws_sdk_dynamodb.types.key_schema.KeySchema"
    """<p>Schema of the table. </p>"""
    table_creation_date_time: (
        "aws_sdk_dynamodb.types.table_creation_date_time.TableCreationDateTime"
    )
    """<p>Time when the source table was created. </p>"""
    provisioned_throughput: (
        "aws_sdk_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    )
    """<p>Read IOPs and Write IOPS on the table when the backup was created.</p>"""
    on_demand_throughput: NotRequired[
        "aws_sdk_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
    item_count: NotRequired["aws_sdk_dynamodb.types.item_count.ItemCount"]
    """<p>Number of items in the table. Note that this is an approximate value. </p>"""
    billing_mode: NotRequired["aws_sdk_dynamodb.types.billing_mode.BillingMode"]
    """<p>Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.</p> <ul> <li> <p> <code>PROVISIONED</code> - Sets the read/write capacity mode to <code>PROVISIONED</code>. We recommend using <code>PROVISIONED</code> for predictable workloads.</p> </li> <li> <p> <code>PAY_PER_REQUEST</code> - Sets the read/write capacity mode to <code>PAY_PER_REQUEST</code>. We recommend using <code>PAY_PER_REQUEST</code> for unpredictable workloads. </p> </li> </ul>"""
