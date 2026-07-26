"""Generated from Smithy shape ``com.amazonaws.schemas#__listOfSchemaSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_schemas.types.schema_summary

__listOfSchemaSummary: TypeAlias = list[
    "capo_schemas.types.schema_summary.SchemaSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSchemaSummary) -> list:
    import capo_schemas.types.schema_summary

    out: list = []
    for item in value:
        out.append(capo_schemas.types.schema_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSchemaSummary:
    import capo_schemas.types.schema_summary

    out: __listOfSchemaSummary = []
    for item in data:
        out.append(capo_schemas.types.schema_summary.deserialize_json(item))
    return out
