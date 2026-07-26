"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelVariantConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.model_variant_config

ModelVariantConfigList: TypeAlias = list[
    "capo_sagemaker.types.model_variant_config.ModelVariantConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelVariantConfigList) -> list:
    import capo_sagemaker.types.model_variant_config

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.model_variant_config.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModelVariantConfigList:
    import capo_sagemaker.types.model_variant_config

    out: ModelVariantConfigList = []
    for item in data:
        out.append(
            capo_sagemaker.types.model_variant_config.deserialize_aws_json_1_1(item)
        )
    return out
