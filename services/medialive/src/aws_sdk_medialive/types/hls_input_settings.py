"""Generated from Smithy shape ``com.amazonaws.medialive#HlsInputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min0
    import aws_sdk_medialive.types.hls_scte35_source_type


class HlsInputSettings(TypedDict, closed=True):
    bandwidth: NotRequired["aws_sdk_medialive.types.__integer_min0.__integerMin0"]
    """When specified the HLS stream with the m3u8 BANDWIDTH that most closely matches this value will be chosen, otherwise the highest bandwidth stream in the m3u8 will be chosen. The bitrate is specified in bits per second, as in an HLS manifest."""
    buffer_segments: NotRequired["aws_sdk_medialive.types.__integer_min0.__integerMin0"]
    """When specified, reading of the HLS input will begin this many buffer segments from the end (most recently written segment). When not specified, the HLS input will begin with the first segment specified in the m3u8."""
    retries: NotRequired["aws_sdk_medialive.types.__integer_min0.__integerMin0"]
    """The number of consecutive times that attempts to read a manifest or segment must fail before the input is considered unavailable."""
    retry_interval: NotRequired["aws_sdk_medialive.types.__integer_min0.__integerMin0"]
    """The number of seconds between retries when an attempt to read a manifest or segment fails."""
    scte35_source: NotRequired[
        "aws_sdk_medialive.types.hls_scte35_source_type.HlsScte35SourceType"
    ]
    """Identifies the source for the SCTE-35 messages that MediaLive will ingest. Messages can be ingested from the content segments (in the stream) or from tags in the playlist (the HLS manifest). MediaLive ignores SCTE-35 information in the source that is not selected."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsInputSettings) -> dict:
    out: dict = {}
    if "bandwidth" in value:
        out["bandwidth"] = value["bandwidth"]
    if "buffer_segments" in value:
        out["bufferSegments"] = value["buffer_segments"]
    if "retries" in value:
        out["retries"] = value["retries"]
    if "retry_interval" in value:
        out["retryInterval"] = value["retry_interval"]
    if "scte35_source" in value:
        import aws_sdk_medialive.types.hls_scte35_source_type

        out["scte35Source"] = (
            aws_sdk_medialive.types.hls_scte35_source_type.serialize_json(
                value["scte35_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> HlsInputSettings:
    out: HlsInputSettings = {}  # type: ignore[typeddict-item]
    if "bandwidth" in data:
        out["bandwidth"] = data["bandwidth"]
    if "bufferSegments" in data:
        out["buffer_segments"] = data["bufferSegments"]
    if "retries" in data:
        out["retries"] = data["retries"]
    if "retryInterval" in data:
        out["retry_interval"] = data["retryInterval"]
    if "scte35Source" in data:
        import aws_sdk_medialive.types.hls_scte35_source_type

        out["scte35_source"] = (
            aws_sdk_medialive.types.hls_scte35_source_type.deserialize_json(
                data["scte35Source"]
            )
        )
    return out
