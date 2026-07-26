"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#CmafPackage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__boolean
    import capo_mediapackage_vod.types.__integer
    import capo_mediapackage_vod.types.__list_of_hls_manifest
    import capo_mediapackage_vod.types.cmaf_encryption


class CmafPackage(TypedDict, closed=True):
    encryption: NotRequired[
        "capo_mediapackage_vod.types.cmaf_encryption.CmafEncryption"
    ]
    hls_manifests: NotRequired[
        "capo_mediapackage_vod.types.__list_of_hls_manifest.__listOfHlsManifest"
    ]
    """A list of HLS manifest configurations."""
    include_encoder_configuration_in_segments: NotRequired[
        "capo_mediapackage_vod.types.__boolean.__boolean"
    ]
    """When includeEncoderConfigurationInSegments is set to true, MediaPackage places your encoder's Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) metadata in every video segment instead of in the init fragment. This lets you use different SPS/PPS/VPS settings for your assets during content playback."""
    segment_duration_seconds: NotRequired[
        "capo_mediapackage_vod.types.__integer.__integer"
    ]
    """Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration."""


# --- restJson1 ser/de ---
def serialize_json(value: CmafPackage) -> dict:
    out: dict = {}
    if "encryption" in value:
        import capo_mediapackage_vod.types.cmaf_encryption

        out["encryption"] = capo_mediapackage_vod.types.cmaf_encryption.serialize_json(
            value["encryption"]
        )
    if "hls_manifests" in value:
        import capo_mediapackage_vod.types.__list_of_hls_manifest

        out["hlsManifests"] = (
            capo_mediapackage_vod.types.__list_of_hls_manifest.serialize_json(
                value["hls_manifests"]
            )
        )
    if "include_encoder_configuration_in_segments" in value:
        out["includeEncoderConfigurationInSegments"] = value[
            "include_encoder_configuration_in_segments"
        ]
    if "segment_duration_seconds" in value:
        out["segmentDurationSeconds"] = value["segment_duration_seconds"]
    return out


def deserialize_json(data: dict) -> CmafPackage:
    out: CmafPackage = {}  # type: ignore[typeddict-item]
    if "encryption" in data:
        import capo_mediapackage_vod.types.cmaf_encryption

        out["encryption"] = (
            capo_mediapackage_vod.types.cmaf_encryption.deserialize_json(
                data["encryption"]
            )
        )
    if "hlsManifests" in data:
        import capo_mediapackage_vod.types.__list_of_hls_manifest

        out["hls_manifests"] = (
            capo_mediapackage_vod.types.__list_of_hls_manifest.deserialize_json(
                data["hlsManifests"]
            )
        )
    if "includeEncoderConfigurationInSegments" in data:
        out["include_encoder_configuration_in_segments"] = data[
            "includeEncoderConfigurationInSegments"
        ]
    if "segmentDurationSeconds" in data:
        out["segment_duration_seconds"] = data["segmentDurationSeconds"]
    return out
