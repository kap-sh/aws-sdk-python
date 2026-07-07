"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SearchProductsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.page_token
    import aws_sdk_service_catalog.types.product_view_aggregations
    import aws_sdk_service_catalog.types.product_view_summaries


class SearchProductsOutput(TypedDict, closed=True):
    product_view_summaries: NotRequired[
        "aws_sdk_service_catalog.types.product_view_summaries.ProductViewSummaries"
    ]
    """<p>Information about the product views.</p>"""
    product_view_aggregations: NotRequired[
        "aws_sdk_service_catalog.types.product_view_aggregations.ProductViewAggregations"
    ]
    """<p>The product view aggregations.</p>"""
    next_page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchProductsOutput) -> dict:
    out: dict = {}
    if "product_view_summaries" in value:
        import aws_sdk_service_catalog.types.product_view_summaries

        out["ProductViewSummaries"] = (
            aws_sdk_service_catalog.types.product_view_summaries.serialize_aws_json_1_1(
                value["product_view_summaries"]
            )
        )
    if "product_view_aggregations" in value:
        import aws_sdk_service_catalog.types.product_view_aggregations

        out["ProductViewAggregations"] = (
            aws_sdk_service_catalog.types.product_view_aggregations.serialize_aws_json_1_1(
                value["product_view_aggregations"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchProductsOutput:
    out: SearchProductsOutput = {}  # type: ignore[typeddict-item]
    if "ProductViewSummaries" in data:
        import aws_sdk_service_catalog.types.product_view_summaries

        out["product_view_summaries"] = (
            aws_sdk_service_catalog.types.product_view_summaries.deserialize_aws_json_1_1(
                data["ProductViewSummaries"]
            )
        )
    if "ProductViewAggregations" in data:
        import aws_sdk_service_catalog.types.product_view_aggregations

        out["product_view_aggregations"] = (
            aws_sdk_service_catalog.types.product_view_aggregations.deserialize_aws_json_1_1(
                data["ProductViewAggregations"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
