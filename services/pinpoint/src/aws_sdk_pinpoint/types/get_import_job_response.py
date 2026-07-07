"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.import_job_response


class GetImportJobResponse(TypedDict, closed=True):
    import_job_response: NotRequired[
        "aws_sdk_pinpoint.types.import_job_response.ImportJobResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetImportJobResponse) -> dict:
    out: dict = {}
    if "import_job_response" in value:
        import aws_sdk_pinpoint.types.import_job_response

        out["ImportJobResponse"] = (
            aws_sdk_pinpoint.types.import_job_response.serialize_json(
                value["import_job_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetImportJobResponse:
    out: GetImportJobResponse = {}  # type: ignore[typeddict-item]
    if "ImportJobResponse" in data:
        import aws_sdk_pinpoint.types.import_job_response

        out["import_job_response"] = (
            aws_sdk_pinpoint.types.import_job_response.deserialize_json(
                data["ImportJobResponse"]
            )
        )
    return out
