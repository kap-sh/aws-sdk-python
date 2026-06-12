"""Generated from Smithy shape ``com.amazonaws.servicecatalog#LaunchPathSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.constraint_summaries
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.portfolio_name
    import aws_sdk_service_catalog.types.tags


class LaunchPathSummary(TypedDict):
    id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The identifier of the product path.</p>"""
    constraint_summaries: NotRequired[
        "aws_sdk_service_catalog.types.constraint_summaries.ConstraintSummaries"
    ]
    """<p>The constraints on the portfolio-product relationship.</p>"""
    tags: NotRequired["aws_sdk_service_catalog.types.tags.Tags"]
    """<p>The tags associated with this product path.</p>"""
    name: NotRequired["aws_sdk_service_catalog.types.portfolio_name.PortfolioName"]
    """<p>The name of the portfolio that contains the product. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LaunchPathSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "constraint_summaries" in value:
        import aws_sdk_service_catalog.types.constraint_summaries

        out["ConstraintSummaries"] = (
            aws_sdk_service_catalog.types.constraint_summaries.serialize_aws_json_1_1(
                value["constraint_summaries"]
            )
        )
    if "tags" in value:
        import aws_sdk_service_catalog.types.tags

        out["Tags"] = aws_sdk_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LaunchPathSummary:
    out: LaunchPathSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ConstraintSummaries" in data:
        import aws_sdk_service_catalog.types.constraint_summaries

        out["constraint_summaries"] = (
            aws_sdk_service_catalog.types.constraint_summaries.deserialize_aws_json_1_1(
                data["ConstraintSummaries"]
            )
        )
    if "Tags" in data:
        import aws_sdk_service_catalog.types.tags

        out["tags"] = aws_sdk_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    return out
