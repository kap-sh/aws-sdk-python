"""Generated from Smithy shape ``com.amazonaws.sagemaker#PendingProductionVariantSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.pending_production_variant_summary

PendingProductionVariantSummaryList: TypeAlias = list[
    "capo_sagemaker.types.pending_production_variant_summary.PendingProductionVariantSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingProductionVariantSummaryList) -> list:
    import capo_sagemaker.types.pending_production_variant_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.pending_production_variant_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PendingProductionVariantSummaryList:
    import capo_sagemaker.types.pending_production_variant_summary

    out: PendingProductionVariantSummaryList = []
    for item in data:
        out.append(
            capo_sagemaker.types.pending_production_variant_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
