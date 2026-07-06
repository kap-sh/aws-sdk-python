"""Generated from Smithy shape ``com.amazonaws.omics#AbortMultipartReadSetUploadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.sequence_store_id
    import aws_sdk_omics.types.upload_id


class AbortMultipartReadSetUploadRequest(TypedDict, closed=True):
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The sequence store ID for the store involved in the multipart upload.</p>"""
    upload_id: "aws_sdk_omics.types.upload_id.UploadId"
    """<p>The ID for the multipart upload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AbortMultipartReadSetUploadRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AbortMultipartReadSetUploadRequest:
    out: AbortMultipartReadSetUploadRequest = {}  # type: ignore[typeddict-item]
    return out
