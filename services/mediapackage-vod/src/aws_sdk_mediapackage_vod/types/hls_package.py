"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#HlsPackage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__boolean
    import aws_sdk_mediapackage_vod.types.__integer
    import aws_sdk_mediapackage_vod.types.__list_of_hls_manifest
    import aws_sdk_mediapackage_vod.types.hls_encryption


class HlsPackage(TypedDict):
    encryption: NotRequired[
        "aws_sdk_mediapackage_vod.types.hls_encryption.HlsEncryption"
    ]
    hls_manifests: NotRequired[
        "aws_sdk_mediapackage_vod.types.__list_of_hls_manifest.__listOfHlsManifest"
    ]
    """A list of HLS manifest configurations."""
    include_dvb_subtitles: NotRequired[
        "aws_sdk_mediapackage_vod.types.__boolean.__boolean"
    ]
    """When enabled, MediaPackage passes through digital video broadcasting (DVB) subtitles into the output."""
    segment_duration_seconds: NotRequired[
        "aws_sdk_mediapackage_vod.types.__integer.__integer"
    ]
    """Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration."""
    use_audio_rendition_group: NotRequired[
        "aws_sdk_mediapackage_vod.types.__boolean.__boolean"
    ]
    """When enabled, audio streams will be placed in rendition groups in the output."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsPackage) -> dict:
    out: dict = {}
    if "encryption" in value:
        import aws_sdk_mediapackage_vod.types.hls_encryption

        out["encryption"] = (
            aws_sdk_mediapackage_vod.types.hls_encryption.serialize_json(
                value["encryption"]
            )
        )
    if "hls_manifests" in value:
        import aws_sdk_mediapackage_vod.types.__list_of_hls_manifest

        out["hlsManifests"] = (
            aws_sdk_mediapackage_vod.types.__list_of_hls_manifest.serialize_json(
                value["hls_manifests"]
            )
        )
    if "include_dvb_subtitles" in value:
        out["includeDvbSubtitles"] = value["include_dvb_subtitles"]
    if "segment_duration_seconds" in value:
        out["segmentDurationSeconds"] = value["segment_duration_seconds"]
    if "use_audio_rendition_group" in value:
        out["useAudioRenditionGroup"] = value["use_audio_rendition_group"]
    return out


def deserialize_json(data: dict) -> HlsPackage:
    out: HlsPackage = {}  # type: ignore[typeddict-item]
    if "encryption" in data:
        import aws_sdk_mediapackage_vod.types.hls_encryption

        out["encryption"] = (
            aws_sdk_mediapackage_vod.types.hls_encryption.deserialize_json(
                data["encryption"]
            )
        )
    if "hlsManifests" in data:
        import aws_sdk_mediapackage_vod.types.__list_of_hls_manifest

        out["hls_manifests"] = (
            aws_sdk_mediapackage_vod.types.__list_of_hls_manifest.deserialize_json(
                data["hlsManifests"]
            )
        )
    if "includeDvbSubtitles" in data:
        out["include_dvb_subtitles"] = data["includeDvbSubtitles"]
    if "segmentDurationSeconds" in data:
        out["segment_duration_seconds"] = data["segmentDurationSeconds"]
    if "useAudioRenditionGroup" in data:
        out["use_audio_rendition_group"] = data["useAudioRenditionGroup"]
    return out
