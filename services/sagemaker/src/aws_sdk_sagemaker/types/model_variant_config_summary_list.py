"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelVariantConfigSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_variant_config_summary

ModelVariantConfigSummaryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.model_variant_config_summary.ModelVariantConfigSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelVariantConfigSummaryList) -> list:
    import aws_sdk_sagemaker.types.model_variant_config_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.model_variant_config_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModelVariantConfigSummaryList:
    import aws_sdk_sagemaker.types.model_variant_config_summary

    out: ModelVariantConfigSummaryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.model_variant_config_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
