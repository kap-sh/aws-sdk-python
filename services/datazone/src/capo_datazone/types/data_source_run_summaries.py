"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceRunSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.data_source_run_summary

DataSourceRunSummaries: TypeAlias = list[
    "capo_datazone.types.data_source_run_summary.DataSourceRunSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceRunSummaries) -> list:
    import capo_datazone.types.data_source_run_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.data_source_run_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSourceRunSummaries:
    import capo_datazone.types.data_source_run_summary

    out: DataSourceRunSummaries = []
    for item in data:
        out.append(capo_datazone.types.data_source_run_summary.deserialize_json(item))
    return out
