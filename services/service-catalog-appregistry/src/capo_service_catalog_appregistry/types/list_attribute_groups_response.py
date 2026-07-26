"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ListAttributeGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.attribute_group_summaries
    import capo_service_catalog_appregistry.types.next_token


class ListAttributeGroupsResponse(TypedDict, closed=True):
    attribute_groups: NotRequired[
        "capo_service_catalog_appregistry.types.attribute_group_summaries.AttributeGroupSummaries"
    ]
    """<p>This list of attribute groups.</p>"""
    next_token: NotRequired[
        "capo_service_catalog_appregistry.types.next_token.NextToken"
    ]
    """<p>The token to use to get the next page of results after a previous API call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttributeGroupsResponse) -> dict:
    out: dict = {}
    if "attribute_groups" in value:
        import capo_service_catalog_appregistry.types.attribute_group_summaries

        out["attributeGroups"] = (
            capo_service_catalog_appregistry.types.attribute_group_summaries.serialize_json(
                value["attribute_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAttributeGroupsResponse:
    out: ListAttributeGroupsResponse = {}  # type: ignore[typeddict-item]
    if "attributeGroups" in data:
        import capo_service_catalog_appregistry.types.attribute_group_summaries

        out["attribute_groups"] = (
            capo_service_catalog_appregistry.types.attribute_group_summaries.deserialize_json(
                data["attributeGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
