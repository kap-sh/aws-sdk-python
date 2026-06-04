"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateTableReplicaAutoScalingInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import DeserializationError

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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTableReplicaAutoScalingInput) -> dict:
    out: dict = {}
    if "global_secondary_index_updates" in value:
        import aws_sdk_dynamodb.types.global_secondary_index_auto_scaling_update_list

        out["GlobalSecondaryIndexUpdates"] = (
            aws_sdk_dynamodb.types.global_secondary_index_auto_scaling_update_list.serialize_aws_json_1_0(
                value["global_secondary_index_updates"]
            )
        )
    out["TableName"] = value["table_name"]
    if "provisioned_write_capacity_auto_scaling_update" in value:
        import aws_sdk_dynamodb.types.auto_scaling_settings_update

        out["ProvisionedWriteCapacityAutoScalingUpdate"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_update.serialize_aws_json_1_0(
                value["provisioned_write_capacity_auto_scaling_update"]
            )
        )
    if "replica_updates" in value:
        import aws_sdk_dynamodb.types.replica_auto_scaling_update_list

        out["ReplicaUpdates"] = (
            aws_sdk_dynamodb.types.replica_auto_scaling_update_list.serialize_aws_json_1_0(
                value["replica_updates"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateTableReplicaAutoScalingInput:
    out: UpdateTableReplicaAutoScalingInput = {}  # type: ignore[typeddict-item]
    if "GlobalSecondaryIndexUpdates" in data:
        import aws_sdk_dynamodb.types.global_secondary_index_auto_scaling_update_list

        out["global_secondary_index_updates"] = (
            aws_sdk_dynamodb.types.global_secondary_index_auto_scaling_update_list.deserialize_aws_json_1_0(
                data["GlobalSecondaryIndexUpdates"]
            )
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "UpdateTableReplicaAutoScalingInput.table_name required"
        )
    if "ProvisionedWriteCapacityAutoScalingUpdate" in data:
        import aws_sdk_dynamodb.types.auto_scaling_settings_update

        out["provisioned_write_capacity_auto_scaling_update"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_update.deserialize_aws_json_1_0(
                data["ProvisionedWriteCapacityAutoScalingUpdate"]
            )
        )
    if "ReplicaUpdates" in data:
        import aws_sdk_dynamodb.types.replica_auto_scaling_update_list

        out["replica_updates"] = (
            aws_sdk_dynamodb.types.replica_auto_scaling_update_list.deserialize_aws_json_1_0(
                data["ReplicaUpdates"]
            )
        )
    return out
