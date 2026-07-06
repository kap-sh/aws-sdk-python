"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListPortfoliosForProductOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.page_token
    import aws_sdk_service_catalog.types.portfolio_details


class ListPortfoliosForProductOutput(TypedDict, closed=True):
    portfolio_details: NotRequired[
        "aws_sdk_service_catalog.types.portfolio_details.PortfolioDetails"
    ]
    """<p>Information about the portfolios.</p>"""
    next_page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPortfoliosForProductOutput) -> dict:
    out: dict = {}
    if "portfolio_details" in value:
        import aws_sdk_service_catalog.types.portfolio_details

        out["PortfolioDetails"] = (
            aws_sdk_service_catalog.types.portfolio_details.serialize_aws_json_1_1(
                value["portfolio_details"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPortfoliosForProductOutput:
    out: ListPortfoliosForProductOutput = {}  # type: ignore[typeddict-item]
    if "PortfolioDetails" in data:
        import aws_sdk_service_catalog.types.portfolio_details

        out["portfolio_details"] = (
            aws_sdk_service_catalog.types.portfolio_details.deserialize_aws_json_1_1(
                data["PortfolioDetails"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
