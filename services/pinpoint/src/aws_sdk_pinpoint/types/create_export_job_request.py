"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreateExportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.export_job_request


class CreateExportJobRequest(TypedDict):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    export_job_request: NotRequired[
        "aws_sdk_pinpoint.types.export_job_request.ExportJobRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateExportJobRequest) -> dict:
    out: dict = {}
    if "export_job_request" in value:
        import aws_sdk_pinpoint.types.export_job_request

        out["ExportJobRequest"] = (
            aws_sdk_pinpoint.types.export_job_request.serialize_json(
                value["export_job_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateExportJobRequest:
    out: CreateExportJobRequest = {}  # type: ignore[typeddict-item]
    if "ExportJobRequest" in data:
        import aws_sdk_pinpoint.types.export_job_request

        out["export_job_request"] = (
            aws_sdk_pinpoint.types.export_job_request.deserialize_json(
                data["ExportJobRequest"]
            )
        )
    return out
