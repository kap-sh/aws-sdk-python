"""Generated from Smithy shape ``com.amazonaws.m2#ListDataSetExportHistoryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.data_set_export_task_list
    import aws_sdk_m2.types.next_token


class ListDataSetExportHistoryResponse(TypedDict):
    data_set_export_tasks: (
        "aws_sdk_m2.types.data_set_export_task_list.DataSetExportTaskList"
    )
    """<p>The data set export tasks.</p>"""
    next_token: NotRequired["aws_sdk_m2.types.next_token.NextToken"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to this operation to retrieve the next set of items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSetExportHistoryResponse) -> dict:
    out: dict = {}
    import aws_sdk_m2.types.data_set_export_task_list

    out["dataSetExportTasks"] = (
        aws_sdk_m2.types.data_set_export_task_list.serialize_json(
            value["data_set_export_tasks"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataSetExportHistoryResponse:
    out: ListDataSetExportHistoryResponse = {}  # type: ignore[typeddict-item]
    if "dataSetExportTasks" in data:
        import aws_sdk_m2.types.data_set_export_task_list

        out["data_set_export_tasks"] = (
            aws_sdk_m2.types.data_set_export_task_list.deserialize_json(
                data["dataSetExportTasks"]
            )
        )
    else:
        raise DeserializationError(
            "ListDataSetExportHistoryResponse.data_set_export_tasks required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
