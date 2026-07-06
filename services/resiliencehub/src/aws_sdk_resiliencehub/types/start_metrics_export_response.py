"""Generated from Smithy shape ``com.amazonaws.resiliencehub#StartMetricsExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.metrics_export_status_type
    import aws_sdk_resiliencehub.types.string255


class StartMetricsExportResponse(TypedDict, closed=True):
    metrics_export_id: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>Identifier of the metrics export task.</p>"""
    status: (
        "aws_sdk_resiliencehub.types.metrics_export_status_type.MetricsExportStatusType"
    )
    """<p>Indicates the status of the metrics export task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMetricsExportResponse) -> dict:
    out: dict = {}
    out["metricsExportId"] = value["metrics_export_id"]
    import aws_sdk_resiliencehub.types.metrics_export_status_type

    out["status"] = (
        aws_sdk_resiliencehub.types.metrics_export_status_type.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartMetricsExportResponse:
    out: StartMetricsExportResponse = {}  # type: ignore[typeddict-item]
    if "metricsExportId" in data:
        out["metrics_export_id"] = data["metricsExportId"]
    else:
        raise DeserializationError(
            "StartMetricsExportResponse.metrics_export_id required"
        )
    if "status" in data:
        import aws_sdk_resiliencehub.types.metrics_export_status_type

        out["status"] = (
            aws_sdk_resiliencehub.types.metrics_export_status_type.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("StartMetricsExportResponse.status required")
    return out
