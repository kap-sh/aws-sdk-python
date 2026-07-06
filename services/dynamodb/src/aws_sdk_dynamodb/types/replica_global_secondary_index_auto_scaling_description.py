"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexAutoScalingDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_settings_description
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.index_status


class ReplicaGlobalSecondaryIndexAutoScalingDescription(TypedDict, closed=True):
    index_name: NotRequired["aws_sdk_dynamodb.types.index_name.IndexName"]
    """<p>The name of the global secondary index.</p>"""
    index_status: NotRequired["aws_sdk_dynamodb.types.index_status.IndexStatus"]
    """<p>The current state of the replica global secondary index:</p> <ul> <li> <p> <code>CREATING</code> - The index is being created.</p> </li> <li> <p> <code>UPDATING</code> - The table/index configuration is being updated. The table/index remains available for data operations when <code>UPDATING</code> </p> </li> <li> <p> <code>DELETING</code> - The index is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The index is ready for use.</p> </li> </ul>"""
    provisioned_read_capacity_auto_scaling_settings: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_description.AutoScalingSettingsDescription"
    ]
    provisioned_write_capacity_auto_scaling_settings: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_description.AutoScalingSettingsDescription"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ReplicaGlobalSecondaryIndexAutoScalingDescription,
) -> dict:
    out: dict = {}
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    if "index_status" in value:
        import aws_sdk_dynamodb.types.index_status

        out["IndexStatus"] = aws_sdk_dynamodb.types.index_status.serialize_aws_json_1_0(
            value["index_status"]
        )
    if "provisioned_read_capacity_auto_scaling_settings" in value:
        import aws_sdk_dynamodb.types.auto_scaling_settings_description

        out["ProvisionedReadCapacityAutoScalingSettings"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_description.serialize_aws_json_1_0(
                value["provisioned_read_capacity_auto_scaling_settings"]
            )
        )
    if "provisioned_write_capacity_auto_scaling_settings" in value:
        import aws_sdk_dynamodb.types.auto_scaling_settings_description

        out["ProvisionedWriteCapacityAutoScalingSettings"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_description.serialize_aws_json_1_0(
                value["provisioned_write_capacity_auto_scaling_settings"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ReplicaGlobalSecondaryIndexAutoScalingDescription:
    out: ReplicaGlobalSecondaryIndexAutoScalingDescription = {}  # type: ignore[typeddict-item]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    if "IndexStatus" in data:
        import aws_sdk_dynamodb.types.index_status

        out["index_status"] = (
            aws_sdk_dynamodb.types.index_status.deserialize_aws_json_1_0(
                data["IndexStatus"]
            )
        )
    if "ProvisionedReadCapacityAutoScalingSettings" in data:
        import aws_sdk_dynamodb.types.auto_scaling_settings_description

        out["provisioned_read_capacity_auto_scaling_settings"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_description.deserialize_aws_json_1_0(
                data["ProvisionedReadCapacityAutoScalingSettings"]
            )
        )
    if "ProvisionedWriteCapacityAutoScalingSettings" in data:
        import aws_sdk_dynamodb.types.auto_scaling_settings_description

        out["provisioned_write_capacity_auto_scaling_settings"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_description.deserialize_aws_json_1_0(
                data["ProvisionedWriteCapacityAutoScalingSettings"]
            )
        )
    return out
