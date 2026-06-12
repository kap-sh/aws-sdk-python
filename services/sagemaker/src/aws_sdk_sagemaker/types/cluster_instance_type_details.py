"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceTypeDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_instance_type_detail

ClusterInstanceTypeDetails: TypeAlias = list[
    "aws_sdk_sagemaker.types.cluster_instance_type_detail.ClusterInstanceTypeDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceTypeDetails) -> list:
    import aws_sdk_sagemaker.types.cluster_instance_type_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.cluster_instance_type_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterInstanceTypeDetails:
    import aws_sdk_sagemaker.types.cluster_instance_type_detail

    out: ClusterInstanceTypeDetails = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.cluster_instance_type_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
