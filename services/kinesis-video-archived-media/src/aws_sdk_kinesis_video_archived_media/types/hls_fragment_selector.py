"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#HLSFragmentSelector``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.hls_fragment_selector_type
    import aws_sdk_kinesis_video_archived_media.types.hls_timestamp_range


class HLSFragmentSelector(TypedDict):
    fragment_selector_type: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.hls_fragment_selector_type.HLSFragmentSelectorType"
    ]
    """<p>The source of the timestamps for the requested media.</p> <p>When <code>FragmentSelectorType</code> is set to <code>PRODUCER_TIMESTAMP</code> and <a>GetHLSStreamingSessionURLInput$PlaybackMode</a> is <code>ON_DEMAND</code> or <code>LIVE_REPLAY</code>, the first fragment ingested with a producer timestamp within the specified <a>FragmentSelector$TimestampRange</a> is included in the media playlist. In addition, the fragments with producer timestamps within the <code>TimestampRange</code> ingested immediately following the first fragment (up to the <a>GetHLSStreamingSessionURLInput$MaxMediaPlaylistFragmentResults</a> value) are included. </p> <p>Fragments that have duplicate producer timestamps are deduplicated. This means that if producers are producing a stream of fragments with producer timestamps that are approximately equal to the true clock time, the HLS media playlists will contain all of the fragments within the requested timestamp range. If some fragments are ingested within the same time range and very different points in time, only the oldest ingested collection of fragments are returned.</p> <p>When <code>FragmentSelectorType</code> is set to <code>PRODUCER_TIMESTAMP</code> and <a>GetHLSStreamingSessionURLInput$PlaybackMode</a> is <code>LIVE</code>, the producer timestamps are used in the MP4 fragments and for deduplication. But the most recently ingested fragments based on server timestamps are included in the HLS media playlist. This means that even if fragments ingested in the past have producer timestamps with values now, they are not included in the HLS media playlist.</p> <p>The default is <code>SERVER_TIMESTAMP</code>.</p>"""
    timestamp_range: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.hls_timestamp_range.HLSTimestampRange"
    ]
    """<p>The start and end of the timestamp range for the requested media.</p> <p>This value should not be present if <code>PlaybackType</code> is <code>LIVE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HLSFragmentSelector) -> dict:
    out: dict = {}
    if "fragment_selector_type" in value:
        import aws_sdk_kinesis_video_archived_media.types.hls_fragment_selector_type

        out["FragmentSelectorType"] = (
            aws_sdk_kinesis_video_archived_media.types.hls_fragment_selector_type.serialize_json(
                value["fragment_selector_type"]
            )
        )
    if "timestamp_range" in value:
        import aws_sdk_kinesis_video_archived_media.types.hls_timestamp_range

        out["TimestampRange"] = (
            aws_sdk_kinesis_video_archived_media.types.hls_timestamp_range.serialize_json(
                value["timestamp_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> HLSFragmentSelector:
    out: HLSFragmentSelector = {}  # type: ignore[typeddict-item]
    if "FragmentSelectorType" in data:
        import aws_sdk_kinesis_video_archived_media.types.hls_fragment_selector_type

        out["fragment_selector_type"] = (
            aws_sdk_kinesis_video_archived_media.types.hls_fragment_selector_type.deserialize_json(
                data["FragmentSelectorType"]
            )
        )
    if "TimestampRange" in data:
        import aws_sdk_kinesis_video_archived_media.types.hls_timestamp_range

        out["timestamp_range"] = (
            aws_sdk_kinesis_video_archived_media.types.hls_timestamp_range.deserialize_json(
                data["TimestampRange"]
            )
        )
    return out
