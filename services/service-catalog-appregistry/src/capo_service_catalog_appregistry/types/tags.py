"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.tag_key
    import capo_service_catalog_appregistry.types.tag_value

Tags: TypeAlias = dict[
    "capo_service_catalog_appregistry.types.tag_key.TagKey",
    "capo_service_catalog_appregistry.types.tag_value.TagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Tags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Tags:
    out: Tags = {}
    for key, value in data.items():
        out[key] = value
    return out
