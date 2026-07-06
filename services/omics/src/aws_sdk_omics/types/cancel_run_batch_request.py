"""Generated from Smithy shape ``com.amazonaws.omics#CancelRunBatchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.batch_id


class CancelRunBatchRequest(TypedDict, closed=True):
    batch_id: "aws_sdk_omics.types.batch_id.BatchId"
    """<p>The identifier portion of the run batch ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelRunBatchRequest) -> dict:
    out: dict = {}
    out["batchId"] = value["batch_id"]
    return out


def deserialize_json(data: dict) -> CancelRunBatchRequest:
    out: CancelRunBatchRequest = {}  # type: ignore[typeddict-item]
    if "batchId" in data:
        out["batch_id"] = data["batchId"]
    else:
        raise DeserializationError("CancelRunBatchRequest.batch_id required")
    return out
