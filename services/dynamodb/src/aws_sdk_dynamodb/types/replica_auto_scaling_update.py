"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaAutoScalingUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_settings_update
    import aws_sdk_dynamodb.types.region_name
    import aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_update_list


class ReplicaAutoScalingUpdate(TypedDict, closed=True):
    region_name: "aws_sdk_dynamodb.types.region_name.RegionName"
    """<p>The Region where the replica exists.</p>"""
    replica_global_secondary_index_updates: NotRequired[
        "aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_update_list.ReplicaGlobalSecondaryIndexAutoScalingUpdateList"
    ]
    """<p>Represents the auto scaling settings of global secondary indexes that will be modified.</p>"""
    replica_provisioned_read_capacity_auto_scaling_update: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_update.AutoScalingSettingsUpdate"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaAutoScalingUpdate) -> dict:
    out: dict = {}
    out["RegionName"] = value["region_name"]
    if "replica_global_secondary_index_updates" in value:
        import aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_update_list

        out["ReplicaGlobalSecondaryIndexUpdates"] = (
            aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_update_list.serialize_aws_json_1_0(
                value["replica_global_secondary_index_updates"]
            )
        )
    if "replica_provisioned_read_capacity_auto_scaling_update" in value:
        import aws_sdk_dynamodb.types.auto_scaling_settings_update

        out["ReplicaProvisionedReadCapacityAutoScalingUpdate"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_update.serialize_aws_json_1_0(
                value["replica_provisioned_read_capacity_auto_scaling_update"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicaAutoScalingUpdate:
    out: ReplicaAutoScalingUpdate = {}  # type: ignore[typeddict-item]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    else:
        raise DeserializationError("ReplicaAutoScalingUpdate.region_name required")
    if "ReplicaGlobalSecondaryIndexUpdates" in data:
        import aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_update_list

        out["replica_global_secondary_index_updates"] = (
            aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_update_list.deserialize_aws_json_1_0(
                data["ReplicaGlobalSecondaryIndexUpdates"]
            )
        )
    if "ReplicaProvisionedReadCapacityAutoScalingUpdate" in data:
        import aws_sdk_dynamodb.types.auto_scaling_settings_update

        out["replica_provisioned_read_capacity_auto_scaling_update"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_update.deserialize_aws_json_1_0(
                data["ReplicaProvisionedReadCapacityAutoScalingUpdate"]
            )
        )
    return out
