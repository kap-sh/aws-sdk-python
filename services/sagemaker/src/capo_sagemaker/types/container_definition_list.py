"""Generated from Smithy shape ``com.amazonaws.sagemaker#ContainerDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.container_definition

ContainerDefinitionList: TypeAlias = list[
    "capo_sagemaker.types.container_definition.ContainerDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerDefinitionList) -> list:
    import capo_sagemaker.types.container_definition

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.container_definition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerDefinitionList:
    import capo_sagemaker.types.container_definition

    out: ContainerDefinitionList = []
    for item in data:
        out.append(
            capo_sagemaker.types.container_definition.deserialize_aws_json_1_1(item)
        )
    return out
