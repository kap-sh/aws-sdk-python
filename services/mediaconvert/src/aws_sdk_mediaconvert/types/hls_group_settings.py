"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsGroupSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__double_min0_max2147483647
    import aws_sdk_mediaconvert.types.__integer_min0_max3600
    import aws_sdk_mediaconvert.types.__integer_min0_max2147483647
    import aws_sdk_mediaconvert.types.__integer_min1_max2147483647
    import aws_sdk_mediaconvert.types.__integer_min_negative2147483648_max2147483647
    import aws_sdk_mediaconvert.types.__list_of_hls_ad_markers
    import aws_sdk_mediaconvert.types.__list_of_hls_additional_manifest
    import aws_sdk_mediaconvert.types.__list_of_hls_caption_language_mapping
    import aws_sdk_mediaconvert.types.__list_of_hls_image_based_trick_play_variant
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.__string_pattern_s3
    import aws_sdk_mediaconvert.types.destination_settings
    import aws_sdk_mediaconvert.types.hls_audio_only_header
    import aws_sdk_mediaconvert.types.hls_caption_language_setting
    import aws_sdk_mediaconvert.types.hls_caption_segment_length_control
    import aws_sdk_mediaconvert.types.hls_client_cache
    import aws_sdk_mediaconvert.types.hls_codec_specification
    import aws_sdk_mediaconvert.types.hls_directory_structure
    import aws_sdk_mediaconvert.types.hls_encryption_settings
    import aws_sdk_mediaconvert.types.hls_image_based_trick_play
    import aws_sdk_mediaconvert.types.hls_image_based_trick_play_settings
    import aws_sdk_mediaconvert.types.hls_manifest_compression
    import aws_sdk_mediaconvert.types.hls_manifest_duration_format
    import aws_sdk_mediaconvert.types.hls_output_selection
    import aws_sdk_mediaconvert.types.hls_program_date_time
    import aws_sdk_mediaconvert.types.hls_progressive_write_hls_manifest
    import aws_sdk_mediaconvert.types.hls_segment_control
    import aws_sdk_mediaconvert.types.hls_segment_length_control
    import aws_sdk_mediaconvert.types.hls_stream_inf_resolution
    import aws_sdk_mediaconvert.types.hls_target_duration_compatibility_mode
    import aws_sdk_mediaconvert.types.hls_timed_metadata_id3_frame


class HlsGroupSettings(TypedDict):
    ad_markers: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_hls_ad_markers.__listOfHlsAdMarkers"
    ]
    """Choose one or more ad marker types to decorate your Apple HLS manifest. This setting does not determine whether SCTE-35 markers appear in the outputs themselves."""
    additional_manifests: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_hls_additional_manifest.__listOfHlsAdditionalManifest"
    ]
    """By default, the service creates one top-level .m3u8 HLS manifest for each HLS output group in your job. This default manifest references every output in the output group. To create additional top-level manifests that reference a subset of the outputs in the output group, specify a list of them here."""
    audio_only_header: NotRequired[
        "aws_sdk_mediaconvert.types.hls_audio_only_header.HlsAudioOnlyHeader"
    ]
    """Ignore this setting unless you are using FairPlay DRM with Verimatrix and you encounter playback issues. Keep the default value, Include, to output audio-only headers. Choose Exclude to remove the audio-only headers from your audio segments."""
    base_url: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file."""
    caption_language_mappings: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_hls_caption_language_mapping.__listOfHlsCaptionLanguageMapping"
    ]
    """Language to be used on Caption outputs"""
    caption_language_setting: NotRequired[
        "aws_sdk_mediaconvert.types.hls_caption_language_setting.HlsCaptionLanguageSetting"
    ]
    """Applies only to 608 Embedded output captions. Insert: Include CLOSED-CAPTIONS lines in the manifest. Specify at least one language in the CC1 Language Code field. One CLOSED-CAPTION line is added for each Language Code you specify. Make sure to specify the languages in the order in which they appear in the original source (if the source is embedded format) or the order of the caption selectors (if the source is other than embedded). Otherwise, languages in the manifest will not match up properly with the output captions. None: Include CLOSED-CAPTIONS=NONE line in the manifest. Omit: Omit any CLOSED-CAPTIONS line from the manifest."""
    caption_segment_length_control: NotRequired[
        "aws_sdk_mediaconvert.types.hls_caption_segment_length_control.HlsCaptionSegmentLengthControl"
    ]
    """Set Caption segment length control to Match video to create caption segments that align with the video segments from the first video output in this output group. For example, if the video segments are 2 seconds long, your WebVTT segments will also be 2 seconds long. Keep the default setting, Large segments to create caption segments that are 300 seconds long."""
    client_cache: NotRequired[
        "aws_sdk_mediaconvert.types.hls_client_cache.HlsClientCache"
    ]
    """Disable this setting only when your workflow requires the #EXT-X-ALLOW-CACHE:no tag. Otherwise, keep the default value Enabled and control caching in your video distribution set up. For example, use the Cache-Control http header."""
    codec_specification: NotRequired[
        "aws_sdk_mediaconvert.types.hls_codec_specification.HlsCodecSpecification"
    ]
    """Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation."""
    destination: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_s3.__stringPatternS3"
    ]
    """Use Destination to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file."""
    destination_settings: NotRequired[
        "aws_sdk_mediaconvert.types.destination_settings.DestinationSettings"
    ]
    """Settings associated with the destination. Will vary based on the type of destination"""
    directory_structure: NotRequired[
        "aws_sdk_mediaconvert.types.hls_directory_structure.HlsDirectoryStructure"
    ]
    """Indicates whether segments should be placed in subdirectories."""
    encryption: NotRequired[
        "aws_sdk_mediaconvert.types.hls_encryption_settings.HlsEncryptionSettings"
    ]
    """DRM settings."""
    image_based_trick_play: NotRequired[
        "aws_sdk_mediaconvert.types.hls_image_based_trick_play.HlsImageBasedTrickPlay"
    ]
    """Specify whether MediaConvert generates images for trick play. Keep the default value, None, to not generate any images. Choose Thumbnail to generate tiled thumbnails. Choose Thumbnail and full frame to generate tiled thumbnails and full-resolution images of single frames. Choose Advanced to customize thumbnail and tile settings for a single trick play variant. Choose Variants to specify multiple trick play variants, each with its own thumbnail and tile settings. MediaConvert creates a child manifest for each set of images that you generate and adds corresponding entries to the parent manifest. A common application for these images is Roku trick mode. The thumbnails and full-frame images that MediaConvert creates with this feature are compatible with this Roku specification: https://developer.roku.com/docs/developer-program/media-playback/trick-mode/hls-and-dash.md"""
    image_based_trick_play_settings: NotRequired[
        "aws_sdk_mediaconvert.types.hls_image_based_trick_play_settings.HlsImageBasedTrickPlaySettings"
    ]
    """Tile and thumbnail settings applicable when imageBasedTrickPlay is ADVANCED"""
    image_based_trick_play_variants: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_hls_image_based_trick_play_variant.__listOfHlsImageBasedTrickPlayVariant"
    ]
    """Specify multiple image-based trick play variants. Each entry creates a separate set of JPEG tile images with its own resolution, tile layout, and cadence settings. Set imageBasedTrickPlay to VARIANTS when using this setting."""
    manifest_compression: NotRequired[
        "aws_sdk_mediaconvert.types.hls_manifest_compression.HlsManifestCompression"
    ]
    """When set to GZIP, compresses HLS playlist."""
    manifest_duration_format: NotRequired[
        "aws_sdk_mediaconvert.types.hls_manifest_duration_format.HlsManifestDurationFormat"
    ]
    """Indicates whether the output manifest should use floating point values for segment duration."""
    min_final_segment_length: NotRequired[
        "aws_sdk_mediaconvert.types.__double_min0_max2147483647.__doubleMin0Max2147483647"
    ]
    """Keep this setting at the default value of 0, unless you are troubleshooting a problem with how devices play back the end of your video asset. If you know that player devices are hanging on the final segment of your video because the length of your final segment is too short, use this setting to specify a minimum final segment length, in seconds. Choose a value that is greater than or equal to 1 and less than your segment length. When you specify a value for this setting, the encoder will combine any final segment that is shorter than the length that you specify with the previous segment. For example, your segment length is 3 seconds and your final segment is .5 seconds without a minimum final segment length; when you set the minimum final segment length to 1, your final segment is 3.5 seconds."""
    min_segment_length: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """When set, Minimum Segment Size is enforced by looking ahead and back within the specified range for a nearby avail and extending the segment size if needed."""
    output_selection: NotRequired[
        "aws_sdk_mediaconvert.types.hls_output_selection.HlsOutputSelection"
    ]
    """Indicates whether the .m3u8 manifest file should be generated for this HLS output group."""
    program_date_time: NotRequired[
        "aws_sdk_mediaconvert.types.hls_program_date_time.HlsProgramDateTime"
    ]
    """Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is calculated as follows: either the program date and time are initialized using the input timecode source, or the time is initialized using the input timecode source and the date is initialized using the timestamp_offset."""
    program_date_time_period: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max3600.__integerMin0Max3600"
    ]
    """Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds."""
    progressive_write_hls_manifest: NotRequired[
        "aws_sdk_mediaconvert.types.hls_progressive_write_hls_manifest.HlsProgressiveWriteHlsManifest"
    ]
    """Specify whether MediaConvert generates HLS manifests while your job is running or when your job is complete. To generate HLS manifests while your job is running: Choose Enabled. Use if you want to play back your content as soon as it's available. MediaConvert writes the parent and child manifests after the first three media segments are written to your destination S3 bucket. It then writes new updated manifests after each additional segment is written. The parent manifest includes the latest BANDWIDTH and AVERAGE-BANDWIDTH attributes, and child manifests include the latest available media segment. When your job completes, the final child playlists include an EXT-X-ENDLIST tag. To generate HLS manifests only when your job completes: Choose Disabled."""
    segment_control: NotRequired[
        "aws_sdk_mediaconvert.types.hls_segment_control.HlsSegmentControl"
    ]
    """When set to SINGLE_FILE, emits program as a single media resource (.ts) file, uses #EXT-X-BYTERANGE tags to index segment for playback."""
    segment_length: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Specify the length, in whole seconds, of each segment. When you don't specify a value, MediaConvert defaults to 10. Related settings: Use Segment length control to specify whether the encoder enforces this value strictly. Use Segment control to specify whether MediaConvert creates separate segment files or one content file that has metadata to mark the segment boundaries."""
    segment_length_control: NotRequired[
        "aws_sdk_mediaconvert.types.hls_segment_length_control.HlsSegmentLengthControl"
    ]
    """Specify how you want MediaConvert to determine segment lengths in this output group. To use the exact value that you specify under Segment length: Choose Exact. Note that this might result in additional I-frames in the output GOP. To create segment lengths that are a multiple of the GOP: Choose Multiple of GOP. MediaConvert will round up the segment lengths to match the next GOP boundary. To have MediaConvert automatically determine a segment duration that is a multiple of both the audio packets and the frame rates: Choose Match. When you do, also specify a target segment duration under Segment length. This is useful for some ad-insertion or segment replacement workflows. Note that Match has the following requirements: - Output containers: Include at least one video output and at least one audio output. Audio-only outputs are not supported. - Output frame rate: Follow source is not supported. - Multiple output frame rates: When you specify multiple outputs, we recommend they share a similar frame rate (as in X/3, X/2, X, or 2X). For example: 5, 15, 30 and 60. Or: 25 and 50. (Outputs must share an integer multiple.) - Output audio codec: Specify Advanced Audio Coding (AAC). - Output sample rate: Choose 48kHz."""
    segments_per_subdirectory: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Specify the number of segments to write to a subdirectory before starting a new one. You must also set Directory structure to Subdirectory per stream for this setting to have an effect."""
    stream_inf_resolution: NotRequired[
        "aws_sdk_mediaconvert.types.hls_stream_inf_resolution.HlsStreamInfResolution"
    ]
    """Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest."""
    target_duration_compatibility_mode: NotRequired[
        "aws_sdk_mediaconvert.types.hls_target_duration_compatibility_mode.HlsTargetDurationCompatibilityMode"
    ]
    r"""When set to LEGACY, the segment target duration is always rounded up to the nearest integer value above its current value in seconds. When set to SPEC\\_COMPLIANT, the segment target duration is rounded up to the nearest integer value if fraction seconds are greater than or equal to 0.5 (>= 0.5) and rounded down if less than 0.5 (< 0.5). You may need to use LEGACY if your client needs to ensure that the target duration is always longer than the actual duration of the segment. Some older players may experience interrupted playback when the actual duration of a track in a segment is longer than the target duration."""
    timed_metadata_id3_frame: NotRequired[
        "aws_sdk_mediaconvert.types.hls_timed_metadata_id3_frame.HlsTimedMetadataId3Frame"
    ]
    """Specify the type of the ID3 frame to use for ID3 timestamps in your output. To include ID3 timestamps: Specify PRIV or TDRL and set ID3 metadata to Passthrough. To exclude ID3 timestamps: Set ID3 timestamp frame type to None."""
    timed_metadata_id3_period: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative2147483648_max2147483647.__integerMinNegative2147483648Max2147483647"
    ]
    """Specify the interval in seconds to write ID3 timestamps in your output. The first timestamp starts at the output timecode and date, and increases incrementally with each ID3 timestamp. To use the default interval of 10 seconds: Leave blank. To include this metadata in your output: Set ID3 timestamp frame type to PRIV or TDRL, and set ID3 metadata to Passthrough."""
    timestamp_delta_milliseconds: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative2147483648_max2147483647.__integerMinNegative2147483648Max2147483647"
    ]
    """Provides an extra millisecond delta offset to fine tune the timestamps."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsGroupSettings) -> dict:
    out: dict = {}
    if "ad_markers" in value:
        import aws_sdk_mediaconvert.types.__list_of_hls_ad_markers

        out["adMarkers"] = (
            aws_sdk_mediaconvert.types.__list_of_hls_ad_markers.serialize_json(
                value["ad_markers"]
            )
        )
    if "additional_manifests" in value:
        import aws_sdk_mediaconvert.types.__list_of_hls_additional_manifest

        out["additionalManifests"] = (
            aws_sdk_mediaconvert.types.__list_of_hls_additional_manifest.serialize_json(
                value["additional_manifests"]
            )
        )
    if "audio_only_header" in value:
        import aws_sdk_mediaconvert.types.hls_audio_only_header

        out["audioOnlyHeader"] = (
            aws_sdk_mediaconvert.types.hls_audio_only_header.serialize_json(
                value["audio_only_header"]
            )
        )
    if "base_url" in value:
        out["baseUrl"] = value["base_url"]
    if "caption_language_mappings" in value:
        import aws_sdk_mediaconvert.types.__list_of_hls_caption_language_mapping

        out["captionLanguageMappings"] = (
            aws_sdk_mediaconvert.types.__list_of_hls_caption_language_mapping.serialize_json(
                value["caption_language_mappings"]
            )
        )
    if "caption_language_setting" in value:
        import aws_sdk_mediaconvert.types.hls_caption_language_setting

        out["captionLanguageSetting"] = (
            aws_sdk_mediaconvert.types.hls_caption_language_setting.serialize_json(
                value["caption_language_setting"]
            )
        )
    if "caption_segment_length_control" in value:
        import aws_sdk_mediaconvert.types.hls_caption_segment_length_control

        out["captionSegmentLengthControl"] = (
            aws_sdk_mediaconvert.types.hls_caption_segment_length_control.serialize_json(
                value["caption_segment_length_control"]
            )
        )
    if "client_cache" in value:
        import aws_sdk_mediaconvert.types.hls_client_cache

        out["clientCache"] = aws_sdk_mediaconvert.types.hls_client_cache.serialize_json(
            value["client_cache"]
        )
    if "codec_specification" in value:
        import aws_sdk_mediaconvert.types.hls_codec_specification

        out["codecSpecification"] = (
            aws_sdk_mediaconvert.types.hls_codec_specification.serialize_json(
                value["codec_specification"]
            )
        )
    if "destination" in value:
        out["destination"] = value["destination"]
    if "destination_settings" in value:
        import aws_sdk_mediaconvert.types.destination_settings

        out["destinationSettings"] = (
            aws_sdk_mediaconvert.types.destination_settings.serialize_json(
                value["destination_settings"]
            )
        )
    if "directory_structure" in value:
        import aws_sdk_mediaconvert.types.hls_directory_structure

        out["directoryStructure"] = (
            aws_sdk_mediaconvert.types.hls_directory_structure.serialize_json(
                value["directory_structure"]
            )
        )
    if "encryption" in value:
        import aws_sdk_mediaconvert.types.hls_encryption_settings

        out["encryption"] = (
            aws_sdk_mediaconvert.types.hls_encryption_settings.serialize_json(
                value["encryption"]
            )
        )
    if "image_based_trick_play" in value:
        import aws_sdk_mediaconvert.types.hls_image_based_trick_play

        out["imageBasedTrickPlay"] = (
            aws_sdk_mediaconvert.types.hls_image_based_trick_play.serialize_json(
                value["image_based_trick_play"]
            )
        )
    if "image_based_trick_play_settings" in value:
        import aws_sdk_mediaconvert.types.hls_image_based_trick_play_settings

        out["imageBasedTrickPlaySettings"] = (
            aws_sdk_mediaconvert.types.hls_image_based_trick_play_settings.serialize_json(
                value["image_based_trick_play_settings"]
            )
        )
    if "image_based_trick_play_variants" in value:
        import aws_sdk_mediaconvert.types.__list_of_hls_image_based_trick_play_variant

        out["imageBasedTrickPlayVariants"] = (
            aws_sdk_mediaconvert.types.__list_of_hls_image_based_trick_play_variant.serialize_json(
                value["image_based_trick_play_variants"]
            )
        )
    if "manifest_compression" in value:
        import aws_sdk_mediaconvert.types.hls_manifest_compression

        out["manifestCompression"] = (
            aws_sdk_mediaconvert.types.hls_manifest_compression.serialize_json(
                value["manifest_compression"]
            )
        )
    if "manifest_duration_format" in value:
        import aws_sdk_mediaconvert.types.hls_manifest_duration_format

        out["manifestDurationFormat"] = (
            aws_sdk_mediaconvert.types.hls_manifest_duration_format.serialize_json(
                value["manifest_duration_format"]
            )
        )
    if "min_final_segment_length" in value:
        out["minFinalSegmentLength"] = value["min_final_segment_length"]
    if "min_segment_length" in value:
        out["minSegmentLength"] = value["min_segment_length"]
    if "output_selection" in value:
        import aws_sdk_mediaconvert.types.hls_output_selection

        out["outputSelection"] = (
            aws_sdk_mediaconvert.types.hls_output_selection.serialize_json(
                value["output_selection"]
            )
        )
    if "program_date_time" in value:
        import aws_sdk_mediaconvert.types.hls_program_date_time

        out["programDateTime"] = (
            aws_sdk_mediaconvert.types.hls_program_date_time.serialize_json(
                value["program_date_time"]
            )
        )
    if "program_date_time_period" in value:
        out["programDateTimePeriod"] = value["program_date_time_period"]
    if "progressive_write_hls_manifest" in value:
        import aws_sdk_mediaconvert.types.hls_progressive_write_hls_manifest

        out["progressiveWriteHlsManifest"] = (
            aws_sdk_mediaconvert.types.hls_progressive_write_hls_manifest.serialize_json(
                value["progressive_write_hls_manifest"]
            )
        )
    if "segment_control" in value:
        import aws_sdk_mediaconvert.types.hls_segment_control

        out["segmentControl"] = (
            aws_sdk_mediaconvert.types.hls_segment_control.serialize_json(
                value["segment_control"]
            )
        )
    if "segment_length" in value:
        out["segmentLength"] = value["segment_length"]
    if "segment_length_control" in value:
        import aws_sdk_mediaconvert.types.hls_segment_length_control

        out["segmentLengthControl"] = (
            aws_sdk_mediaconvert.types.hls_segment_length_control.serialize_json(
                value["segment_length_control"]
            )
        )
    if "segments_per_subdirectory" in value:
        out["segmentsPerSubdirectory"] = value["segments_per_subdirectory"]
    if "stream_inf_resolution" in value:
        import aws_sdk_mediaconvert.types.hls_stream_inf_resolution

        out["streamInfResolution"] = (
            aws_sdk_mediaconvert.types.hls_stream_inf_resolution.serialize_json(
                value["stream_inf_resolution"]
            )
        )
    if "target_duration_compatibility_mode" in value:
        import aws_sdk_mediaconvert.types.hls_target_duration_compatibility_mode

        out["targetDurationCompatibilityMode"] = (
            aws_sdk_mediaconvert.types.hls_target_duration_compatibility_mode.serialize_json(
                value["target_duration_compatibility_mode"]
            )
        )
    if "timed_metadata_id3_frame" in value:
        import aws_sdk_mediaconvert.types.hls_timed_metadata_id3_frame

        out["timedMetadataId3Frame"] = (
            aws_sdk_mediaconvert.types.hls_timed_metadata_id3_frame.serialize_json(
                value["timed_metadata_id3_frame"]
            )
        )
    if "timed_metadata_id3_period" in value:
        out["timedMetadataId3Period"] = value["timed_metadata_id3_period"]
    if "timestamp_delta_milliseconds" in value:
        out["timestampDeltaMilliseconds"] = value["timestamp_delta_milliseconds"]
    return out


def deserialize_json(data: dict) -> HlsGroupSettings:
    out: HlsGroupSettings = {}  # type: ignore[typeddict-item]
    if "adMarkers" in data:
        import aws_sdk_mediaconvert.types.__list_of_hls_ad_markers

        out["ad_markers"] = (
            aws_sdk_mediaconvert.types.__list_of_hls_ad_markers.deserialize_json(
                data["adMarkers"]
            )
        )
    if "additionalManifests" in data:
        import aws_sdk_mediaconvert.types.__list_of_hls_additional_manifest

        out["additional_manifests"] = (
            aws_sdk_mediaconvert.types.__list_of_hls_additional_manifest.deserialize_json(
                data["additionalManifests"]
            )
        )
    if "audioOnlyHeader" in data:
        import aws_sdk_mediaconvert.types.hls_audio_only_header

        out["audio_only_header"] = (
            aws_sdk_mediaconvert.types.hls_audio_only_header.deserialize_json(
                data["audioOnlyHeader"]
            )
        )
    if "baseUrl" in data:
        out["base_url"] = data["baseUrl"]
    if "captionLanguageMappings" in data:
        import aws_sdk_mediaconvert.types.__list_of_hls_caption_language_mapping

        out["caption_language_mappings"] = (
            aws_sdk_mediaconvert.types.__list_of_hls_caption_language_mapping.deserialize_json(
                data["captionLanguageMappings"]
            )
        )
    if "captionLanguageSetting" in data:
        import aws_sdk_mediaconvert.types.hls_caption_language_setting

        out["caption_language_setting"] = (
            aws_sdk_mediaconvert.types.hls_caption_language_setting.deserialize_json(
                data["captionLanguageSetting"]
            )
        )
    if "captionSegmentLengthControl" in data:
        import aws_sdk_mediaconvert.types.hls_caption_segment_length_control

        out["caption_segment_length_control"] = (
            aws_sdk_mediaconvert.types.hls_caption_segment_length_control.deserialize_json(
                data["captionSegmentLengthControl"]
            )
        )
    if "clientCache" in data:
        import aws_sdk_mediaconvert.types.hls_client_cache

        out["client_cache"] = (
            aws_sdk_mediaconvert.types.hls_client_cache.deserialize_json(
                data["clientCache"]
            )
        )
    if "codecSpecification" in data:
        import aws_sdk_mediaconvert.types.hls_codec_specification

        out["codec_specification"] = (
            aws_sdk_mediaconvert.types.hls_codec_specification.deserialize_json(
                data["codecSpecification"]
            )
        )
    if "destination" in data:
        out["destination"] = data["destination"]
    if "destinationSettings" in data:
        import aws_sdk_mediaconvert.types.destination_settings

        out["destination_settings"] = (
            aws_sdk_mediaconvert.types.destination_settings.deserialize_json(
                data["destinationSettings"]
            )
        )
    if "directoryStructure" in data:
        import aws_sdk_mediaconvert.types.hls_directory_structure

        out["directory_structure"] = (
            aws_sdk_mediaconvert.types.hls_directory_structure.deserialize_json(
                data["directoryStructure"]
            )
        )
    if "encryption" in data:
        import aws_sdk_mediaconvert.types.hls_encryption_settings

        out["encryption"] = (
            aws_sdk_mediaconvert.types.hls_encryption_settings.deserialize_json(
                data["encryption"]
            )
        )
    if "imageBasedTrickPlay" in data:
        import aws_sdk_mediaconvert.types.hls_image_based_trick_play

        out["image_based_trick_play"] = (
            aws_sdk_mediaconvert.types.hls_image_based_trick_play.deserialize_json(
                data["imageBasedTrickPlay"]
            )
        )
    if "imageBasedTrickPlaySettings" in data:
        import aws_sdk_mediaconvert.types.hls_image_based_trick_play_settings

        out["image_based_trick_play_settings"] = (
            aws_sdk_mediaconvert.types.hls_image_based_trick_play_settings.deserialize_json(
                data["imageBasedTrickPlaySettings"]
            )
        )
    if "imageBasedTrickPlayVariants" in data:
        import aws_sdk_mediaconvert.types.__list_of_hls_image_based_trick_play_variant

        out["image_based_trick_play_variants"] = (
            aws_sdk_mediaconvert.types.__list_of_hls_image_based_trick_play_variant.deserialize_json(
                data["imageBasedTrickPlayVariants"]
            )
        )
    if "manifestCompression" in data:
        import aws_sdk_mediaconvert.types.hls_manifest_compression

        out["manifest_compression"] = (
            aws_sdk_mediaconvert.types.hls_manifest_compression.deserialize_json(
                data["manifestCompression"]
            )
        )
    if "manifestDurationFormat" in data:
        import aws_sdk_mediaconvert.types.hls_manifest_duration_format

        out["manifest_duration_format"] = (
            aws_sdk_mediaconvert.types.hls_manifest_duration_format.deserialize_json(
                data["manifestDurationFormat"]
            )
        )
    if "minFinalSegmentLength" in data:
        out["min_final_segment_length"] = data["minFinalSegmentLength"]
    if "minSegmentLength" in data:
        out["min_segment_length"] = data["minSegmentLength"]
    if "outputSelection" in data:
        import aws_sdk_mediaconvert.types.hls_output_selection

        out["output_selection"] = (
            aws_sdk_mediaconvert.types.hls_output_selection.deserialize_json(
                data["outputSelection"]
            )
        )
    if "programDateTime" in data:
        import aws_sdk_mediaconvert.types.hls_program_date_time

        out["program_date_time"] = (
            aws_sdk_mediaconvert.types.hls_program_date_time.deserialize_json(
                data["programDateTime"]
            )
        )
    if "programDateTimePeriod" in data:
        out["program_date_time_period"] = data["programDateTimePeriod"]
    if "progressiveWriteHlsManifest" in data:
        import aws_sdk_mediaconvert.types.hls_progressive_write_hls_manifest

        out["progressive_write_hls_manifest"] = (
            aws_sdk_mediaconvert.types.hls_progressive_write_hls_manifest.deserialize_json(
                data["progressiveWriteHlsManifest"]
            )
        )
    if "segmentControl" in data:
        import aws_sdk_mediaconvert.types.hls_segment_control

        out["segment_control"] = (
            aws_sdk_mediaconvert.types.hls_segment_control.deserialize_json(
                data["segmentControl"]
            )
        )
    if "segmentLength" in data:
        out["segment_length"] = data["segmentLength"]
    if "segmentLengthControl" in data:
        import aws_sdk_mediaconvert.types.hls_segment_length_control

        out["segment_length_control"] = (
            aws_sdk_mediaconvert.types.hls_segment_length_control.deserialize_json(
                data["segmentLengthControl"]
            )
        )
    if "segmentsPerSubdirectory" in data:
        out["segments_per_subdirectory"] = data["segmentsPerSubdirectory"]
    if "streamInfResolution" in data:
        import aws_sdk_mediaconvert.types.hls_stream_inf_resolution

        out["stream_inf_resolution"] = (
            aws_sdk_mediaconvert.types.hls_stream_inf_resolution.deserialize_json(
                data["streamInfResolution"]
            )
        )
    if "targetDurationCompatibilityMode" in data:
        import aws_sdk_mediaconvert.types.hls_target_duration_compatibility_mode

        out["target_duration_compatibility_mode"] = (
            aws_sdk_mediaconvert.types.hls_target_duration_compatibility_mode.deserialize_json(
                data["targetDurationCompatibilityMode"]
            )
        )
    if "timedMetadataId3Frame" in data:
        import aws_sdk_mediaconvert.types.hls_timed_metadata_id3_frame

        out["timed_metadata_id3_frame"] = (
            aws_sdk_mediaconvert.types.hls_timed_metadata_id3_frame.deserialize_json(
                data["timedMetadataId3Frame"]
            )
        )
    if "timedMetadataId3Period" in data:
        out["timed_metadata_id3_period"] = data["timedMetadataId3Period"]
    if "timestampDeltaMilliseconds" in data:
        out["timestamp_delta_milliseconds"] = data["timestampDeltaMilliseconds"]
    return out
