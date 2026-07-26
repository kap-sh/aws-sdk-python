"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StartImportTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.import_task


class StartImportTaskResponse(TypedDict, closed=True):
    task: NotRequired["capo_application_discovery_service.types.import_task.ImportTask"]
    """<p>An array of information related to the import task request including status information, times, IDs, the Amazon S3 Object URL for the import file, and more. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartImportTaskResponse) -> dict:
    out: dict = {}
    if "task" in value:
        import capo_application_discovery_service.types.import_task

        out["task"] = (
            capo_application_discovery_service.types.import_task.serialize_aws_json_1_1(
                value["task"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartImportTaskResponse:
    out: StartImportTaskResponse = {}  # type: ignore[typeddict-item]
    if "task" in data:
        import capo_application_discovery_service.types.import_task

        out["task"] = (
            capo_application_discovery_service.types.import_task.deserialize_aws_json_1_1(
                data["task"]
            )
        )
    return out
