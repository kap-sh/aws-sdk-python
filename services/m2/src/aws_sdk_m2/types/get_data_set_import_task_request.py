"""Generated from Smithy shape ``com.amazonaws.m2#GetDataSetImportTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_m2.types.identifier


class GetDataSetImportTaskRequest(TypedDict):
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The application identifier.</p>"""
    task_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The task identifier returned by the <a>CreateDataSetImportTask</a> operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSetImportTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataSetImportTaskRequest:
    out: GetDataSetImportTaskRequest = {}  # type: ignore[typeddict-item]
    return out
