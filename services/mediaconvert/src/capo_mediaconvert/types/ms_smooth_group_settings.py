"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MsSmoothGroupSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min1_max2147483647
    import capo_mediaconvert.types.__list_of_ms_smooth_additional_manifest
    import capo_mediaconvert.types.__string_pattern_s3
    import capo_mediaconvert.types.destination_settings
    import capo_mediaconvert.types.ms_smooth_audio_deduplication
    import capo_mediaconvert.types.ms_smooth_encryption_settings
    import capo_mediaconvert.types.ms_smooth_fragment_length_control
    import capo_mediaconvert.types.ms_smooth_manifest_encoding


class MsSmoothGroupSettings(TypedDict, closed=True):
    additional_manifests: NotRequired[
        "capo_mediaconvert.types.__list_of_ms_smooth_additional_manifest.__listOfMsSmoothAdditionalManifest"
    ]
    """By default, the service creates one .ism Microsoft Smooth Streaming manifest for each Microsoft Smooth Streaming output group in your job. This default manifest references every output in the output group. To create additional manifests that reference a subset of the outputs in the output group, specify a list of them here."""
    audio_deduplication: NotRequired[
        "capo_mediaconvert.types.ms_smooth_audio_deduplication.MsSmoothAudioDeduplication"
    ]
    """COMBINE_DUPLICATE_STREAMS combines identical audio encoding settings across a Microsoft Smooth output group into a single audio stream."""
    destination: NotRequired[
        "capo_mediaconvert.types.__string_pattern_s3.__stringPatternS3"
    ]
    """Use Destination to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file."""
    destination_settings: NotRequired[
        "capo_mediaconvert.types.destination_settings.DestinationSettings"
    ]
    """Settings associated with the destination. Will vary based on the type of destination"""
    encryption: NotRequired[
        "capo_mediaconvert.types.ms_smooth_encryption_settings.MsSmoothEncryptionSettings"
    ]
    """If you are using DRM, set DRM System to specify the value SpekeKeyProvider."""
    fragment_length: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Specify how you want MediaConvert to determine the fragment length. Choose Exact to have the encoder use the exact length that you specify with the setting Fragment length. This might result in extra I-frames. Choose Multiple of GOP to have the encoder round up the segment lengths to match the next GOP boundary."""
    fragment_length_control: NotRequired[
        "capo_mediaconvert.types.ms_smooth_fragment_length_control.MsSmoothFragmentLengthControl"
    ]
    """Specify how you want MediaConvert to determine the fragment length. Choose Exact to have the encoder use the exact length that you specify with the setting Fragment length. This might result in extra I-frames. Choose Multiple of GOP to have the encoder round up the segment lengths to match the next GOP boundary."""
    manifest_encoding: NotRequired[
        "capo_mediaconvert.types.ms_smooth_manifest_encoding.MsSmoothManifestEncoding"
    ]
    """Use Manifest encoding to specify the encoding format for the server and client manifest. Valid options are utf8 and utf16."""


# --- restJson1 ser/de ---
def serialize_json(value: MsSmoothGroupSettings) -> dict:
    out: dict = {}
    if "additional_manifests" in value:
        import capo_mediaconvert.types.__list_of_ms_smooth_additional_manifest

        out["additionalManifests"] = (
            capo_mediaconvert.types.__list_of_ms_smooth_additional_manifest.serialize_json(
                value["additional_manifests"]
            )
        )
    if "audio_deduplication" in value:
        import capo_mediaconvert.types.ms_smooth_audio_deduplication

        out["audioDeduplication"] = (
            capo_mediaconvert.types.ms_smooth_audio_deduplication.serialize_json(
                value["audio_deduplication"]
            )
        )
    if "destination" in value:
        out["destination"] = value["destination"]
    if "destination_settings" in value:
        import capo_mediaconvert.types.destination_settings

        out["destinationSettings"] = (
            capo_mediaconvert.types.destination_settings.serialize_json(
                value["destination_settings"]
            )
        )
    if "encryption" in value:
        import capo_mediaconvert.types.ms_smooth_encryption_settings

        out["encryption"] = (
            capo_mediaconvert.types.ms_smooth_encryption_settings.serialize_json(
                value["encryption"]
            )
        )
    if "fragment_length" in value:
        out["fragmentLength"] = value["fragment_length"]
    if "fragment_length_control" in value:
        import capo_mediaconvert.types.ms_smooth_fragment_length_control

        out["fragmentLengthControl"] = (
            capo_mediaconvert.types.ms_smooth_fragment_length_control.serialize_json(
                value["fragment_length_control"]
            )
        )
    if "manifest_encoding" in value:
        import capo_mediaconvert.types.ms_smooth_manifest_encoding

        out["manifestEncoding"] = (
            capo_mediaconvert.types.ms_smooth_manifest_encoding.serialize_json(
                value["manifest_encoding"]
            )
        )
    return out


def deserialize_json(data: dict) -> MsSmoothGroupSettings:
    out: MsSmoothGroupSettings = {}  # type: ignore[typeddict-item]
    if "additionalManifests" in data:
        import capo_mediaconvert.types.__list_of_ms_smooth_additional_manifest

        out["additional_manifests"] = (
            capo_mediaconvert.types.__list_of_ms_smooth_additional_manifest.deserialize_json(
                data["additionalManifests"]
            )
        )
    if "audioDeduplication" in data:
        import capo_mediaconvert.types.ms_smooth_audio_deduplication

        out["audio_deduplication"] = (
            capo_mediaconvert.types.ms_smooth_audio_deduplication.deserialize_json(
                data["audioDeduplication"]
            )
        )
    if "destination" in data:
        out["destination"] = data["destination"]
    if "destinationSettings" in data:
        import capo_mediaconvert.types.destination_settings

        out["destination_settings"] = (
            capo_mediaconvert.types.destination_settings.deserialize_json(
                data["destinationSettings"]
            )
        )
    if "encryption" in data:
        import capo_mediaconvert.types.ms_smooth_encryption_settings

        out["encryption"] = (
            capo_mediaconvert.types.ms_smooth_encryption_settings.deserialize_json(
                data["encryption"]
            )
        )
    if "fragmentLength" in data:
        out["fragment_length"] = data["fragmentLength"]
    if "fragmentLengthControl" in data:
        import capo_mediaconvert.types.ms_smooth_fragment_length_control

        out["fragment_length_control"] = (
            capo_mediaconvert.types.ms_smooth_fragment_length_control.deserialize_json(
                data["fragmentLengthControl"]
            )
        )
    if "manifestEncoding" in data:
        import capo_mediaconvert.types.ms_smooth_manifest_encoding

        out["manifest_encoding"] = (
            capo_mediaconvert.types.ms_smooth_manifest_encoding.deserialize_json(
                data["manifestEncoding"]
            )
        )
    return out
