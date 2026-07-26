"""Generated from Smithy shape ``com.amazonaws.wafv2#DescribeManagedProductsByVendorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.managed_product_descriptors


class DescribeManagedProductsByVendorResponse(TypedDict, closed=True):
    managed_products: NotRequired[
        "capo_wafv2.types.managed_product_descriptors.ManagedProductDescriptors"
    ]
    """<p>High-level information for the managed rule groups owned by the specified vendor. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeManagedProductsByVendorResponse) -> dict:
    out: dict = {}
    if "managed_products" in value:
        import capo_wafv2.types.managed_product_descriptors

        out["ManagedProducts"] = (
            capo_wafv2.types.managed_product_descriptors.serialize_aws_json_1_1(
                value["managed_products"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeManagedProductsByVendorResponse:
    out: DescribeManagedProductsByVendorResponse = {}  # type: ignore[typeddict-item]
    if "ManagedProducts" in data:
        import capo_wafv2.types.managed_product_descriptors

        out["managed_products"] = (
            capo_wafv2.types.managed_product_descriptors.deserialize_aws_json_1_1(
                data["ManagedProducts"]
            )
        )
    return out
