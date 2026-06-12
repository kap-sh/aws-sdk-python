"""Generated from Smithy shape ``com.amazonaws.sagemaker#AddClusterNodeSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.add_cluster_node_specification

AddClusterNodeSpecificationList: TypeAlias = list[
    "aws_sdk_sagemaker.types.add_cluster_node_specification.AddClusterNodeSpecification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddClusterNodeSpecificationList) -> list:
    import aws_sdk_sagemaker.types.add_cluster_node_specification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.add_cluster_node_specification.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AddClusterNodeSpecificationList:
    import aws_sdk_sagemaker.types.add_cluster_node_specification

    out: AddClusterNodeSpecificationList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.add_cluster_node_specification.deserialize_aws_json_1_1(
                item
            )
        )
    return out
