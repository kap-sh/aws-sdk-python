"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexSettingsUpdate``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_settings_update
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.positive_long_object


class ReplicaGlobalSecondaryIndexSettingsUpdate(TypedDict):
    index_name: "aws_sdk_dynamodb.types.index_name.IndexName"
    """<p>The name of the global secondary index. The name must be unique among all other indexes on this table.</p>"""
    provisioned_read_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The maximum number of strongly consistent reads consumed per second before DynamoDB returns a <code>ThrottlingException</code>.</p>"""
    provisioned_read_capacity_auto_scaling_settings_update: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_update.AutoScalingSettingsUpdate"
    ]
    """<p>Auto scaling settings for managing a global secondary index replica's read capacity units.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaGlobalSecondaryIndexSettingsUpdate) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    if "provisioned_read_capacity_units" in value:
        out["ProvisionedReadCapacityUnits"] = value["provisioned_read_capacity_units"]
    if "provisioned_read_capacity_auto_scaling_settings_update" in value:
        import aws_sdk_dynamodb.types.auto_scaling_settings_update

        out["ProvisionedReadCapacityAutoScalingSettingsUpdate"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_update.serialize_aws_json_1_0(
                value["provisioned_read_capacity_auto_scaling_settings_update"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicaGlobalSecondaryIndexSettingsUpdate:
    out: ReplicaGlobalSecondaryIndexSettingsUpdate = {}  # type: ignore[typeddict-item]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    else:
        raise DeserializationError(
            "ReplicaGlobalSecondaryIndexSettingsUpdate.index_name required"
        )
    if "ProvisionedReadCapacityUnits" in data:
        out["provisioned_read_capacity_units"] = data["ProvisionedReadCapacityUnits"]
    if "ProvisionedReadCapacityAutoScalingSettingsUpdate" in data:
        import aws_sdk_dynamodb.types.auto_scaling_settings_update

        out["provisioned_read_capacity_auto_scaling_settings_update"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_update.deserialize_aws_json_1_0(
                data["ProvisionedReadCapacityAutoScalingSettingsUpdate"]
            )
        )
    return out
