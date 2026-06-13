"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ImportTaskSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.import_task_summary

ImportTaskSummaryList: TypeAlias = list[
    "aws_sdk_neptune_graph.types.import_task_summary.ImportTaskSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportTaskSummaryList) -> list:
    import aws_sdk_neptune_graph.types.import_task_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_neptune_graph.types.import_task_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportTaskSummaryList:
    import aws_sdk_neptune_graph.types.import_task_summary

    out: ImportTaskSummaryList = []
    for item in data:
        out.append(
            aws_sdk_neptune_graph.types.import_task_summary.deserialize_json(item)
        )
    return out
