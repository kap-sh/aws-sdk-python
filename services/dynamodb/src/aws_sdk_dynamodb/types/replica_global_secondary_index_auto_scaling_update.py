"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexAutoScalingUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_settings_update
    import aws_sdk_dynamodb.types.index_name


class ReplicaGlobalSecondaryIndexAutoScalingUpdate(TypedDict):
    index_name: NotRequired["aws_sdk_dynamodb.types.index_name.IndexName"]
    """<p>The name of the global secondary index.</p>"""
    provisioned_read_capacity_auto_scaling_update: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_settings_update.AutoScalingSettingsUpdate"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaGlobalSecondaryIndexAutoScalingUpdate) -> dict:
    out: dict = {}
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    if "provisioned_read_capacity_auto_scaling_update" in value:
        import aws_sdk_dynamodb.types.auto_scaling_settings_update

        out["ProvisionedReadCapacityAutoScalingUpdate"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_update.serialize_aws_json_1_0(
                value["provisioned_read_capacity_auto_scaling_update"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ReplicaGlobalSecondaryIndexAutoScalingUpdate:
    out: ReplicaGlobalSecondaryIndexAutoScalingUpdate = {}  # type: ignore[typeddict-item]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    if "ProvisionedReadCapacityAutoScalingUpdate" in data:
        import aws_sdk_dynamodb.types.auto_scaling_settings_update

        out["provisioned_read_capacity_auto_scaling_update"] = (
            aws_sdk_dynamodb.types.auto_scaling_settings_update.deserialize_aws_json_1_0(
                data["ProvisionedReadCapacityAutoScalingUpdate"]
            )
        )
    return out
