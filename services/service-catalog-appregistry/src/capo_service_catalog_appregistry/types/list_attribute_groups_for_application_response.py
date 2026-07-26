"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ListAttributeGroupsForApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.attribute_group_details_list
    import capo_service_catalog_appregistry.types.next_token


class ListAttributeGroupsForApplicationResponse(TypedDict, closed=True):
    attribute_groups_details: NotRequired[
        "capo_service_catalog_appregistry.types.attribute_group_details_list.AttributeGroupDetailsList"
    ]
    """<p> The details related to a specific attribute group. </p>"""
    next_token: NotRequired[
        "capo_service_catalog_appregistry.types.next_token.NextToken"
    ]
    """<p>The token to use to get the next page of results after a previous API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttributeGroupsForApplicationResponse) -> dict:
    out: dict = {}
    if "attribute_groups_details" in value:
        import capo_service_catalog_appregistry.types.attribute_group_details_list

        out["attributeGroupsDetails"] = (
            capo_service_catalog_appregistry.types.attribute_group_details_list.serialize_json(
                value["attribute_groups_details"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAttributeGroupsForApplicationResponse:
    out: ListAttributeGroupsForApplicationResponse = {}  # type: ignore[typeddict-item]
    if "attributeGroupsDetails" in data:
        import capo_service_catalog_appregistry.types.attribute_group_details_list

        out["attribute_groups_details"] = (
            capo_service_catalog_appregistry.types.attribute_group_details_list.deserialize_json(
                data["attributeGroupsDetails"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
