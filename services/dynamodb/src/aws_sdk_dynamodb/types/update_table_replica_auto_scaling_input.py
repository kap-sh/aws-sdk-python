"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateTableReplicaAutoScalingInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_settings_update
    import aws_sdk_dynamodb.types.global_secondary_index_auto_scaling_update_list
    import aws_sdk_dynamodb.types.replica_auto_scaling_update_list
    import aws_sdk_dynamodb.types.table_arn


class UpdateTableReplicaAutoScalingInput(TypedDict):
    global_secondary_index_updates: NotRequired[
        "aws_sdk_dynamodb.types.global_secondary_index_auto_scaling_update_list.GlobalSecondaryIndexAutoScalingUpdateList"
    ]
    """<p>Represents the auto scaling settings of the global secondary indexes of the replica to be updated.</p>"""
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The name of the global table to be updated. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    provisioned_write_capacity_auto_scaling_update: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_update.AutoScalingSettingsUpdate"
    ]
    replica_updates: NotRequired[
        "aws_sdk_dynamodb.types.replica_auto_scaling_update_list.ReplicaAutoScalingUpdateList"
    ]
    """<p>Represents the auto scaling settings of replicas of the table that will be modified.</p>"""
