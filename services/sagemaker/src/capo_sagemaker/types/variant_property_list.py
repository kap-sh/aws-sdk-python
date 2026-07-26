"""Generated from Smithy shape ``com.amazonaws.sagemaker#VariantPropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.variant_property

VariantPropertyList: TypeAlias = list[
    "capo_sagemaker.types.variant_property.VariantProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VariantPropertyList) -> list:
    import capo_sagemaker.types.variant_property

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.variant_property.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> VariantPropertyList:
    import capo_sagemaker.types.variant_property

    out: VariantPropertyList = []
    for item in data:
        out.append(capo_sagemaker.types.variant_property.deserialize_aws_json_1_1(item))
    return out
