"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterRestrictedInstanceGroupSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_restricted_instance_group_specification

ClusterRestrictedInstanceGroupSpecifications: TypeAlias = list[
    "aws_sdk_sagemaker.types.cluster_restricted_instance_group_specification.ClusterRestrictedInstanceGroupSpecification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterRestrictedInstanceGroupSpecifications) -> list:
    import aws_sdk_sagemaker.types.cluster_restricted_instance_group_specification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.cluster_restricted_instance_group_specification.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> ClusterRestrictedInstanceGroupSpecifications:
    import aws_sdk_sagemaker.types.cluster_restricted_instance_group_specification

    out: ClusterRestrictedInstanceGroupSpecifications = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.cluster_restricted_instance_group_specification.deserialize_aws_json_1_1(
                item
            )
        )
    return out
