"""Generated from Smithy shape ``com.amazonaws.m2#GetDataSetExportTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_m2.types.identifier


class GetDataSetExportTaskRequest(TypedDict):
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The application identifier.</p>"""
    task_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The task identifier returned by the <a>CreateDataSetExportTask</a> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSetExportTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataSetExportTaskRequest:
    out: GetDataSetExportTaskRequest = {}  # type: ignore[typeddict-item]
    return out
