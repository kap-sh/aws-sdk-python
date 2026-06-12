"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SearchProductsAsAdminOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.page_token
    import aws_sdk_service_catalog.types.product_view_details


class SearchProductsAsAdminOutput(TypedDict):
    product_view_details: NotRequired[
        "aws_sdk_service_catalog.types.product_view_details.ProductViewDetails"
    ]
    """<p>Information about the product views.</p>"""
    next_page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchProductsAsAdminOutput) -> dict:
    out: dict = {}
    if "product_view_details" in value:
        import aws_sdk_service_catalog.types.product_view_details

        out["ProductViewDetails"] = (
            aws_sdk_service_catalog.types.product_view_details.serialize_aws_json_1_1(
                value["product_view_details"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchProductsAsAdminOutput:
    out: SearchProductsAsAdminOutput = {}  # type: ignore[typeddict-item]
    if "ProductViewDetails" in data:
        import aws_sdk_service_catalog.types.product_view_details

        out["product_view_details"] = (
            aws_sdk_service_catalog.types.product_view_details.deserialize_aws_json_1_1(
                data["ProductViewDetails"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
