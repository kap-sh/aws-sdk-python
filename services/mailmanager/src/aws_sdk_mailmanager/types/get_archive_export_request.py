"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetArchiveExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.export_id


class GetArchiveExportRequest(TypedDict, closed=True):
    export_id: "aws_sdk_mailmanager.types.export_id.ExportId"
    """<p>The identifier of the export job to get details for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetArchiveExportRequest) -> dict:
    out: dict = {}
    out["ExportId"] = value["export_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetArchiveExportRequest:
    out: GetArchiveExportRequest = {}  # type: ignore[typeddict-item]
    if "ExportId" in data:
        out["export_id"] = data["ExportId"]
    else:
        raise DeserializationError("GetArchiveExportRequest.export_id required")
    return out
