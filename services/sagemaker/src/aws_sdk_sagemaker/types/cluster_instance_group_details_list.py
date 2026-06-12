"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceGroupDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_instance_group_details

ClusterInstanceGroupDetailsList: TypeAlias = list[
    "aws_sdk_sagemaker.types.cluster_instance_group_details.ClusterInstanceGroupDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceGroupDetailsList) -> list:
    import aws_sdk_sagemaker.types.cluster_instance_group_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.cluster_instance_group_details.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterInstanceGroupDetailsList:
    import aws_sdk_sagemaker.types.cluster_instance_group_details

    out: ClusterInstanceGroupDetailsList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.cluster_instance_group_details.deserialize_aws_json_1_1(
                item
            )
        )
    return out
