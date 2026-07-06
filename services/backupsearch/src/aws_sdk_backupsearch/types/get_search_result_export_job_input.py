"""Generated from Smithy shape ``com.amazonaws.backupsearch#GetSearchResultExportJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.generic_id


class GetSearchResultExportJobInput(TypedDict, closed=True):
    export_job_identifier: "aws_sdk_backupsearch.types.generic_id.GenericId"
    """<p>This is the unique string that identifies a specific export job.</p> <p>Required for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSearchResultExportJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSearchResultExportJobInput:
    out: GetSearchResultExportJobInput = {}  # type: ignore[typeddict-item]
    return out
