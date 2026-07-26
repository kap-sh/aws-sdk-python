"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetExportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.export_job_response


class GetExportJobResponse(TypedDict, closed=True):
    export_job_response: NotRequired[
        "capo_pinpoint.types.export_job_response.ExportJobResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetExportJobResponse) -> dict:
    out: dict = {}
    if "export_job_response" in value:
        import capo_pinpoint.types.export_job_response

        out["ExportJobResponse"] = (
            capo_pinpoint.types.export_job_response.serialize_json(
                value["export_job_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetExportJobResponse:
    out: GetExportJobResponse = {}  # type: ignore[typeddict-item]
    if "ExportJobResponse" in data:
        import capo_pinpoint.types.export_job_response

        out["export_job_response"] = (
            capo_pinpoint.types.export_job_response.deserialize_json(
                data["ExportJobResponse"]
            )
        )
    return out
