"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateClusterSoftwareInstanceGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.update_cluster_software_instance_group_specification

UpdateClusterSoftwareInstanceGroups: TypeAlias = list[
    "aws_sdk_sagemaker.types.update_cluster_software_instance_group_specification.UpdateClusterSoftwareInstanceGroupSpecification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateClusterSoftwareInstanceGroups) -> list:
    import aws_sdk_sagemaker.types.update_cluster_software_instance_group_specification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.update_cluster_software_instance_group_specification.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UpdateClusterSoftwareInstanceGroups:
    import aws_sdk_sagemaker.types.update_cluster_software_instance_group_specification

    out: UpdateClusterSoftwareInstanceGroups = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.update_cluster_software_instance_group_specification.deserialize_aws_json_1_1(
                item
            )
        )
    return out
