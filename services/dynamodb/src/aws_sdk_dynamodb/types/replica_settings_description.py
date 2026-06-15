"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaSettingsDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_settings_description
    import aws_sdk_dynamodb.types.billing_mode_summary
    import aws_sdk_dynamodb.types.non_negative_long_object
    import aws_sdk_dynamodb.types.region_name
    import aws_sdk_dynamodb.types.replica_global_secondary_index_settings_description_list
    import aws_sdk_dynamodb.types.replica_status
    import aws_sdk_dynamodb.types.table_class_summary


class ReplicaSettingsDescription(TypedDict):
    region_name: "aws_sdk_dynamodb.types.region_name.RegionName"
    """<p>The Region name of the replica.</p>"""
    replica_status: NotRequired["aws_sdk_dynamodb.types.replica_status.ReplicaStatus"]
    """<p>The current state of the Region:</p> <ul> <li> <p> <code>CREATING</code> - The Region is being created.</p> </li> <li> <p> <code>UPDATING</code> - The Region is being updated.</p> </li> <li> <p> <code>DELETING</code> - The Region is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The Region is ready for use.</p> </li> </ul>"""
    replica_billing_mode_summary: NotRequired[
        "aws_sdk_dynamodb.types.billing_mode_summary.BillingModeSummary"
    ]
    """<p>The read/write capacity mode of the replica.</p>"""
    replica_provisioned_read_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.non_negative_long_object.NonNegativeLongObject"
    ]
    r"""<p>The maximum number of strongly consistent reads consumed per second before DynamoDB returns a <code>ThrottlingException</code>. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput\">Specifying Read and Write Requirements</a> in the <i>Amazon DynamoDB Developer Guide</i>. </p>"""
    replica_provisioned_read_capacity_auto_scaling_settings: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_description.AutoScalingSettingsDescription"
    ]
    """<p>Auto scaling settings for a global table replica's read capacity units.</p>"""
    replica_provisioned_write_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.non_negative_long_object.NonNegativeLongObject"
    ]
    r"""<p>The maximum number of writes consumed per second before DynamoDB returns a <code>ThrottlingException</code>. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput\">Specifying Read and Write Requirements</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    replica_provisioned_write_capacity_auto_scaling_settings: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_description.AutoScalingSettingsDescription"
    ]
    """<p>Auto scaling settings for a global table replica's write capacity units.</p>"""
    replica_global_secondary_index_settings: NotRequired[
        "aws_sdk_dynamodb.types.replica_global_secondary_index_settings_description_list.ReplicaGlobalSecondaryIndexSettingsDescriptionList"
    ]
    """<p>Replica global secondary index settings for the global table.</p>"""
    replica_table_class_summary: NotRequired[
        "aws_sdk_dynamodb.types.table_class_summary.TableClassSummary"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaSettingsDescription) -> dict:
    out: dict = {}
    out["RegionName"] = value["region_name"]
    if "replica_status" in value:
        import aws_sdk_dynamodb.types.replica_status

        out["ReplicaStatus"] = (
            aws_sdk_dynamodb.types.replica_status.serialize_aws_json_1_0(
                value["replica_status"]
            )
        )
    if "replica_billing_mode_summary" in value:
        import aws_sdk_dynamodb.types.billing_mode_summary

        out["ReplicaBillingModeSummary"] = (
            aws_sdk_dynamodb.types.billing_mode_summary.serialize_aws_json_1_0(
                value["replica_billing_mode_summary"]
            )
        )
    if "replica_provisioned_read_capacity_units" in value:
        out["ReplicaProvisionedReadCapacityUnits"] = value[
            "replica_provisioned_read_capacity_units"
        ]
    if "replica_provisioned_read_capacity_auto_scaling_settings" in value:
        import aws_sdk_dynamodb.types.auto_scaling_settings_description

        out["ReplicaProvisionedReadCapacityAutoScalingSettings"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_description.serialize_aws_json_1_0(
                value["replica_provisioned_read_capacity_auto_scaling_settings"]
            )
        )
    if "replica_provisioned_write_capacity_units" in value:
        out["ReplicaProvisionedWriteCapacityUnits"] = value[
            "replica_provisioned_write_capacity_units"
        ]
    if "replica_provisioned_write_capacity_auto_scaling_settings" in value:
        import aws_sdk_dynamodb.types.auto_scaling_settings_description

        out["ReplicaProvisionedWriteCapacityAutoScalingSettings"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_description.serialize_aws_json_1_0(
                value["replica_provisioned_write_capacity_auto_scaling_settings"]
            )
        )
    if "replica_global_secondary_index_settings" in value:
        import aws_sdk_dynamodb.types.replica_global_secondary_index_settings_description_list

        out["ReplicaGlobalSecondaryIndexSettings"] = (
            aws_sdk_dynamodb.types.replica_global_secondary_index_settings_description_list.serialize_aws_json_1_0(
                value["replica_global_secondary_index_settings"]
            )
        )
    if "replica_table_class_summary" in value:
        import aws_sdk_dynamodb.types.table_class_summary

        out["ReplicaTableClassSummary"] = (
            aws_sdk_dynamodb.types.table_class_summary.serialize_aws_json_1_0(
                value["replica_table_class_summary"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicaSettingsDescription:
    out: ReplicaSettingsDescription = {}  # type: ignore[typeddict-item]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    else:
        raise DeserializationError("ReplicaSettingsDescription.region_name required")
    if "ReplicaStatus" in data:
        import aws_sdk_dynamodb.types.replica_status

        out["replica_status"] = (
            aws_sdk_dynamodb.types.replica_status.deserialize_aws_json_1_0(
                data["ReplicaStatus"]
            )
        )
    if "ReplicaBillingModeSummary" in data:
        import aws_sdk_dynamodb.types.billing_mode_summary

        out["replica_billing_mode_summary"] = (
            aws_sdk_dynamodb.types.billing_mode_summary.deserialize_aws_json_1_0(
                data["ReplicaBillingModeSummary"]
            )
        )
    if "ReplicaProvisionedReadCapacityUnits" in data:
        out["replica_provisioned_read_capacity_units"] = data[
            "ReplicaProvisionedReadCapacityUnits"
        ]
    if "ReplicaProvisionedReadCapacityAutoScalingSettings" in data:
        import aws_sdk_dynamodb.types.auto_scaling_settings_description

        out["replica_provisioned_read_capacity_auto_scaling_settings"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_description.deserialize_aws_json_1_0(
                data["ReplicaProvisionedReadCapacityAutoScalingSettings"]
            )
        )
    if "ReplicaProvisionedWriteCapacityUnits" in data:
        out["replica_provisioned_write_capacity_units"] = data[
            "ReplicaProvisionedWriteCapacityUnits"
        ]
    if "ReplicaProvisionedWriteCapacityAutoScalingSettings" in data:
        import aws_sdk_dynamodb.types.auto_scaling_settings_description

        out["replica_provisioned_write_capacity_auto_scaling_settings"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_description.deserialize_aws_json_1_0(
                data["ReplicaProvisionedWriteCapacityAutoScalingSettings"]
            )
        )
    if "ReplicaGlobalSecondaryIndexSettings" in data:
        import aws_sdk_dynamodb.types.replica_global_secondary_index_settings_description_list

        out["replica_global_secondary_index_settings"] = (
            aws_sdk_dynamodb.types.replica_global_secondary_index_settings_description_list.deserialize_aws_json_1_0(
                data["ReplicaGlobalSecondaryIndexSettings"]
            )
        )
    if "ReplicaTableClassSummary" in data:
        import aws_sdk_dynamodb.types.table_class_summary

        out["replica_table_class_summary"] = (
            aws_sdk_dynamodb.types.table_class_summary.deserialize_aws_json_1_0(
                data["ReplicaTableClassSummary"]
            )
        )
    return out
