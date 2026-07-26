"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceGroupSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_instance_group_specification

ClusterInstanceGroupSpecifications: TypeAlias = list[
    "capo_sagemaker.types.cluster_instance_group_specification.ClusterInstanceGroupSpecification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceGroupSpecifications) -> list:
    import capo_sagemaker.types.cluster_instance_group_specification

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.cluster_instance_group_specification.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterInstanceGroupSpecifications:
    import capo_sagemaker.types.cluster_instance_group_specification

    out: ClusterInstanceGroupSpecifications = []
    for item in data:
        out.append(
            capo_sagemaker.types.cluster_instance_group_specification.deserialize_aws_json_1_1(
                item
            )
        )
    return out
