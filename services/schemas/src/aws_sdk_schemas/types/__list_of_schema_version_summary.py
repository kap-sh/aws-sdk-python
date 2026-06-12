"""Generated from Smithy shape ``com.amazonaws.schemas#__listOfSchemaVersionSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_schemas.types.schema_version_summary

__listOfSchemaVersionSummary: TypeAlias = list[
    "aws_sdk_schemas.types.schema_version_summary.SchemaVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSchemaVersionSummary) -> list:
    import aws_sdk_schemas.types.schema_version_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_schemas.types.schema_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSchemaVersionSummary:
    import aws_sdk_schemas.types.schema_version_summary

    out: __listOfSchemaVersionSummary = []
    for item in data:
        out.append(aws_sdk_schemas.types.schema_version_summary.deserialize_json(item))
    return out
