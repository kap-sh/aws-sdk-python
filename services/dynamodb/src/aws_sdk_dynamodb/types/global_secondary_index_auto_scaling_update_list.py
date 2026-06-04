"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndexAutoScalingUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_secondary_index_auto_scaling_update

GlobalSecondaryIndexAutoScalingUpdateList: TypeAlias = list[
    "aws_sdk_dynamodb.types.global_secondary_index_auto_scaling_update.GlobalSecondaryIndexAutoScalingUpdate"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalSecondaryIndexAutoScalingUpdateList) -> list:
    import aws_sdk_dynamodb.types.global_secondary_index_auto_scaling_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb.types.global_secondary_index_auto_scaling_update.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> GlobalSecondaryIndexAutoScalingUpdateList:
    import aws_sdk_dynamodb.types.global_secondary_index_auto_scaling_update

    out: GlobalSecondaryIndexAutoScalingUpdateList = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.global_secondary_index_auto_scaling_update.deserialize_aws_json_1_0(
                item
            )
        )
    return out
