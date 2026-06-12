"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ApplicationTagDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.tag_key
    import aws_sdk_service_catalog_appregistry.types.tag_value

ApplicationTagDefinition: TypeAlias = dict[
    "aws_sdk_service_catalog_appregistry.types.tag_key.TagKey",
    "aws_sdk_service_catalog_appregistry.types.tag_value.TagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ApplicationTagDefinition) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ApplicationTagDefinition:
    out: ApplicationTagDefinition = {}
    for key, value in data.items():
        out[key] = value
    return out
