"""Generated from Smithy shape ``com.amazonaws.omics#ListMultipartReadSetUploadsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.next_token
    import aws_sdk_omics.types.sequence_store_id


class ListMultipartReadSetUploadsRequest(TypedDict, closed=True):
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The Sequence Store ID used for the multipart uploads.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of multipart uploads returned in a page.</p>"""
    next_token: NotRequired["aws_sdk_omics.types.next_token.NextToken"]
    """<p>Next token returned in the response of a previous ListMultipartReadSetUploads call. Used to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMultipartReadSetUploadsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMultipartReadSetUploadsRequest:
    out: ListMultipartReadSetUploadsRequest = {}  # type: ignore[typeddict-item]
    return out
