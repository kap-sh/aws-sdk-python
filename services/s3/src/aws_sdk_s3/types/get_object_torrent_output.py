"""Generated from Smithy shape ``com.amazonaws.s3#GetObjectTorrentOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3.types.request_charged
    import aws_sdk_s3.types.streaming_blob


class GetObjectTorrentOutput(TypedDict):
    body: "aws_sdk_s3.types.streaming_blob.StreamingBlob"
    """<p>A Bencoded dictionary as defined by the BitTorrent specification</p>"""
    request_charged: NotRequired["aws_sdk_s3.types.request_charged.RequestCharged"]
