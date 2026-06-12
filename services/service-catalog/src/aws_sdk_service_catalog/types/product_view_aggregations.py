"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductViewAggregations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.product_view_aggregation_type
    import aws_sdk_service_catalog.types.product_view_aggregation_values

ProductViewAggregations: TypeAlias = dict[
    "aws_sdk_service_catalog.types.product_view_aggregation_type.ProductViewAggregationType",
    "aws_sdk_service_catalog.types.product_view_aggregation_values.ProductViewAggregationValues",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ProductViewAggregations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_service_catalog.types.product_view_aggregation_values

        out[key] = (
            aws_sdk_service_catalog.types.product_view_aggregation_values.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductViewAggregations:
    out: ProductViewAggregations = {}
    for key, value in data.items():
        import aws_sdk_service_catalog.types.product_view_aggregation_values

        out[key] = (
            aws_sdk_service_catalog.types.product_view_aggregation_values.deserialize_aws_json_1_1(
                value
            )
        )
    return out
