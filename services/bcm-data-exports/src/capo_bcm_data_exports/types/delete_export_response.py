"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#DeleteExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.arn


class DeleteExportResponse(TypedDict, closed=True):
    export_arn: NotRequired["capo_bcm_data_exports.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for this export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteExportResponse) -> dict:
    out: dict = {}
    if "export_arn" in value:
        out["ExportArn"] = value["export_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteExportResponse:
    out: DeleteExportResponse = {}  # type: ignore[typeddict-item]
    if "ExportArn" in data:
        out["export_arn"] = data["ExportArn"]
    return out
