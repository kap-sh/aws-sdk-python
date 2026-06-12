"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductViewDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.product_view_detail

ProductViewDetails: TypeAlias = list[
    "aws_sdk_service_catalog.types.product_view_detail.ProductViewDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductViewDetails) -> list:
    import aws_sdk_service_catalog.types.product_view_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.product_view_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProductViewDetails:
    import aws_sdk_service_catalog.types.product_view_detail

    out: ProductViewDetails = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.product_view_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
