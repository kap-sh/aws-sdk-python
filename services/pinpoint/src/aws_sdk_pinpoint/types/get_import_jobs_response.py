"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetImportJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.import_jobs_response


class GetImportJobsResponse(TypedDict):
    import_jobs_response: NotRequired[
        "aws_sdk_pinpoint.types.import_jobs_response.ImportJobsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetImportJobsResponse) -> dict:
    out: dict = {}
    if "import_jobs_response" in value:
        import aws_sdk_pinpoint.types.import_jobs_response

        out["ImportJobsResponse"] = (
            aws_sdk_pinpoint.types.import_jobs_response.serialize_json(
                value["import_jobs_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetImportJobsResponse:
    out: GetImportJobsResponse = {}  # type: ignore[typeddict-item]
    if "ImportJobsResponse" in data:
        import aws_sdk_pinpoint.types.import_jobs_response

        out["import_jobs_response"] = (
            aws_sdk_pinpoint.types.import_jobs_response.deserialize_json(
                data["ImportJobsResponse"]
            )
        )
    return out
