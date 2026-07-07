"""Generated from Smithy shape ``com.amazonaws.wisdom#GetImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.uuid
    import aws_sdk_wisdom.types.uuid_or_arn


class GetImportJobRequest(TypedDict, closed=True):
    import_job_id: "aws_sdk_wisdom.types.uuid.Uuid"
    """<p>The identifier of the import job to retrieve.</p>"""
    knowledge_base_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base that the import job belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImportJobRequest:
    out: GetImportJobRequest = {}  # type: ignore[typeddict-item]
    return out
