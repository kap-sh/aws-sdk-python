"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreateExportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.export_job_response


class CreateExportJobResponse(TypedDict):
    export_job_response: NotRequired[
        "aws_sdk_pinpoint.types.export_job_response.ExportJobResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateExportJobResponse) -> dict:
    out: dict = {}
    if "export_job_response" in value:
        import aws_sdk_pinpoint.types.export_job_response

        out["ExportJobResponse"] = (
            aws_sdk_pinpoint.types.export_job_response.serialize_json(
                value["export_job_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateExportJobResponse:
    out: CreateExportJobResponse = {}  # type: ignore[typeddict-item]
    if "ExportJobResponse" in data:
        import aws_sdk_pinpoint.types.export_job_response

        out["export_job_response"] = (
            aws_sdk_pinpoint.types.export_job_response.deserialize_json(
                data["ExportJobResponse"]
            )
        )
    return out
