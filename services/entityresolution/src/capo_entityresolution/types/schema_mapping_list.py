"""Generated from Smithy shape ``com.amazonaws.entityresolution#SchemaMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.schema_mapping_summary

SchemaMappingList: TypeAlias = list[
    "capo_entityresolution.types.schema_mapping_summary.SchemaMappingSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaMappingList) -> list:
    import capo_entityresolution.types.schema_mapping_summary

    out: list = []
    for item in value:
        out.append(
            capo_entityresolution.types.schema_mapping_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SchemaMappingList:
    import capo_entityresolution.types.schema_mapping_summary

    out: SchemaMappingList = []
    for item in data:
        out.append(
            capo_entityresolution.types.schema_mapping_summary.deserialize_json(item)
        )
    return out
