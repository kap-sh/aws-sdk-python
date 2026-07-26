"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLInferenceContainerDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_container_definitions
    import capo_sagemaker.types.auto_ml_processing_unit

AutoMLInferenceContainerDefinitions: TypeAlias = dict[
    "capo_sagemaker.types.auto_ml_processing_unit.AutoMLProcessingUnit",
    "capo_sagemaker.types.auto_ml_container_definitions.AutoMLContainerDefinitions",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: AutoMLInferenceContainerDefinitions,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sagemaker.types.auto_ml_container_definitions
        import capo_sagemaker.types.auto_ml_processing_unit

        out[
            capo_sagemaker.types.auto_ml_processing_unit.serialize_aws_json_1_1(key)
        ] = capo_sagemaker.types.auto_ml_container_definitions.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLInferenceContainerDefinitions:
    out: AutoMLInferenceContainerDefinitions = {}
    for key, value in data.items():
        import capo_sagemaker.types.auto_ml_container_definitions
        import capo_sagemaker.types.auto_ml_processing_unit

        out[
            capo_sagemaker.types.auto_ml_processing_unit.deserialize_aws_json_1_1(key)
        ] = capo_sagemaker.types.auto_ml_container_definitions.deserialize_aws_json_1_1(
            value
        )
    return out
