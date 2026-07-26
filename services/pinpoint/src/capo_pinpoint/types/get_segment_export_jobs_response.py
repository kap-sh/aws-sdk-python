"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetSegmentExportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.export_jobs_response


class GetSegmentExportJobsResponse(TypedDict, closed=True):
    export_jobs_response: NotRequired[
        "capo_pinpoint.types.export_jobs_response.ExportJobsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentExportJobsResponse) -> dict:
    out: dict = {}
    if "export_jobs_response" in value:
        import capo_pinpoint.types.export_jobs_response

        out["ExportJobsResponse"] = (
            capo_pinpoint.types.export_jobs_response.serialize_json(
                value["export_jobs_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSegmentExportJobsResponse:
    out: GetSegmentExportJobsResponse = {}  # type: ignore[typeddict-item]
    if "ExportJobsResponse" in data:
        import capo_pinpoint.types.export_jobs_response

        out["export_jobs_response"] = (
            capo_pinpoint.types.export_jobs_response.deserialize_json(
                data["ExportJobsResponse"]
            )
        )
    return out
