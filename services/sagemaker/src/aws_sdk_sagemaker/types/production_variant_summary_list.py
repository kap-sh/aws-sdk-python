"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.production_variant_summary

ProductionVariantSummaryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.production_variant_summary.ProductionVariantSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductionVariantSummaryList) -> list:
    import aws_sdk_sagemaker.types.production_variant_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.production_variant_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProductionVariantSummaryList:
    import aws_sdk_sagemaker.types.production_variant_summary

    out: ProductionVariantSummaryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.production_variant_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
