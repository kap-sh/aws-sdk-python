"""Generated from Smithy shape ``com.amazonaws.qconnect#GetImportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.import_job_data


class GetImportJobResponse(TypedDict):
    import_job: NotRequired["aws_sdk_qconnect.types.import_job_data.ImportJobData"]
    """<p>The import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportJobResponse) -> dict:
    out: dict = {}
    if "import_job" in value:
        import aws_sdk_qconnect.types.import_job_data

        out["importJob"] = aws_sdk_qconnect.types.import_job_data.serialize_json(
            value["import_job"]
        )
    return out


def deserialize_json(data: dict) -> GetImportJobResponse:
    out: GetImportJobResponse = {}  # type: ignore[typeddict-item]
    if "importJob" in data:
        import aws_sdk_qconnect.types.import_job_data

        out["import_job"] = aws_sdk_qconnect.types.import_job_data.deserialize_json(
            data["importJob"]
        )
    return out
