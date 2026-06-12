"""Generated from Smithy shape ``com.amazonaws.sagemaker#ShadowModeConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_variant_name
    import aws_sdk_sagemaker.types.shadow_model_variant_config_list


class ShadowModeConfig(TypedDict):
    source_model_variant_name: NotRequired[
        "aws_sdk_sagemaker.types.model_variant_name.ModelVariantName"
    ]
    """<p> The name of the production variant, which takes all the inference requests. </p>"""
    shadow_model_variants: NotRequired[
        "aws_sdk_sagemaker.types.shadow_model_variant_config_list.ShadowModelVariantConfigList"
    ]
    """<p>List of shadow variant configurations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShadowModeConfig) -> dict:
    out: dict = {}
    if "source_model_variant_name" in value:
        out["SourceModelVariantName"] = value["source_model_variant_name"]
    if "shadow_model_variants" in value:
        import aws_sdk_sagemaker.types.shadow_model_variant_config_list

        out["ShadowModelVariants"] = (
            aws_sdk_sagemaker.types.shadow_model_variant_config_list.serialize_aws_json_1_1(
                value["shadow_model_variants"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ShadowModeConfig:
    out: ShadowModeConfig = {}  # type: ignore[typeddict-item]
    if "SourceModelVariantName" in data:
        out["source_model_variant_name"] = data["SourceModelVariantName"]
    if "ShadowModelVariants" in data:
        import aws_sdk_sagemaker.types.shadow_model_variant_config_list

        out["shadow_model_variants"] = (
            aws_sdk_sagemaker.types.shadow_model_variant_config_list.deserialize_aws_json_1_1(
                data["ShadowModelVariants"]
            )
        )
    return out
