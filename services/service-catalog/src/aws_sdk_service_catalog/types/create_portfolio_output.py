"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreatePortfolioOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.portfolio_detail
    import aws_sdk_service_catalog.types.tags


class CreatePortfolioOutput(TypedDict, closed=True):
    portfolio_detail: NotRequired[
        "aws_sdk_service_catalog.types.portfolio_detail.PortfolioDetail"
    ]
    """<p>Information about the portfolio.</p>"""
    tags: NotRequired["aws_sdk_service_catalog.types.tags.Tags"]
    """<p>Information about the tags associated with the portfolio.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePortfolioOutput) -> dict:
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
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePortfolioOutput:
    out: CreatePortfolioOutput = {}  # type: ignore[typeddict-item]
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
    return out
