"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.schema_summary

SchemaSummaryList: TypeAlias = list[
    "capo_cleanrooms.types.schema_summary.SchemaSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaSummaryList) -> list:
    import capo_cleanrooms.types.schema_summary

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.schema_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SchemaSummaryList:
    import capo_cleanrooms.types.schema_summary

    out: SchemaSummaryList = []
    for item in data:
        out.append(capo_cleanrooms.types.schema_summary.deserialize_json(item))
    return out
