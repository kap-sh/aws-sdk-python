"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExportReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.arn
    import aws_sdk_bcm_data_exports.types.export_name
    import aws_sdk_bcm_data_exports.types.export_status


class ExportReference(TypedDict, closed=True):
    export_arn: "aws_sdk_bcm_data_exports.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for this export.</p>"""
    export_name: "aws_sdk_bcm_data_exports.types.export_name.ExportName"
    """<p>The name of this specific data export.</p>"""
    export_status: "aws_sdk_bcm_data_exports.types.export_status.ExportStatus"
    """<p>The status of this specific data export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportReference) -> dict:
    out: dict = {}
    out["ExportArn"] = value["export_arn"]
    out["ExportName"] = value["export_name"]
    import aws_sdk_bcm_data_exports.types.export_status

    out["ExportStatus"] = (
        aws_sdk_bcm_data_exports.types.export_status.serialize_aws_json_1_1(
            value["export_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportReference:
    out: ExportReference = {}  # type: ignore[typeddict-item]
    if "ExportArn" in data:
        out["export_arn"] = data["ExportArn"]
    else:
        raise DeserializationError("ExportReference.export_arn required")
    if "ExportName" in data:
        out["export_name"] = data["ExportName"]
    else:
        raise DeserializationError("ExportReference.export_name required")
    if "ExportStatus" in data:
        import aws_sdk_bcm_data_exports.types.export_status

        out["export_status"] = (
            aws_sdk_bcm_data_exports.types.export_status.deserialize_aws_json_1_1(
                data["ExportStatus"]
            )
        )
    else:
        raise DeserializationError("ExportReference.export_status required")
    return out
