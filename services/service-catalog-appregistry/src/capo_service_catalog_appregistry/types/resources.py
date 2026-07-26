"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#Resources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.resource_info

Resources: TypeAlias = list[
    "capo_service_catalog_appregistry.types.resource_info.ResourceInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: Resources) -> list:
    import capo_service_catalog_appregistry.types.resource_info

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog_appregistry.types.resource_info.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> Resources:
    import capo_service_catalog_appregistry.types.resource_info

    out: Resources = []
    for item in data:
        out.append(
            capo_service_catalog_appregistry.types.resource_info.deserialize_json(item)
        )
    return out
