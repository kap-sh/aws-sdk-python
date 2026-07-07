"""Generated from Smithy shape ``com.amazonaws.omics#ExportReadSetDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.job_status_message
    import aws_sdk_omics.types.read_set_export_job_item_status
    import aws_sdk_omics.types.read_set_id


class ExportReadSetDetail(TypedDict, closed=True):
    id: "aws_sdk_omics.types.read_set_id.ReadSetId"
    """<p>The set's ID.</p>"""
    status: (
        "aws_sdk_omics.types.read_set_export_job_item_status.ReadSetExportJobItemStatus"
    )
    """<p>The set's status.</p>"""
    status_message: NotRequired[
        "aws_sdk_omics.types.job_status_message.JobStatusMessage"
    ]
    """<p>The set's status message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportReadSetDetail) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> ExportReadSetDetail:
    out: ExportReadSetDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ExportReadSetDetail.id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ExportReadSetDetail.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    return out
