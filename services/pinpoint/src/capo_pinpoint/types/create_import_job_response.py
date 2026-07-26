"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreateImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.import_job_response


class CreateImportJobResponse(TypedDict, closed=True):
    import_job_response: NotRequired[
        "capo_pinpoint.types.import_job_response.ImportJobResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateImportJobResponse) -> dict:
    out: dict = {}
    if "import_job_response" in value:
        import capo_pinpoint.types.import_job_response

        out["ImportJobResponse"] = (
            capo_pinpoint.types.import_job_response.serialize_json(
                value["import_job_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateImportJobResponse:
    out: CreateImportJobResponse = {}  # type: ignore[typeddict-item]
    if "ImportJobResponse" in data:
        import capo_pinpoint.types.import_job_response

        out["import_job_response"] = (
            capo_pinpoint.types.import_job_response.deserialize_json(
                data["ImportJobResponse"]
            )
        )
    return out
