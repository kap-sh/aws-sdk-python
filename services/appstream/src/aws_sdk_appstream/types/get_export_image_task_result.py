"""Generated from Smithy shape ``com.amazonaws.appstream#GetExportImageTaskResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.export_image_task


class GetExportImageTaskResult(TypedDict, closed=True):
    export_image_task: NotRequired[
        "aws_sdk_appstream.types.export_image_task.ExportImageTask"
    ]
    """<p>Information about the export image task, including its current state, created date, and any error details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExportImageTaskResult) -> dict:
    out: dict = {}
    if "export_image_task" in value:
        import aws_sdk_appstream.types.export_image_task

        out["ExportImageTask"] = (
            aws_sdk_appstream.types.export_image_task.serialize_aws_json_1_1(
                value["export_image_task"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExportImageTaskResult:
    out: GetExportImageTaskResult = {}  # type: ignore[typeddict-item]
    if "ExportImageTask" in data:
        import aws_sdk_appstream.types.export_image_task

        out["export_image_task"] = (
            aws_sdk_appstream.types.export_image_task.deserialize_aws_json_1_1(
                data["ExportImageTask"]
            )
        )
    return out
