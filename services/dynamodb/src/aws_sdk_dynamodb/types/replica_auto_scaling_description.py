"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaAutoScalingDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_settings_description
    import aws_sdk_dynamodb.types.region_name
    import aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_description_list
    import aws_sdk_dynamodb.types.replica_status


class ReplicaAutoScalingDescription(TypedDict):
    region_name: NotRequired["aws_sdk_dynamodb.types.region_name.RegionName"]
    """<p>The Region where the replica exists.</p>"""
    global_secondary_indexes: NotRequired[
        "aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_description_list.ReplicaGlobalSecondaryIndexAutoScalingDescriptionList"
    ]
    """<p>Replica-specific global secondary index auto scaling settings.</p>"""
    replica_provisioned_read_capacity_auto_scaling_settings: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_description.AutoScalingSettingsDescription"
    ]
    replica_provisioned_write_capacity_auto_scaling_settings: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_description.AutoScalingSettingsDescription"
    ]
    replica_status: NotRequired["aws_sdk_dynamodb.types.replica_status.ReplicaStatus"]
    """<p>The current state of the replica:</p> <ul> <li> <p> <code>CREATING</code> - The replica is being created.</p> </li> <li> <p> <code>UPDATING</code> - The replica is being updated.</p> </li> <li> <p> <code>DELETING</code> - The replica is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The replica is ready for use.</p> </li> </ul>"""
