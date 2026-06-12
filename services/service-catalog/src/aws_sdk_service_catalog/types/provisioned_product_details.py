"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.provisioned_product_detail

ProvisionedProductDetails: TypeAlias = list[
    "aws_sdk_service_catalog.types.provisioned_product_detail.ProvisionedProductDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionedProductDetails) -> list:
    import aws_sdk_service_catalog.types.provisioned_product_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.provisioned_product_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvisionedProductDetails:
    import aws_sdk_service_catalog.types.provisioned_product_detail

    out: ProvisionedProductDetails = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.provisioned_product_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
