"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#CreateExportResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.arn

class CreateExportResponse(TypedDict):
    export_arn: NotRequired["aws_sdk_bcm_data_exports.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for this export.</p>"""

# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExportResponse) -> dict:
    out: dict = {}
    if "export_arn" in value:
        out["ExportArn"] = value["export_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExportResponse:
    out: CreateExportResponse = {}  # type: ignore[typeddict-item]
    if "ExportArn" in data:
        out["export_arn"] = data["ExportArn"]
    return out