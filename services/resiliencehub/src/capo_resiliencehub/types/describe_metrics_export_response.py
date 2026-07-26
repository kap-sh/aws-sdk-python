"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeMetricsExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.metrics_export_status_type
    import capo_resiliencehub.types.s3_location
    import capo_resiliencehub.types.string255
    import capo_resiliencehub.types.string500


class DescribeMetricsExportResponse(TypedDict, closed=True):
    metrics_export_id: "capo_resiliencehub.types.string255.String255"
    """<p>Identifier for the metrics export task.</p>"""
    status: (
        "capo_resiliencehub.types.metrics_export_status_type.MetricsExportStatusType"
    )
    """<p>Indicates the status of the metrics export task.</p>"""
    export_location: NotRequired["capo_resiliencehub.types.s3_location.S3Location"]
    """<p>Specifies the name of the Amazon S3 bucket where the exported metrics is stored.</p>"""
    error_message: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>Explains the error that occurred while exporting the metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMetricsExportResponse) -> dict:
    out: dict = {}
    out["metricsExportId"] = value["metrics_export_id"]
    import capo_resiliencehub.types.metrics_export_status_type

    out["status"] = capo_resiliencehub.types.metrics_export_status_type.serialize_json(
        value["status"]
    )
    if "export_location" in value:
        import capo_resiliencehub.types.s3_location

        out["exportLocation"] = capo_resiliencehub.types.s3_location.serialize_json(
            value["export_location"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> DescribeMetricsExportResponse:
    out: DescribeMetricsExportResponse = {}  # type: ignore[typeddict-item]
    if "metricsExportId" in data:
        out["metrics_export_id"] = data["metricsExportId"]
    else:
        raise DeserializationError(
            "DescribeMetricsExportResponse.metrics_export_id required"
        )
    if "status" in data:
        import capo_resiliencehub.types.metrics_export_status_type

        out["status"] = (
            capo_resiliencehub.types.metrics_export_status_type.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DescribeMetricsExportResponse.status required")
    if "exportLocation" in data:
        import capo_resiliencehub.types.s3_location

        out["export_location"] = capo_resiliencehub.types.s3_location.deserialize_json(
            data["exportLocation"]
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
