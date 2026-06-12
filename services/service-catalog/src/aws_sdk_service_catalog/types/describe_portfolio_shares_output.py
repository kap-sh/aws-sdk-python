"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribePortfolioSharesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.page_token
    import aws_sdk_service_catalog.types.portfolio_share_details


class DescribePortfolioSharesOutput(TypedDict):
    next_page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""
    portfolio_share_details: NotRequired[
        "aws_sdk_service_catalog.types.portfolio_share_details.PortfolioShareDetails"
    ]
    """<p>Summaries about each of the portfolio shares.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePortfolioSharesOutput) -> dict:
    out: dict = {}
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    if "portfolio_share_details" in value:
        import aws_sdk_service_catalog.types.portfolio_share_details

        out["PortfolioShareDetails"] = (
            aws_sdk_service_catalog.types.portfolio_share_details.serialize_aws_json_1_1(
                value["portfolio_share_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePortfolioSharesOutput:
    out: DescribePortfolioSharesOutput = {}  # type: ignore[typeddict-item]
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    if "PortfolioShareDetails" in data:
        import aws_sdk_service_catalog.types.portfolio_share_details

        out["portfolio_share_details"] = (
            aws_sdk_service_catalog.types.portfolio_share_details.deserialize_aws_json_1_1(
                data["PortfolioShareDetails"]
            )
        )
    return out
