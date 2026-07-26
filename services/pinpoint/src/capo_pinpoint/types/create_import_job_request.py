"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreateImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.import_job_request


class CreateImportJobRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    import_job_request: NotRequired[
        "capo_pinpoint.types.import_job_request.ImportJobRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateImportJobRequest) -> dict:
    out: dict = {}
    if "import_job_request" in value:
        import capo_pinpoint.types.import_job_request

        out["ImportJobRequest"] = capo_pinpoint.types.import_job_request.serialize_json(
            value["import_job_request"]
        )
    return out


def deserialize_json(data: dict) -> CreateImportJobRequest:
    out: CreateImportJobRequest = {}  # type: ignore[typeddict-item]
    if "ImportJobRequest" in data:
        import capo_pinpoint.types.import_job_request

        out["import_job_request"] = (
            capo_pinpoint.types.import_job_request.deserialize_json(
                data["ImportJobRequest"]
            )
        )
    return out
