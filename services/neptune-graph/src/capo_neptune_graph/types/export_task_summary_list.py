"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExportTaskSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_neptune_graph.types.export_task_summary

ExportTaskSummaryList: TypeAlias = list[
    "capo_neptune_graph.types.export_task_summary.ExportTaskSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportTaskSummaryList) -> list:
    import capo_neptune_graph.types.export_task_summary

    out: list = []
    for item in value:
        out.append(capo_neptune_graph.types.export_task_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportTaskSummaryList:
    import capo_neptune_graph.types.export_task_summary

    out: ExportTaskSummaryList = []
    for item in data:
        out.append(capo_neptune_graph.types.export_task_summary.deserialize_json(item))
    return out
