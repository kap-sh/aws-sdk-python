"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CancelMetadataTransferJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.id


class CancelMetadataTransferJobRequest(TypedDict, closed=True):
    metadata_transfer_job_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The metadata transfer job Id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelMetadataTransferJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelMetadataTransferJobRequest:
    out: CancelMetadataTransferJobRequest = {}  # type: ignore[typeddict-item]
    return out
