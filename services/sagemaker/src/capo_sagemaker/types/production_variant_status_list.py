"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.production_variant_status

ProductionVariantStatusList: TypeAlias = list[
    "capo_sagemaker.types.production_variant_status.ProductionVariantStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductionVariantStatusList) -> list:
    import capo_sagemaker.types.production_variant_status

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.production_variant_status.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProductionVariantStatusList:
    import capo_sagemaker.types.production_variant_status

    out: ProductionVariantStatusList = []
    for item in data:
        out.append(
            capo_sagemaker.types.production_variant_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
