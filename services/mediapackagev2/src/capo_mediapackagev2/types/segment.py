"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#Segment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.encryption
    import capo_mediapackagev2.types.scte


class Segment(TypedDict, closed=True):
    segment_duration_seconds: NotRequired["int"]
    """<p>The duration (in seconds) of each segment. Enter a value equal to, or a multiple of, the input segment duration. If the value that you enter is different from the input segment duration, MediaPackage rounds segments to the nearest multiple of the input segment duration.</p>"""
    segment_name: NotRequired["str"]
    """<p>The name that describes the segment. The name is the base name of the segment used in all content manifests inside of the endpoint. You can't use spaces in the name.</p>"""
    ts_use_audio_rendition_group: NotRequired["bool"]
    """<p>When selected, MediaPackage bundles all audio tracks in a rendition group. All other tracks in the stream can be used with any audio rendition from the group.</p>"""
    include_iframe_only_streams: NotRequired["bool"]
    """<p>When selected, the stream set includes an additional I-frame only stream, along with the other tracks. If false, this extra stream is not included. MediaPackage generates an I-frame only stream from the first rendition in the manifest. The service inserts EXT-I-FRAMES-ONLY tags in the output manifest, and then generates and includes an I-frames only playlist in the stream. This playlist permits player functionality like fast forward and rewind.</p>"""
    ts_include_dvb_subtitles: NotRequired["bool"]
    """<p>By default, MediaPackage excludes all digital video broadcasting (DVB) subtitles from the output. When selected, MediaPackage passes through DVB subtitles into the output.</p>"""
    scte: NotRequired["capo_mediapackagev2.types.scte.Scte"]
    """<p>The SCTE configuration options in the segment settings.</p>"""
    encryption: NotRequired["capo_mediapackagev2.types.encryption.Encryption"]


# --- restJson1 ser/de ---
def serialize_json(value: Segment) -> dict:
    out: dict = {}
    if "segment_duration_seconds" in value:
        out["SegmentDurationSeconds"] = value["segment_duration_seconds"]
    if "segment_name" in value:
        out["SegmentName"] = value["segment_name"]
    if "ts_use_audio_rendition_group" in value:
        out["TsUseAudioRenditionGroup"] = value["ts_use_audio_rendition_group"]
    if "include_iframe_only_streams" in value:
        out["IncludeIframeOnlyStreams"] = value["include_iframe_only_streams"]
    if "ts_include_dvb_subtitles" in value:
        out["TsIncludeDvbSubtitles"] = value["ts_include_dvb_subtitles"]
    if "scte" in value:
        import capo_mediapackagev2.types.scte

        out["Scte"] = capo_mediapackagev2.types.scte.serialize_json(value["scte"])
    if "encryption" in value:
        import capo_mediapackagev2.types.encryption

        out["Encryption"] = capo_mediapackagev2.types.encryption.serialize_json(
            value["encryption"]
        )
    return out


def deserialize_json(data: dict) -> Segment:
    out: Segment = {}  # type: ignore[typeddict-item]
    if "SegmentDurationSeconds" in data:
        out["segment_duration_seconds"] = data["SegmentDurationSeconds"]
    if "SegmentName" in data:
        out["segment_name"] = data["SegmentName"]
    if "TsUseAudioRenditionGroup" in data:
        out["ts_use_audio_rendition_group"] = data["TsUseAudioRenditionGroup"]
    if "IncludeIframeOnlyStreams" in data:
        out["include_iframe_only_streams"] = data["IncludeIframeOnlyStreams"]
    if "TsIncludeDvbSubtitles" in data:
        out["ts_include_dvb_subtitles"] = data["TsIncludeDvbSubtitles"]
    if "Scte" in data:
        import capo_mediapackagev2.types.scte

        out["scte"] = capo_mediapackagev2.types.scte.deserialize_json(data["Scte"])
    if "Encryption" in data:
        import capo_mediapackagev2.types.encryption

        out["encryption"] = capo_mediapackagev2.types.encryption.deserialize_json(
            data["Encryption"]
        )
    return out
