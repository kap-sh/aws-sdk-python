"""Generated from Smithy shape ``com.amazonaws.schemas#__listOfSearchSchemaVersionSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_schemas.types.search_schema_version_summary

__listOfSearchSchemaVersionSummary: TypeAlias = list[
    "aws_sdk_schemas.types.search_schema_version_summary.SearchSchemaVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSearchSchemaVersionSummary) -> list:
    import aws_sdk_schemas.types.search_schema_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_schemas.types.search_schema_version_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfSearchSchemaVersionSummary:
    import aws_sdk_schemas.types.search_schema_version_summary

    out: __listOfSearchSchemaVersionSummary = []
    for item in data:
        out.append(
            aws_sdk_schemas.types.search_schema_version_summary.deserialize_json(item)
        )
    return out
