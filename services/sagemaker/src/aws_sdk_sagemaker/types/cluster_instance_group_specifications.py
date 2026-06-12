"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceGroupSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_instance_group_specification

ClusterInstanceGroupSpecifications: TypeAlias = list[
    "aws_sdk_sagemaker.types.cluster_instance_group_specification.ClusterInstanceGroupSpecification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceGroupSpecifications) -> list:
    import aws_sdk_sagemaker.types.cluster_instance_group_specification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.cluster_instance_group_specification.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterInstanceGroupSpecifications:
    import aws_sdk_sagemaker.types.cluster_instance_group_specification

    out: ClusterInstanceGroupSpecifications = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.cluster_instance_group_specification.deserialize_aws_json_1_1(
                item
            )
        )
    return out
