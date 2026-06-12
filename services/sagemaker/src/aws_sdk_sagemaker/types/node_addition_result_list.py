"""Generated from Smithy shape ``com.amazonaws.sagemaker#NodeAdditionResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.node_addition_result

NodeAdditionResultList: TypeAlias = list[
    "aws_sdk_sagemaker.types.node_addition_result.NodeAdditionResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeAdditionResultList) -> list:
    import aws_sdk_sagemaker.types.node_addition_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.node_addition_result.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NodeAdditionResultList:
    import aws_sdk_sagemaker.types.node_addition_result

    out: NodeAdditionResultList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.node_addition_result.deserialize_aws_json_1_1(item)
        )
    return out
