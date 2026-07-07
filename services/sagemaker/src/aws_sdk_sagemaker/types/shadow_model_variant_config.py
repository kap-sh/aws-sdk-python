"""Generated from Smithy shape ``com.amazonaws.sagemaker#ShadowModelVariantConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_variant_name
    import aws_sdk_sagemaker.types.percentage


class ShadowModelVariantConfig(TypedDict, closed=True):
    shadow_model_variant_name: NotRequired[
        "aws_sdk_sagemaker.types.model_variant_name.ModelVariantName"
    ]
    """<p>The name of the shadow variant.</p>"""
    sampling_percentage: NotRequired["aws_sdk_sagemaker.types.percentage.Percentage"]
    """<p> The percentage of inference requests that Amazon SageMaker replicates from the production variant to the shadow variant. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShadowModelVariantConfig) -> dict:
    out: dict = {}
    if "shadow_model_variant_name" in value:
        out["ShadowModelVariantName"] = value["shadow_model_variant_name"]
    if "sampling_percentage" in value:
        out["SamplingPercentage"] = value["sampling_percentage"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ShadowModelVariantConfig:
    out: ShadowModelVariantConfig = {}  # type: ignore[typeddict-item]
    if "ShadowModelVariantName" in data:
        out["shadow_model_variant_name"] = data["ShadowModelVariantName"]
    if "SamplingPercentage" in data:
        out["sampling_percentage"] = data["SamplingPercentage"]
    return out
