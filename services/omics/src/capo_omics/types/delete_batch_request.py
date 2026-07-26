"""Generated from Smithy shape ``com.amazonaws.omics#DeleteBatchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.batch_id


class DeleteBatchRequest(TypedDict, closed=True):
    batch_id: "capo_omics.types.batch_id.BatchId"
    """<p>The identifier portion of the run batch ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBatchRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBatchRequest:
    out: DeleteBatchRequest = {}  # type: ignore[typeddict-item]
    return out
