"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.production_variant

ProductionVariantList: TypeAlias = list[
    "capo_sagemaker.types.production_variant.ProductionVariant"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductionVariantList) -> list:
    import capo_sagemaker.types.production_variant

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.production_variant.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProductionVariantList:
    import capo_sagemaker.types.production_variant

    out: ProductionVariantList = []
    for item in data:
        out.append(
            capo_sagemaker.types.production_variant.deserialize_aws_json_1_1(item)
        )
    return out
