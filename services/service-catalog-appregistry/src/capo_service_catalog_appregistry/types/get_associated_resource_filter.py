"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#GetAssociatedResourceFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.resource_item_status

GetAssociatedResourceFilter: TypeAlias = list[
    "capo_service_catalog_appregistry.types.resource_item_status.ResourceItemStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetAssociatedResourceFilter) -> list:
    import capo_service_catalog_appregistry.types.resource_item_status

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog_appregistry.types.resource_item_status.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GetAssociatedResourceFilter:
    import capo_service_catalog_appregistry.types.resource_item_status

    out: GetAssociatedResourceFilter = []
    for item in data:
        out.append(
            capo_service_catalog_appregistry.types.resource_item_status.deserialize_json(
                item
            )
        )
    return out
