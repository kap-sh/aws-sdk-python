"""Generated from Smithy shape ``com.amazonaws.wafv2#DescribeAllManagedProductsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.managed_product_descriptors


class DescribeAllManagedProductsResponse(TypedDict, closed=True):
    managed_products: NotRequired[
        "aws_sdk_wafv2.types.managed_product_descriptors.ManagedProductDescriptors"
    ]
    """<p>High-level information for the Amazon Web Services Managed Rules rule groups and Amazon Web Services Marketplace managed rule groups. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAllManagedProductsResponse) -> dict:
    out: dict = {}
    if "managed_products" in value:
        import aws_sdk_wafv2.types.managed_product_descriptors

        out["ManagedProducts"] = (
            aws_sdk_wafv2.types.managed_product_descriptors.serialize_aws_json_1_1(
                value["managed_products"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAllManagedProductsResponse:
    out: DescribeAllManagedProductsResponse = {}  # type: ignore[typeddict-item]
    if "ManagedProducts" in data:
        import aws_sdk_wafv2.types.managed_product_descriptors

        out["managed_products"] = (
            aws_sdk_wafv2.types.managed_product_descriptors.deserialize_aws_json_1_1(
                data["ManagedProducts"]
            )
        )
    return out
