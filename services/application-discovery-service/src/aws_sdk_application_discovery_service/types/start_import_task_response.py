"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StartImportTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.import_task


class StartImportTaskResponse(TypedDict):
    task: NotRequired[
        "aws_sdk_application_discovery_service.types.import_task.ImportTask"
    ]
    """<p>An array of information related to the import task request including status information, times, IDs, the Amazon S3 Object URL for the import file, and more. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartImportTaskResponse) -> dict:
    out: dict = {}
    if "task" in value:
        import aws_sdk_application_discovery_service.types.import_task

        out["task"] = (
            aws_sdk_application_discovery_service.types.import_task.serialize_aws_json_1_1(
                value["task"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartImportTaskResponse:
    out: StartImportTaskResponse = {}  # type: ignore[typeddict-item]
    if "task" in data:
        import aws_sdk_application_discovery_service.types.import_task

        out["task"] = (
            aws_sdk_application_discovery_service.types.import_task.deserialize_aws_json_1_1(
                data["task"]
            )
        )
    return out
