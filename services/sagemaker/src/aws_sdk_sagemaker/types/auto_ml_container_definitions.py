"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLContainerDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_container_definition

AutoMLContainerDefinitions: TypeAlias = list[
    "aws_sdk_sagemaker.types.auto_ml_container_definition.AutoMLContainerDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLContainerDefinitions) -> list:
    import aws_sdk_sagemaker.types.auto_ml_container_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.auto_ml_container_definition.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutoMLContainerDefinitions:
    import aws_sdk_sagemaker.types.auto_ml_container_definition

    out: AutoMLContainerDefinitions = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.auto_ml_container_definition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
