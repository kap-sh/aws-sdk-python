"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_instance_type

ClusterInstanceTypes: TypeAlias = list[
    "aws_sdk_sagemaker.types.cluster_instance_type.ClusterInstanceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceTypes) -> list:
    import aws_sdk_sagemaker.types.cluster_instance_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.cluster_instance_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterInstanceTypes:
    import aws_sdk_sagemaker.types.cluster_instance_type

    out: ClusterInstanceTypes = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.cluster_instance_type.deserialize_aws_json_1_1(item)
        )
    return out
