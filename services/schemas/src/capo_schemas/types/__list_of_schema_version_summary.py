"""Generated from Smithy shape ``com.amazonaws.schemas#__listOfSchemaVersionSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_schemas.types.schema_version_summary

__listOfSchemaVersionSummary: TypeAlias = list[
    "capo_schemas.types.schema_version_summary.SchemaVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSchemaVersionSummary) -> list:
    import capo_schemas.types.schema_version_summary

    out: list = []
    for item in value:
        out.append(capo_schemas.types.schema_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSchemaVersionSummary:
    import capo_schemas.types.schema_version_summary

    out: __listOfSchemaVersionSummary = []
    for item in data:
        out.append(capo_schemas.types.schema_version_summary.deserialize_json(item))
    return out
