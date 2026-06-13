"""Generated from Smithy shape ``com.amazonaws.omics#GetReadSetActivationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.activation_job_id
    import aws_sdk_omics.types.sequence_store_id


class GetReadSetActivationJobRequest(TypedDict):
    id: "aws_sdk_omics.types.activation_job_id.ActivationJobId"
    """<p>The job's ID.</p>"""
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The job's sequence store ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReadSetActivationJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReadSetActivationJobRequest:
    out: GetReadSetActivationJobRequest = {}  # type: ignore[typeddict-item]
    return out
