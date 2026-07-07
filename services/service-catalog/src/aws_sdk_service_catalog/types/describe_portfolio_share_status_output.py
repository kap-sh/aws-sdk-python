"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribePortfolioShareStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.organization_node_value
    import aws_sdk_service_catalog.types.share_details
    import aws_sdk_service_catalog.types.share_status


class DescribePortfolioShareStatusOutput(TypedDict, closed=True):
    portfolio_share_token: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The token for the portfolio share operation. For example, <code>share-6v24abcdefghi</code>.</p>"""
    portfolio_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The portfolio identifier.</p>"""
    organization_node_value: NotRequired[
        "aws_sdk_service_catalog.types.organization_node_value.OrganizationNodeValue"
    ]
    """<p>Organization node identifier. It can be either account id, organizational unit id or organization id.</p>"""
    status: NotRequired["aws_sdk_service_catalog.types.share_status.ShareStatus"]
    """<p>Status of the portfolio share operation.</p>"""
    share_details: NotRequired[
        "aws_sdk_service_catalog.types.share_details.ShareDetails"
    ]
    """<p>Information about the portfolio share operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePortfolioShareStatusOutput) -> dict:
    out: dict = {}
    if "portfolio_share_token" in value:
        out["PortfolioShareToken"] = value["portfolio_share_token"]
    if "portfolio_id" in value:
        out["PortfolioId"] = value["portfolio_id"]
    if "organization_node_value" in value:
        out["OrganizationNodeValue"] = value["organization_node_value"]
    if "status" in value:
        import aws_sdk_service_catalog.types.share_status

        out["Status"] = (
            aws_sdk_service_catalog.types.share_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "share_details" in value:
        import aws_sdk_service_catalog.types.share_details

        out["ShareDetails"] = (
            aws_sdk_service_catalog.types.share_details.serialize_aws_json_1_1(
                value["share_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePortfolioShareStatusOutput:
    out: DescribePortfolioShareStatusOutput = {}  # type: ignore[typeddict-item]
    if "PortfolioShareToken" in data:
        out["portfolio_share_token"] = data["PortfolioShareToken"]
    if "PortfolioId" in data:
        out["portfolio_id"] = data["PortfolioId"]
    if "OrganizationNodeValue" in data:
        out["organization_node_value"] = data["OrganizationNodeValue"]
    if "Status" in data:
        import aws_sdk_service_catalog.types.share_status

        out["status"] = (
            aws_sdk_service_catalog.types.share_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "ShareDetails" in data:
        import aws_sdk_service_catalog.types.share_details

        out["share_details"] = (
            aws_sdk_service_catalog.types.share_details.deserialize_aws_json_1_1(
                data["ShareDetails"]
            )
        )
    return out
