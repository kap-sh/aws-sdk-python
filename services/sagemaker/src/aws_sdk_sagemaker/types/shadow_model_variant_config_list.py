"""Generated from Smithy shape ``com.amazonaws.sagemaker#ShadowModelVariantConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.shadow_model_variant_config

ShadowModelVariantConfigList: TypeAlias = list[
    "aws_sdk_sagemaker.types.shadow_model_variant_config.ShadowModelVariantConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShadowModelVariantConfigList) -> list:
    import aws_sdk_sagemaker.types.shadow_model_variant_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.shadow_model_variant_config.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ShadowModelVariantConfigList:
    import aws_sdk_sagemaker.types.shadow_model_variant_config

    out: ShadowModelVariantConfigList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.shadow_model_variant_config.deserialize_aws_json_1_1(
                item
            )
        )
    return out
