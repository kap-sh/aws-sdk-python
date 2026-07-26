"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaAutoScalingDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.auto_scaling_settings_description
    import capo_dynamodb.types.region_name
    import capo_dynamodb.types.replica_global_secondary_index_auto_scaling_description_list
    import capo_dynamodb.types.replica_status


class ReplicaAutoScalingDescription(TypedDict, closed=True):
    region_name: NotRequired["capo_dynamodb.types.region_name.RegionName"]
    """<p>The Region where the replica exists.</p>"""
    global_secondary_indexes: NotRequired[
        "capo_dynamodb.types.replica_global_secondary_index_auto_scaling_description_list.ReplicaGlobalSecondaryIndexAutoScalingDescriptionList"
    ]
    """<p>Replica-specific global secondary index auto scaling settings.</p>"""
    replica_provisioned_read_capacity_auto_scaling_settings: NotRequired[
        "capo_dynamodb.types.auto_scaling_settings_description.AutoScalingSettingsDescription"
    ]
    replica_provisioned_write_capacity_auto_scaling_settings: NotRequired[
        "capo_dynamodb.types.auto_scaling_settings_description.AutoScalingSettingsDescription"
    ]
    replica_status: NotRequired["capo_dynamodb.types.replica_status.ReplicaStatus"]
    """<p>The current state of the replica:</p> <ul> <li> <p> <code>CREATING</code> - The replica is being created.</p> </li> <li> <p> <code>UPDATING</code> - The replica is being updated.</p> </li> <li> <p> <code>DELETING</code> - The replica is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The replica is ready for use.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaAutoScalingDescription) -> dict:
    out: dict = {}
    if "region_name" in value:
        out["RegionName"] = value["region_name"]
    if "global_secondary_indexes" in value:
        import capo_dynamodb.types.replica_global_secondary_index_auto_scaling_description_list

        out["GlobalSecondaryIndexes"] = (
            capo_dynamodb.types.replica_global_secondary_index_auto_scaling_description_list.serialize_aws_json_1_0(
                value["global_secondary_indexes"]
            )
        )
    if "replica_provisioned_read_capacity_auto_scaling_settings" in value:
        import capo_dynamodb.types.auto_scaling_settings_description

        out["ReplicaProvisionedReadCapacityAutoScalingSettings"] = (
            capo_dynamodb.types.auto_scaling_settings_description.serialize_aws_json_1_0(
                value["replica_provisioned_read_capacity_auto_scaling_settings"]
            )
        )
    if "replica_provisioned_write_capacity_auto_scaling_settings" in value:
        import capo_dynamodb.types.auto_scaling_settings_description

        out["ReplicaProvisionedWriteCapacityAutoScalingSettings"] = (
            capo_dynamodb.types.auto_scaling_settings_description.serialize_aws_json_1_0(
                value["replica_provisioned_write_capacity_auto_scaling_settings"]
            )
        )
    if "replica_status" in value:
        import capo_dynamodb.types.replica_status

        out["ReplicaStatus"] = (
            capo_dynamodb.types.replica_status.serialize_aws_json_1_0(
                value["replica_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicaAutoScalingDescription:
    out: ReplicaAutoScalingDescription = {}  # type: ignore[typeddict-item]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    if "GlobalSecondaryIndexes" in data:
        import capo_dynamodb.types.replica_global_secondary_index_auto_scaling_description_list

        out["global_secondary_indexes"] = (
            capo_dynamodb.types.replica_global_secondary_index_auto_scaling_description_list.deserialize_aws_json_1_0(
                data["GlobalSecondaryIndexes"]
            )
        )
    if "ReplicaProvisionedReadCapacityAutoScalingSettings" in data:
        import capo_dynamodb.types.auto_scaling_settings_description

        out["replica_provisioned_read_capacity_auto_scaling_settings"] = (
            capo_dynamodb.types.auto_scaling_settings_description.deserialize_aws_json_1_0(
                data["ReplicaProvisionedReadCapacityAutoScalingSettings"]
            )
        )
    if "ReplicaProvisionedWriteCapacityAutoScalingSettings" in data:
        import capo_dynamodb.types.auto_scaling_settings_description

        out["replica_provisioned_write_capacity_auto_scaling_settings"] = (
            capo_dynamodb.types.auto_scaling_settings_description.deserialize_aws_json_1_0(
                data["ReplicaProvisionedWriteCapacityAutoScalingSettings"]
            )
        )
    if "ReplicaStatus" in data:
        import capo_dynamodb.types.replica_status

        out["replica_status"] = (
            capo_dynamodb.types.replica_status.deserialize_aws_json_1_0(
                data["ReplicaStatus"]
            )
        )
    return out
