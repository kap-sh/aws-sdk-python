"""Generated from Smithy shape ``com.amazonaws.s3tables#TableSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3tables.types.table_summary

TableSummaryList: TypeAlias = list["capo_s3tables.types.table_summary.TableSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: TableSummaryList) -> list:
    import capo_s3tables.types.table_summary

    out: list = []
    for item in value:
        out.append(capo_s3tables.types.table_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TableSummaryList:
    import capo_s3tables.types.table_summary

    out: TableSummaryList = []
    for item in data:
        out.append(capo_s3tables.types.table_summary.deserialize_json(item))
    return out
