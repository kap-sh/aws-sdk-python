"""Generated from Smithy shape ``com.amazonaws.dynamodb#RestoreTableToPointInTimeInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.billing_mode
    import aws_sdk_dynamodb.types.boolean_object
    import aws_sdk_dynamodb.types.date
    import aws_sdk_dynamodb.types.global_secondary_index_list
    import aws_sdk_dynamodb.types.local_secondary_index_list
    import aws_sdk_dynamodb.types.on_demand_throughput
    import aws_sdk_dynamodb.types.provisioned_throughput
    import aws_sdk_dynamodb.types.sse_specification
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.table_name


class RestoreTableToPointInTimeInput(TypedDict):
    source_table_arn: NotRequired["aws_sdk_dynamodb.types.table_arn.TableArn"]
    """<p>The DynamoDB table that will be restored. This value is an Amazon Resource Name (ARN).</p>"""
    source_table_name: NotRequired["aws_sdk_dynamodb.types.table_name.TableName"]
    """<p>Name of the source table that is being restored.</p>"""
    target_table_name: "aws_sdk_dynamodb.types.table_name.TableName"
    """<p>The name of the new table to which it must be restored to.</p>"""
    use_latest_restorable_time: NotRequired[
        "aws_sdk_dynamodb.types.boolean_object.BooleanObject"
    ]
    """<p>Restore the table to the latest possible time. <code>LatestRestorableDateTime</code> is typically 5 minutes before the current time. </p>"""
    restore_date_time: NotRequired["aws_sdk_dynamodb.types.date.Date"]
    """<p>Time in the past to restore the table to.</p>"""
    billing_mode_override: NotRequired[
        "aws_sdk_dynamodb.types.billing_mode.BillingMode"
    ]
    """<p>The billing mode of the restored table.</p>"""
    global_secondary_index_override: NotRequired[
        "aws_sdk_dynamodb.types.global_secondary_index_list.GlobalSecondaryIndexList"
    ]
    """<p>List of global secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.</p>"""
    local_secondary_index_override: NotRequired[
        "aws_sdk_dynamodb.types.local_secondary_index_list.LocalSecondaryIndexList"
    ]
    """<p>List of local secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.</p>"""
    provisioned_throughput_override: NotRequired[
        "aws_sdk_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
    ]
    """<p>Provisioned throughput settings for the restored table.</p>"""
    on_demand_throughput_override: NotRequired[
        "aws_sdk_dynamodb.types.on_demand_throughput.OnDemandThroughput"
    ]
    sse_specification_override: NotRequired[
        "aws_sdk_dynamodb.types.sse_specification.SSESpecification"
    ]
    """<p>The new server-side encryption settings for the restored table.</p>"""
