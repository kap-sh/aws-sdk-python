"""Generated from Smithy shape ``com.amazonaws.omics#UploadReadSetPartRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.read_set_part_source
    import aws_sdk_omics.types.read_set_part_streaming_blob
    import aws_sdk_omics.types.sequence_store_id
    import aws_sdk_omics.types.upload_id


class UploadReadSetPartRequest(TypedDict, closed=True):
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The Sequence Store ID used for the multipart upload.</p>"""
    upload_id: "aws_sdk_omics.types.upload_id.UploadId"
    """<p>The ID for the initiated multipart upload.</p>"""
    part_source: "aws_sdk_omics.types.read_set_part_source.ReadSetPartSource"
    """<p>The source file for an upload part.</p>"""
    part_number: "int"
    """<p>The number of the part being uploaded.</p>"""
    payload: "aws_sdk_omics.types.read_set_part_streaming_blob.ReadSetPartStreamingBlob"
    """<p>The read set data to upload for a part.</p>"""
