"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductViewFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.provisioned_product_view_filter_value

ProvisionedProductViewFilterValues: TypeAlias = list[
    "aws_sdk_service_catalog.types.provisioned_product_view_filter_value.ProvisionedProductViewFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionedProductViewFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ProvisionedProductViewFilterValues:
    return list(data)
