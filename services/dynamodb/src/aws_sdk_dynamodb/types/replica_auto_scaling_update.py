"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaAutoScalingUpdate``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_settings_update
    import aws_sdk_dynamodb.types.region_name
    import aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_update_list


class ReplicaAutoScalingUpdate(TypedDict):
    region_name: "aws_sdk_dynamodb.types.region_name.RegionName"
    """<p>The Region where the replica exists.</p>"""
    replica_global_secondary_index_updates: NotRequired[
        "aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_update_list.ReplicaGlobalSecondaryIndexAutoScalingUpdateList"
    ]
    """<p>Represents the auto scaling settings of global secondary indexes that will be modified.</p>"""
    replica_provisioned_read_capacity_auto_scaling_update: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_update.AutoScalingSettingsUpdate"
    ]
