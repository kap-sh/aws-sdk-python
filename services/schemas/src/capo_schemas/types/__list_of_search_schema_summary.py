"""Generated from Smithy shape ``com.amazonaws.schemas#__listOfSearchSchemaSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_schemas.types.search_schema_summary

__listOfSearchSchemaSummary: TypeAlias = list[
    "capo_schemas.types.search_schema_summary.SearchSchemaSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSearchSchemaSummary) -> list:
    import capo_schemas.types.search_schema_summary

    out: list = []
    for item in value:
        out.append(capo_schemas.types.search_schema_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSearchSchemaSummary:
    import capo_schemas.types.search_schema_summary

    out: __listOfSearchSchemaSummary = []
    for item in data:
        out.append(capo_schemas.types.search_schema_summary.deserialize_json(item))
    return out
