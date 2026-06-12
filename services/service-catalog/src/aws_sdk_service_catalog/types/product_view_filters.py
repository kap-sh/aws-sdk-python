"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductViewFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.product_view_filter_by
    import aws_sdk_service_catalog.types.product_view_filter_values

ProductViewFilters: TypeAlias = dict[
    "aws_sdk_service_catalog.types.product_view_filter_by.ProductViewFilterBy",
    "aws_sdk_service_catalog.types.product_view_filter_values.ProductViewFilterValues",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ProductViewFilters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_service_catalog.types.product_view_filter_by
        import aws_sdk_service_catalog.types.product_view_filter_values

        out[
            aws_sdk_service_catalog.types.product_view_filter_by.serialize_aws_json_1_1(
                key
            )
        ] = aws_sdk_service_catalog.types.product_view_filter_values.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductViewFilters:
    out: ProductViewFilters = {}
    for key, value in data.items():
        import aws_sdk_service_catalog.types.product_view_filter_by
        import aws_sdk_service_catalog.types.product_view_filter_values

        out[
            aws_sdk_service_catalog.types.product_view_filter_by.deserialize_aws_json_1_1(
                key
            )
        ] = aws_sdk_service_catalog.types.product_view_filter_values.deserialize_aws_json_1_1(
            value
        )
    return out
