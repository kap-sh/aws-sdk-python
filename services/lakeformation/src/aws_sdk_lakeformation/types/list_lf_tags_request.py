"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListLFTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.page_size
    import aws_sdk_lakeformation.types.resource_share_type
    import aws_sdk_lakeformation.types.token


class ListLFTagsRequest(TypedDict):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    resource_share_type: NotRequired[
        "aws_sdk_lakeformation.types.resource_share_type.ResourceShareType"
    ]
    """<p>If resource share type is <code>ALL</code>, returns both in-account LF-tags and shared LF-tags that the requester has permission to view. If resource share type is <code>FOREIGN</code>, returns all share LF-tags that the requester can view. If no resource share type is passed, lists LF-tags in the given catalog ID that the requester has permission to view.</p>"""
    max_results: NotRequired["aws_sdk_lakeformation.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is not the first call to retrieve this list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLFTagsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "resource_share_type" in value:
        import aws_sdk_lakeformation.types.resource_share_type

        out["ResourceShareType"] = (
            aws_sdk_lakeformation.types.resource_share_type.serialize_json(
                value["resource_share_type"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLFTagsRequest:
    out: ListLFTagsRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "ResourceShareType" in data:
        import aws_sdk_lakeformation.types.resource_share_type

        out["resource_share_type"] = (
            aws_sdk_lakeformation.types.resource_share_type.deserialize_json(
                data["ResourceShareType"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
