"""Generated from Smithy shape ``com.amazonaws.mailmanager#ExportSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.export_id
    import aws_sdk_mailmanager.types.export_status


class ExportSummary(TypedDict):
    export_id: NotRequired["aws_sdk_mailmanager.types.export_id.ExportId"]
    """<p>The unique identifier of the export job.</p>"""
    status: NotRequired["aws_sdk_mailmanager.types.export_status.ExportStatus"]
    """<p>The current status of the export job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportSummary) -> dict:
    out: dict = {}
    if "export_id" in value:
        out["ExportId"] = value["export_id"]
    if "status" in value:
        import aws_sdk_mailmanager.types.export_status

        out["Status"] = aws_sdk_mailmanager.types.export_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportSummary:
    out: ExportSummary = {}  # type: ignore[typeddict-item]
    if "ExportId" in data:
        out["export_id"] = data["ExportId"]
    if "Status" in data:
        import aws_sdk_mailmanager.types.export_status

        out["status"] = (
            aws_sdk_mailmanager.types.export_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
