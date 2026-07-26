"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#TagKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.tag_key

TagKeys: TypeAlias = list["capo_service_catalog_appregistry.types.tag_key.TagKey"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeys) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeys:
    return list(data)
