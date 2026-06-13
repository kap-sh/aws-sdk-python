"""Generated from Smithy shape ``com.amazonaws.mgn#StartExportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.export_task


class StartExportResponse(TypedDict):
    export_task: NotRequired["aws_sdk_mgn.types.export_task.ExportTask"]
    """<p>Start export response export task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartExportResponse) -> dict:
    out: dict = {}
    if "export_task" in value:
        import aws_sdk_mgn.types.export_task

        out["exportTask"] = aws_sdk_mgn.types.export_task.serialize_json(
            value["export_task"]
        )
    return out


def deserialize_json(data: dict) -> StartExportResponse:
    out: StartExportResponse = {}  # type: ignore[typeddict-item]
    if "exportTask" in data:
        import aws_sdk_mgn.types.export_task

        out["export_task"] = aws_sdk_mgn.types.export_task.deserialize_json(
            data["exportTask"]
        )
    return out
