"""Generated from Smithy shape ``com.amazonaws.qconnect#DeleteImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.uuid
    import aws_sdk_qconnect.types.uuid_or_arn


class DeleteImportJobRequest(TypedDict, closed=True):
    knowledge_base_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base.</p>"""
    import_job_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the import job to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteImportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteImportJobRequest:
    out: DeleteImportJobRequest = {}  # type: ignore[typeddict-item]
    return out
