"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#GetExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.export
    import aws_sdk_bcm_data_exports.types.export_status


class GetExportResponse(TypedDict, closed=True):
    export: NotRequired["aws_sdk_bcm_data_exports.types.export.Export"]
    """<p>The data for this specific export.</p>"""
    export_status: NotRequired[
        "aws_sdk_bcm_data_exports.types.export_status.ExportStatus"
    ]
    """<p>The status of this specific export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExportResponse) -> dict:
    out: dict = {}
    if "export" in value:
        import aws_sdk_bcm_data_exports.types.export

        out["Export"] = aws_sdk_bcm_data_exports.types.export.serialize_aws_json_1_1(
            value["export"]
        )
    if "export_status" in value:
        import aws_sdk_bcm_data_exports.types.export_status

        out["ExportStatus"] = (
            aws_sdk_bcm_data_exports.types.export_status.serialize_aws_json_1_1(
                value["export_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExportResponse:
    out: GetExportResponse = {}  # type: ignore[typeddict-item]
    if "Export" in data:
        import aws_sdk_bcm_data_exports.types.export

        out["export"] = aws_sdk_bcm_data_exports.types.export.deserialize_aws_json_1_1(
            data["Export"]
        )
    if "ExportStatus" in data:
        import aws_sdk_bcm_data_exports.types.export_status

        out["export_status"] = (
            aws_sdk_bcm_data_exports.types.export_status.deserialize_aws_json_1_1(
                data["ExportStatus"]
            )
        )
    return out
