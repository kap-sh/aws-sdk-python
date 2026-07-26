"""Generated from Smithy shape ``com.amazonaws.s3#GetObjectTorrentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3.types.request_charged
    import capo_s3.types.streaming_blob


class GetObjectTorrentOutput(TypedDict, closed=True):
    body: "capo_s3.types.streaming_blob.StreamingBlob"
    """<p>A Bencoded dictionary as defined by the BitTorrent specification</p>"""
    request_charged: NotRequired["capo_s3.types.request_charged.RequestCharged"]
