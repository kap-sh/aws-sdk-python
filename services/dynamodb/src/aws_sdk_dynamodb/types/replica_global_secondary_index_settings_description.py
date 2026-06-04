"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexSettingsDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_settings_description
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.index_status
    import aws_sdk_dynamodb.types.positive_long_object


class ReplicaGlobalSecondaryIndexSettingsDescription(TypedDict):
    index_name: "aws_sdk_dynamodb.types.index_name.IndexName"
    """<p>The name of the global secondary index. The name must be unique among all other indexes on this table.</p>"""
    index_status: NotRequired["aws_sdk_dynamodb.types.index_status.IndexStatus"]
    """<p> The current status of the global secondary index:</p> <ul> <li> <p> <code>CREATING</code> - The global secondary index is being created.</p> </li> <li> <p> <code>UPDATING</code> - The global secondary index is being updated.</p> </li> <li> <p> <code>DELETING</code> - The global secondary index is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The global secondary index is ready for use.</p> </li> </ul>"""
    provisioned_read_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum number of strongly consistent reads consumed per second before DynamoDB returns a <code>ThrottlingException</code>.</p>"""
    provisioned_read_capacity_auto_scaling_settings: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_description.AutoScalingSettingsDescription"
    ]
    """<p>Auto scaling settings for a global secondary index replica's read capacity units.</p>"""
    provisioned_write_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum number of writes consumed per second before DynamoDB returns a <code>ThrottlingException</code>.</p>"""
    provisioned_write_capacity_auto_scaling_settings: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_description.AutoScalingSettingsDescription"
    ]
    """<p>Auto scaling settings for a global secondary index replica's write capacity units.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ReplicaGlobalSecondaryIndexSettingsDescription,
) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    if "index_status" in value:
        import aws_sdk_dynamodb.types.index_status

        out["IndexStatus"] = aws_sdk_dynamodb.types.index_status.serialize_aws_json_1_0(
            value["index_status"]
        )
    if "provisioned_read_capacity_units" in value:
        out["ProvisionedReadCapacityUnits"] = value["provisioned_read_capacity_units"]
    if "provisioned_read_capacity_auto_scaling_settings" in value:
        import aws_sdk_dynamodb.types.auto_scaling_settings_description

        out["ProvisionedReadCapacityAutoScalingSettings"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_description.serialize_aws_json_1_0(
                value["provisioned_read_capacity_auto_scaling_settings"]
            )
        )
    if "provisioned_write_capacity_units" in value:
        out["ProvisionedWriteCapacityUnits"] = value["provisioned_write_capacity_units"]
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
) -> ReplicaGlobalSecondaryIndexSettingsDescription:
    out: ReplicaGlobalSecondaryIndexSettingsDescription = {}  # type: ignore[typeddict-item]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    else:
        raise DeserializationError(
            "ReplicaGlobalSecondaryIndexSettingsDescription.index_name required"
        )
    if "IndexStatus" in data:
        import aws_sdk_dynamodb.types.index_status

        out["index_status"] = (
            aws_sdk_dynamodb.types.index_status.deserialize_aws_json_1_0(
                data["IndexStatus"]
            )
        )
    if "ProvisionedReadCapacityUnits" in data:
        out["provisioned_read_capacity_units"] = data["ProvisionedReadCapacityUnits"]
    if "ProvisionedReadCapacityAutoScalingSettings" in data:
        import aws_sdk_dynamodb.types.auto_scaling_settings_description

        out["provisioned_read_capacity_auto_scaling_settings"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_description.deserialize_aws_json_1_0(
                data["ProvisionedReadCapacityAutoScalingSettings"]
            )
        )
    if "ProvisionedWriteCapacityUnits" in data:
        out["provisioned_write_capacity_units"] = data["ProvisionedWriteCapacityUnits"]
    if "ProvisionedWriteCapacityAutoScalingSettings" in data:
        import aws_sdk_dynamodb.types.auto_scaling_settings_description

        out["provisioned_write_capacity_auto_scaling_settings"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_description.deserialize_aws_json_1_0(
                data["ProvisionedWriteCapacityAutoScalingSettings"]
            )
        )
    return out
