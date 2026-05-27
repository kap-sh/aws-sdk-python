"""Generated from Smithy shape ``com.amazonaws.dynamodb#RestoreTableFromBackupInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_arn
    import aws_sdk_dynamodb.types.billing_mode
    import aws_sdk_dynamodb.types.global_secondary_index_list
    import aws_sdk_dynamodb.types.local_secondary_index_list
    import aws_sdk_dynamodb.types.on_demand_throughput
    import aws_sdk_dynamodb.types.provisioned_throughput
    import aws_sdk_dynamodb.types.sse_specification
    import aws_sdk_dynamodb.types.table_name


class RestoreTableFromBackupInput(TypedDict):
    target_table_name: "aws_sdk_dynamodb.types.table_name.TableName"
    """<p>The name of the new table to which the backup must be restored.</p>"""
    backup_arn: "aws_sdk_dynamodb.types.backup_arn.BackupArn"
    """<p>The Amazon Resource Name (ARN) associated with the backup.</p>"""
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
