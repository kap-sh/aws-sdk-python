"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaSettingsUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_settings_update
    import aws_sdk_dynamodb.types.positive_long_object
    import aws_sdk_dynamodb.types.region_name
    import aws_sdk_dynamodb.types.replica_global_secondary_index_settings_update_list
    import aws_sdk_dynamodb.types.table_class


class ReplicaSettingsUpdate(TypedDict):
    region_name: "aws_sdk_dynamodb.types.region_name.RegionName"
    """<p>The Region of the replica to be added.</p>"""
    replica_provisioned_read_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum number of strongly consistent reads consumed per second before DynamoDB returns a <code>ThrottlingException</code>. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput\">Specifying Read and Write Requirements</a> in the <i>Amazon DynamoDB Developer Guide</i>. </p>"""
    replica_provisioned_read_capacity_auto_scaling_settings_update: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_update.AutoScalingSettingsUpdate"
    ]
    """<p>Auto scaling settings for managing a global table replica's read capacity units.</p>"""
    replica_global_secondary_index_settings_update: NotRequired[
        "aws_sdk_dynamodb.types.replica_global_secondary_index_settings_update_list.ReplicaGlobalSecondaryIndexSettingsUpdateList"
    ]
    """<p>Represents the settings of a global secondary index for a global table that will be modified.</p>"""
    replica_table_class: NotRequired["aws_sdk_dynamodb.types.table_class.TableClass"]
    """<p>Replica-specific table class. If not specified, uses the source table's table class.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaSettingsUpdate) -> dict:
    out: dict = {}
    out["RegionName"] = value["region_name"]
    if "replica_provisioned_read_capacity_units" in value:
        out["ReplicaProvisionedReadCapacityUnits"] = value[
            "replica_provisioned_read_capacity_units"
        ]
    if "replica_provisioned_read_capacity_auto_scaling_settings_update" in value:
        import aws_sdk_dynamodb.types.auto_scaling_settings_update

        out["ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_update.serialize_aws_json_1_0(
                value["replica_provisioned_read_capacity_auto_scaling_settings_update"]
            )
        )
    if "replica_global_secondary_index_settings_update" in value:
        import aws_sdk_dynamodb.types.replica_global_secondary_index_settings_update_list

        out["ReplicaGlobalSecondaryIndexSettingsUpdate"] = (
            aws_sdk_dynamodb.types.replica_global_secondary_index_settings_update_list.serialize_aws_json_1_0(
                value["replica_global_secondary_index_settings_update"]
            )
        )
    if "replica_table_class" in value:
        import aws_sdk_dynamodb.types.table_class

        out["ReplicaTableClass"] = (
            aws_sdk_dynamodb.types.table_class.serialize_aws_json_1_0(
                value["replica_table_class"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicaSettingsUpdate:
    out: ReplicaSettingsUpdate = {}  # type: ignore[typeddict-item]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    else:
        raise DeserializationError("ReplicaSettingsUpdate.region_name required")
    if "ReplicaProvisionedReadCapacityUnits" in data:
        out["replica_provisioned_read_capacity_units"] = data[
            "ReplicaProvisionedReadCapacityUnits"
        ]
    if "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate" in data:
        import aws_sdk_dynamodb.types.auto_scaling_settings_update

        out["replica_provisioned_read_capacity_auto_scaling_settings_update"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_update.deserialize_aws_json_1_0(
                data["ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate"]
            )
        )
    if "ReplicaGlobalSecondaryIndexSettingsUpdate" in data:
        import aws_sdk_dynamodb.types.replica_global_secondary_index_settings_update_list

        out["replica_global_secondary_index_settings_update"] = (
            aws_sdk_dynamodb.types.replica_global_secondary_index_settings_update_list.deserialize_aws_json_1_0(
                data["ReplicaGlobalSecondaryIndexSettingsUpdate"]
            )
        )
    if "ReplicaTableClass" in data:
        import aws_sdk_dynamodb.types.table_class

        out["replica_table_class"] = (
            aws_sdk_dynamodb.types.table_class.deserialize_aws_json_1_0(
                data["ReplicaTableClass"]
            )
        )
    return out
