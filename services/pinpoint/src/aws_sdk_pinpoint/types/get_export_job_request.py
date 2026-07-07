"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class GetExportJobRequest(TypedDict, closed=True):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    job_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetExportJobRequest:
    out: GetExportJobRequest = {}  # type: ignore[typeddict-item]
    return out
