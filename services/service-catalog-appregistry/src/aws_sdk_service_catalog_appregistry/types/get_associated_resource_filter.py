"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#GetAssociatedResourceFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.resource_item_status

GetAssociatedResourceFilter: TypeAlias = list[
    "aws_sdk_service_catalog_appregistry.types.resource_item_status.ResourceItemStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetAssociatedResourceFilter) -> list:
    import aws_sdk_service_catalog_appregistry.types.resource_item_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog_appregistry.types.resource_item_status.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GetAssociatedResourceFilter:
    import aws_sdk_service_catalog_appregistry.types.resource_item_status

    out: GetAssociatedResourceFilter = []
    for item in data:
        out.append(
            aws_sdk_service_catalog_appregistry.types.resource_item_status.deserialize_json(
                item
            )
        )
    return out
