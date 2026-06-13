"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#GetExportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.arn


class GetExportRequest(TypedDict):
    export_arn: "aws_sdk_bcm_data_exports.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for this export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExportRequest) -> dict:
    out: dict = {}
    out["ExportArn"] = value["export_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExportRequest:
    out: GetExportRequest = {}  # type: ignore[typeddict-item]
    if "ExportArn" in data:
        out["export_arn"] = data["ExportArn"]
    else:
        raise DeserializationError("GetExportRequest.export_arn required")
    return out
