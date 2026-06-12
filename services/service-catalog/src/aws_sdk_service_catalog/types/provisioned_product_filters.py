"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.provisioned_product_view_filter_by
    import aws_sdk_service_catalog.types.provisioned_product_view_filter_values

ProvisionedProductFilters: TypeAlias = dict[
    "aws_sdk_service_catalog.types.provisioned_product_view_filter_by.ProvisionedProductViewFilterBy",
    "aws_sdk_service_catalog.types.provisioned_product_view_filter_values.ProvisionedProductViewFilterValues",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ProvisionedProductFilters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_service_catalog.types.provisioned_product_view_filter_by
        import aws_sdk_service_catalog.types.provisioned_product_view_filter_values

        out[
            aws_sdk_service_catalog.types.provisioned_product_view_filter_by.serialize_aws_json_1_1(
                key
            )
        ] = aws_sdk_service_catalog.types.provisioned_product_view_filter_values.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisionedProductFilters:
    out: ProvisionedProductFilters = {}
    for key, value in data.items():
        import aws_sdk_service_catalog.types.provisioned_product_view_filter_by
        import aws_sdk_service_catalog.types.provisioned_product_view_filter_values

        out[
            aws_sdk_service_catalog.types.provisioned_product_view_filter_by.deserialize_aws_json_1_1(
                key
            )
        ] = aws_sdk_service_catalog.types.provisioned_product_view_filter_values.deserialize_aws_json_1_1(
            value
        )
    return out
