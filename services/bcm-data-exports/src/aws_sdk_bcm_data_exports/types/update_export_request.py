"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#UpdateExportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.arn
    import aws_sdk_bcm_data_exports.types.export


class UpdateExportRequest(TypedDict):
    export_arn: "aws_sdk_bcm_data_exports.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for this export.</p>"""
    export: "aws_sdk_bcm_data_exports.types.export.Export"
    """<p>The name and query details for the export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateExportRequest) -> dict:
    out: dict = {}
    out["ExportArn"] = value["export_arn"]
    import aws_sdk_bcm_data_exports.types.export

    out["Export"] = aws_sdk_bcm_data_exports.types.export.serialize_aws_json_1_1(
        value["export"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateExportRequest:
    out: UpdateExportRequest = {}  # type: ignore[typeddict-item]
    if "ExportArn" in data:
        out["export_arn"] = data["ExportArn"]
    else:
        raise DeserializationError("UpdateExportRequest.export_arn required")
    if "Export" in data:
        import aws_sdk_bcm_data_exports.types.export

        out["export"] = aws_sdk_bcm_data_exports.types.export.deserialize_aws_json_1_1(
            data["Export"]
        )
    else:
        raise DeserializationError("UpdateExportRequest.export required")
    return out
