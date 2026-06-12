"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribePortfolioOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.budgets
    import aws_sdk_service_catalog.types.portfolio_detail
    import aws_sdk_service_catalog.types.tag_option_details
    import aws_sdk_service_catalog.types.tags


class DescribePortfolioOutput(TypedDict):
    portfolio_detail: NotRequired[
        "aws_sdk_service_catalog.types.portfolio_detail.PortfolioDetail"
    ]
    """<p>Information about the portfolio.</p>"""
    tags: NotRequired["aws_sdk_service_catalog.types.tags.Tags"]
    """<p>Information about the tags associated with the portfolio.</p>"""
    tag_options: NotRequired[
        "aws_sdk_service_catalog.types.tag_option_details.TagOptionDetails"
    ]
    """<p>Information about the TagOptions associated with the portfolio.</p>"""
    budgets: NotRequired["aws_sdk_service_catalog.types.budgets.Budgets"]
    """<p>Information about the associated budgets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePortfolioOutput) -> dict:
    out: dict = {}
    if "portfolio_detail" in value:
        import aws_sdk_service_catalog.types.portfolio_detail

        out["PortfolioDetail"] = (
            aws_sdk_service_catalog.types.portfolio_detail.serialize_aws_json_1_1(
                value["portfolio_detail"]
            )
        )
    if "tags" in value:
        import aws_sdk_service_catalog.types.tags

        out["Tags"] = aws_sdk_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "tag_options" in value:
        import aws_sdk_service_catalog.types.tag_option_details

        out["TagOptions"] = (
            aws_sdk_service_catalog.types.tag_option_details.serialize_aws_json_1_1(
                value["tag_options"]
            )
        )
    if "budgets" in value:
        import aws_sdk_service_catalog.types.budgets

        out["Budgets"] = aws_sdk_service_catalog.types.budgets.serialize_aws_json_1_1(
            value["budgets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePortfolioOutput:
    out: DescribePortfolioOutput = {}  # type: ignore[typeddict-item]
    if "PortfolioDetail" in data:
        import aws_sdk_service_catalog.types.portfolio_detail

        out["portfolio_detail"] = (
            aws_sdk_service_catalog.types.portfolio_detail.deserialize_aws_json_1_1(
                data["PortfolioDetail"]
            )
        )
    if "Tags" in data:
        import aws_sdk_service_catalog.types.tags

        out["tags"] = aws_sdk_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "TagOptions" in data:
        import aws_sdk_service_catalog.types.tag_option_details

        out["tag_options"] = (
            aws_sdk_service_catalog.types.tag_option_details.deserialize_aws_json_1_1(
                data["TagOptions"]
            )
        )
    if "Budgets" in data:
        import aws_sdk_service_catalog.types.budgets

        out["budgets"] = aws_sdk_service_catalog.types.budgets.deserialize_aws_json_1_1(
            data["Budgets"]
        )
    return out
