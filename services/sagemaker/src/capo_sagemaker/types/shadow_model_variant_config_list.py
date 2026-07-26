"""Generated from Smithy shape ``com.amazonaws.sagemaker#ShadowModelVariantConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.shadow_model_variant_config

ShadowModelVariantConfigList: TypeAlias = list[
    "capo_sagemaker.types.shadow_model_variant_config.ShadowModelVariantConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShadowModelVariantConfigList) -> list:
    import capo_sagemaker.types.shadow_model_variant_config

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.shadow_model_variant_config.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ShadowModelVariantConfigList:
    import capo_sagemaker.types.shadow_model_variant_config

    out: ShadowModelVariantConfigList = []
    for item in data:
        out.append(
            capo_sagemaker.types.shadow_model_variant_config.deserialize_aws_json_1_1(
                item
            )
        )
    return out
