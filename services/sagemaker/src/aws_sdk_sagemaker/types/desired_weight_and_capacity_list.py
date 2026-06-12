"""Generated from Smithy shape ``com.amazonaws.sagemaker#DesiredWeightAndCapacityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.desired_weight_and_capacity

DesiredWeightAndCapacityList: TypeAlias = list[
    "aws_sdk_sagemaker.types.desired_weight_and_capacity.DesiredWeightAndCapacity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DesiredWeightAndCapacityList) -> list:
    import aws_sdk_sagemaker.types.desired_weight_and_capacity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.desired_weight_and_capacity.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DesiredWeightAndCapacityList:
    import aws_sdk_sagemaker.types.desired_weight_and_capacity

    out: DesiredWeightAndCapacityList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.desired_weight_and_capacity.deserialize_aws_json_1_1(
                item
            )
        )
    return out
