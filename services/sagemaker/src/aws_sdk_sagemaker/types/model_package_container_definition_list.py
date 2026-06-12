"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageContainerDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_package_container_definition

ModelPackageContainerDefinitionList: TypeAlias = list[
    "aws_sdk_sagemaker.types.model_package_container_definition.ModelPackageContainerDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageContainerDefinitionList) -> list:
    import aws_sdk_sagemaker.types.model_package_container_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.model_package_container_definition.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModelPackageContainerDefinitionList:
    import aws_sdk_sagemaker.types.model_package_container_definition

    out: ModelPackageContainerDefinitionList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.model_package_container_definition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
