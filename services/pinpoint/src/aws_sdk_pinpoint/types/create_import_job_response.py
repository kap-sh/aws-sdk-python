"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreateImportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.import_job_response


class CreateImportJobResponse(TypedDict):
    import_job_response: NotRequired[
        "aws_sdk_pinpoint.types.import_job_response.ImportJobResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateImportJobResponse) -> dict:
    out: dict = {}
    if "import_job_response" in value:
        import aws_sdk_pinpoint.types.import_job_response

        out["ImportJobResponse"] = (
            aws_sdk_pinpoint.types.import_job_response.serialize_json(
                value["import_job_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateImportJobResponse:
    out: CreateImportJobResponse = {}  # type: ignore[typeddict-item]
    if "ImportJobResponse" in data:
        import aws_sdk_pinpoint.types.import_job_response

        out["import_job_response"] = (
            aws_sdk_pinpoint.types.import_job_response.deserialize_json(
                data["ImportJobResponse"]
            )
        )
    return out
