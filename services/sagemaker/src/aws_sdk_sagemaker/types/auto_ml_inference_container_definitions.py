"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLInferenceContainerDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_container_definitions
    import aws_sdk_sagemaker.types.auto_ml_processing_unit

AutoMLInferenceContainerDefinitions: TypeAlias = dict[
    "aws_sdk_sagemaker.types.auto_ml_processing_unit.AutoMLProcessingUnit",
    "aws_sdk_sagemaker.types.auto_ml_container_definitions.AutoMLContainerDefinitions",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: AutoMLInferenceContainerDefinitions,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_sagemaker.types.auto_ml_container_definitions
        import aws_sdk_sagemaker.types.auto_ml_processing_unit

        out[
            aws_sdk_sagemaker.types.auto_ml_processing_unit.serialize_aws_json_1_1(key)
        ] = aws_sdk_sagemaker.types.auto_ml_container_definitions.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLInferenceContainerDefinitions:
    out: AutoMLInferenceContainerDefinitions = {}
    for key, value in data.items():
        import aws_sdk_sagemaker.types.auto_ml_container_definitions
        import aws_sdk_sagemaker.types.auto_ml_processing_unit

        out[
            aws_sdk_sagemaker.types.auto_ml_processing_unit.deserialize_aws_json_1_1(
                key
            )
        ] = aws_sdk_sagemaker.types.auto_ml_container_definitions.deserialize_aws_json_1_1(
            value
        )
    return out
