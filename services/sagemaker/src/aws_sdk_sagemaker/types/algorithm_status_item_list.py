"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlgorithmStatusItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.algorithm_status_item

AlgorithmStatusItemList: TypeAlias = list[
    "aws_sdk_sagemaker.types.algorithm_status_item.AlgorithmStatusItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlgorithmStatusItemList) -> list:
    import aws_sdk_sagemaker.types.algorithm_status_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.algorithm_status_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AlgorithmStatusItemList:
    import aws_sdk_sagemaker.types.algorithm_status_item

    out: AlgorithmStatusItemList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.algorithm_status_item.deserialize_aws_json_1_1(item)
        )
    return out
