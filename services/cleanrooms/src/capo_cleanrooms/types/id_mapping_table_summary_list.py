"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdMappingTableSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.id_mapping_table_summary

IdMappingTableSummaryList: TypeAlias = list[
    "capo_cleanrooms.types.id_mapping_table_summary.IdMappingTableSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingTableSummaryList) -> list:
    import capo_cleanrooms.types.id_mapping_table_summary

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.id_mapping_table_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> IdMappingTableSummaryList:
    import capo_cleanrooms.types.id_mapping_table_summary

    out: IdMappingTableSummaryList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.id_mapping_table_summary.deserialize_json(item)
        )
    return out
