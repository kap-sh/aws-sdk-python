"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListOrganizationPortfolioAccessOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.organization_nodes
    import aws_sdk_service_catalog.types.page_token


class ListOrganizationPortfolioAccessOutput(TypedDict):
    organization_nodes: NotRequired[
        "aws_sdk_service_catalog.types.organization_nodes.OrganizationNodes"
    ]
    """<p>Displays information about the organization nodes.</p>"""
    next_page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOrganizationPortfolioAccessOutput) -> dict:
    out: dict = {}
    if "organization_nodes" in value:
        import aws_sdk_service_catalog.types.organization_nodes

        out["OrganizationNodes"] = (
            aws_sdk_service_catalog.types.organization_nodes.serialize_aws_json_1_1(
                value["organization_nodes"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOrganizationPortfolioAccessOutput:
    out: ListOrganizationPortfolioAccessOutput = {}  # type: ignore[typeddict-item]
    if "OrganizationNodes" in data:
        import aws_sdk_service_catalog.types.organization_nodes

        out["organization_nodes"] = (
            aws_sdk_service_catalog.types.organization_nodes.deserialize_aws_json_1_1(
                data["OrganizationNodes"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
