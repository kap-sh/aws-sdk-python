"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ResourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.resources_list_item

ResourcesList: TypeAlias = list[
    "capo_service_catalog_appregistry.types.resources_list_item.ResourcesListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesList) -> list:
    import capo_service_catalog_appregistry.types.resources_list_item

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog_appregistry.types.resources_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResourcesList:
    import capo_service_catalog_appregistry.types.resources_list_item

    out: ResourcesList = []
    for item in data:
        out.append(
            capo_service_catalog_appregistry.types.resources_list_item.deserialize_json(
                item
            )
        )
    return out
