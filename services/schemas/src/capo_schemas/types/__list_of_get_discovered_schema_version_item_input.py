"""Generated from Smithy shape ``com.amazonaws.schemas#__listOfGetDiscoveredSchemaVersionItemInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_schemas.types.get_discovered_schema_version_item_input

__listOfGetDiscoveredSchemaVersionItemInput: TypeAlias = list[
    "capo_schemas.types.get_discovered_schema_version_item_input.GetDiscoveredSchemaVersionItemInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfGetDiscoveredSchemaVersionItemInput) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOfGetDiscoveredSchemaVersionItemInput:
    return list(data)
