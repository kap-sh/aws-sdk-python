"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetSegmentImportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.import_jobs_response


class GetSegmentImportJobsResponse(TypedDict, closed=True):
    import_jobs_response: NotRequired[
        "aws_sdk_pinpoint.types.import_jobs_response.ImportJobsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentImportJobsResponse) -> dict:
    out: dict = {}
    if "import_jobs_response" in value:
        import aws_sdk_pinpoint.types.import_jobs_response

        out["ImportJobsResponse"] = (
            aws_sdk_pinpoint.types.import_jobs_response.serialize_json(
                value["import_jobs_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSegmentImportJobsResponse:
    out: GetSegmentImportJobsResponse = {}  # type: ignore[typeddict-item]
    if "ImportJobsResponse" in data:
        import aws_sdk_pinpoint.types.import_jobs_response

        out["import_jobs_response"] = (
            aws_sdk_pinpoint.types.import_jobs_response.deserialize_json(
                data["ImportJobsResponse"]
            )
        )
    return out
