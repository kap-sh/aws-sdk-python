"""Generated from Smithy shape ``com.amazonaws.entityresolution#SchemaMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.schema_mapping_summary

SchemaMappingList: TypeAlias = list[
    "aws_sdk_entityresolution.types.schema_mapping_summary.SchemaMappingSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaMappingList) -> list:
    import aws_sdk_entityresolution.types.schema_mapping_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.schema_mapping_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SchemaMappingList:
    import aws_sdk_entityresolution.types.schema_mapping_summary

    out: SchemaMappingList = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.schema_mapping_summary.deserialize_json(item)
        )
    return out
