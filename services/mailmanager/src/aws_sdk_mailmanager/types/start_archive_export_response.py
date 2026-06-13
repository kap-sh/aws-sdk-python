"""Generated from Smithy shape ``com.amazonaws.mailmanager#StartArchiveExportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.export_id


class StartArchiveExportResponse(TypedDict):
    export_id: NotRequired["aws_sdk_mailmanager.types.export_id.ExportId"]
    """<p>The unique identifier for the initiated export job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartArchiveExportResponse) -> dict:
    out: dict = {}
    if "export_id" in value:
        out["ExportId"] = value["export_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartArchiveExportResponse:
    out: StartArchiveExportResponse = {}  # type: ignore[typeddict-item]
    if "ExportId" in data:
        out["export_id"] = data["ExportId"]
    return out
