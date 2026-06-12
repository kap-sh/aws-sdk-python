"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ListAttributeGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.attribute_group_summaries
    import aws_sdk_service_catalog_appregistry.types.next_token


class ListAttributeGroupsResponse(TypedDict):
    attribute_groups: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.attribute_group_summaries.AttributeGroupSummaries"
    ]
    """<p>This list of attribute groups.</p>"""
    next_token: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
    ]
    """<p>The token to use to get the next page of results after a previous API call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttributeGroupsResponse) -> dict:
    out: dict = {}
    if "attribute_groups" in value:
        import aws_sdk_service_catalog_appregistry.types.attribute_group_summaries

        out["attributeGroups"] = (
            aws_sdk_service_catalog_appregistry.types.attribute_group_summaries.serialize_json(
                value["attribute_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAttributeGroupsResponse:
    out: ListAttributeGroupsResponse = {}  # type: ignore[typeddict-item]
    if "attributeGroups" in data:
        import aws_sdk_service_catalog_appregistry.types.attribute_group_summaries

        out["attribute_groups"] = (
            aws_sdk_service_catalog_appregistry.types.attribute_group_summaries.deserialize_json(
                data["attributeGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
