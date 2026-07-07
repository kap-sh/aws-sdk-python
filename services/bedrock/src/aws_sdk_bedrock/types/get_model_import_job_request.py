"""Generated from Smithy shape ``com.amazonaws.bedrock#GetModelImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_import_job_identifier


class GetModelImportJobRequest(TypedDict, closed=True):
    job_identifier: (
        "aws_sdk_bedrock.types.model_import_job_identifier.ModelImportJobIdentifier"
    )
    """<p>The identifier of the import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelImportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetModelImportJobRequest:
    out: GetModelImportJobRequest = {}  # type: ignore[typeddict-item]
    return out
