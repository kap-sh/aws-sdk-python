"""Generated from Smithy shape ``com.amazonaws.schemas#__listOfSchemaSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_schemas.types.schema_summary

__listOfSchemaSummary: TypeAlias = list[
    "aws_sdk_schemas.types.schema_summary.SchemaSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSchemaSummary) -> list:
    import aws_sdk_schemas.types.schema_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_schemas.types.schema_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSchemaSummary:
    import aws_sdk_schemas.types.schema_summary

    out: __listOfSchemaSummary = []
    for item in data:
        out.append(aws_sdk_schemas.types.schema_summary.deserialize_json(item))
    return out
