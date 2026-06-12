"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListImportFileTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.list_import_file_task_information
    import aws_sdk_migrationhubstrategy.types.string


class ListImportFileTaskResponse(TypedDict):
    task_infos: NotRequired[
        "aws_sdk_migrationhubstrategy.types.list_import_file_task_information.ListImportFileTaskInformation"
    ]
    """<p> Lists information about the files you import.</p>"""
    next_token: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> The token you use to retrieve the next set of results, or null if there are no more results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportFileTaskResponse) -> dict:
    out: dict = {}
    if "task_infos" in value:
        import aws_sdk_migrationhubstrategy.types.list_import_file_task_information

        out["taskInfos"] = (
            aws_sdk_migrationhubstrategy.types.list_import_file_task_information.serialize_json(
                value["task_infos"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImportFileTaskResponse:
    out: ListImportFileTaskResponse = {}  # type: ignore[typeddict-item]
    if "taskInfos" in data:
        import aws_sdk_migrationhubstrategy.types.list_import_file_task_information

        out["task_infos"] = (
            aws_sdk_migrationhubstrategy.types.list_import_file_task_information.deserialize_json(
                data["taskInfos"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
