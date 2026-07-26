"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductViewAggregationValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.product_view_aggregation_value

ProductViewAggregationValues: TypeAlias = list[
    "capo_service_catalog.types.product_view_aggregation_value.ProductViewAggregationValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductViewAggregationValues) -> list:
    import capo_service_catalog.types.product_view_aggregation_value

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.product_view_aggregation_value.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProductViewAggregationValues:
    import capo_service_catalog.types.product_view_aggregation_value

    out: ProductViewAggregationValues = []
    for item in data:
        out.append(
            capo_service_catalog.types.product_view_aggregation_value.deserialize_aws_json_1_1(
                item
            )
        )
    return out
