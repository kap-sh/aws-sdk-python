"""Generated from Smithy shape ``com.amazonaws.ssm#PatchSourceProductList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.patch_source_product

PatchSourceProductList: TypeAlias = list[
    "aws_sdk_ssm.types.patch_source_product.PatchSourceProduct"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchSourceProductList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PatchSourceProductList:
    return list(data)
