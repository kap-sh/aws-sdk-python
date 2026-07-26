"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.export_arn
    import capo_dynamodb.types.export_status
    import capo_dynamodb.types.export_type


class ExportSummary(TypedDict, closed=True):
    export_arn: NotRequired["capo_dynamodb.types.export_arn.ExportArn"]
    """<p>The Amazon Resource Name (ARN) of the export.</p>"""
    export_status: NotRequired["capo_dynamodb.types.export_status.ExportStatus"]
    """<p>Export can be in one of the following states: IN_PROGRESS, COMPLETED, or FAILED.</p>"""
    export_type: NotRequired["capo_dynamodb.types.export_type.ExportType"]
    """<p>The type of export that was performed. Valid values are <code>FULL_EXPORT</code> or <code>INCREMENTAL_EXPORT</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportSummary) -> dict:
    out: dict = {}
    if "export_arn" in value:
        out["ExportArn"] = value["export_arn"]
    if "export_status" in value:
        import capo_dynamodb.types.export_status

        out["ExportStatus"] = capo_dynamodb.types.export_status.serialize_aws_json_1_0(
            value["export_status"]
        )
    if "export_type" in value:
        import capo_dynamodb.types.export_type

        out["ExportType"] = capo_dynamodb.types.export_type.serialize_aws_json_1_0(
            value["export_type"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportSummary:
    out: ExportSummary = {}  # type: ignore[typeddict-item]
    if "ExportArn" in data:
        out["export_arn"] = data["ExportArn"]
    if "ExportStatus" in data:
        import capo_dynamodb.types.export_status

        out["export_status"] = (
            capo_dynamodb.types.export_status.deserialize_aws_json_1_0(
                data["ExportStatus"]
            )
        )
    if "ExportType" in data:
        import capo_dynamodb.types.export_type

        out["export_type"] = capo_dynamodb.types.export_type.deserialize_aws_json_1_0(
            data["ExportType"]
        )
    return out
