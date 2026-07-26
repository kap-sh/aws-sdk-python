"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelVariantActionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.model_variant_action
    import capo_sagemaker.types.model_variant_name

ModelVariantActionMap: TypeAlias = dict[
    "capo_sagemaker.types.model_variant_name.ModelVariantName",
    "capo_sagemaker.types.model_variant_action.ModelVariantAction",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ModelVariantActionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sagemaker.types.model_variant_action

        out[key] = capo_sagemaker.types.model_variant_action.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelVariantActionMap:
    out: ModelVariantActionMap = {}
    for key, value in data.items():
        import capo_sagemaker.types.model_variant_action

        out[key] = capo_sagemaker.types.model_variant_action.deserialize_aws_json_1_1(
            value
        )
    return out
