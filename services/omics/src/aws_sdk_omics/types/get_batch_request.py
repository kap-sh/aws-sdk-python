"""Generated from Smithy shape ``com.amazonaws.omics#GetBatchRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.batch_id


class GetBatchRequest(TypedDict):
    batch_id: "aws_sdk_omics.types.batch_id.BatchId"
    """<p>The identifier portion of the run batch ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBatchRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBatchRequest:
    out: GetBatchRequest = {}  # type: ignore[typeddict-item]
    return out
