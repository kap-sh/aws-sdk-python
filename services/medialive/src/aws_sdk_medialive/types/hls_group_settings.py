"""Generated from Smithy shape ``com.amazonaws.medialive#HlsGroupSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min0
    import aws_sdk_medialive.types.__integer_min0_max3600
    import aws_sdk_medialive.types.__integer_min1
    import aws_sdk_medialive.types.__integer_min3
    import aws_sdk_medialive.types.__list_of_caption_language_mapping
    import aws_sdk_medialive.types.__list_of_hls_ad_markers
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.__string_min32_max32
    import aws_sdk_medialive.types.hls_caption_language_setting
    import aws_sdk_medialive.types.hls_cdn_settings
    import aws_sdk_medialive.types.hls_client_cache
    import aws_sdk_medialive.types.hls_codec_specification
    import aws_sdk_medialive.types.hls_directory_structure
    import aws_sdk_medialive.types.hls_discontinuity_tags
    import aws_sdk_medialive.types.hls_encryption_type
    import aws_sdk_medialive.types.hls_id3_segment_tagging_state
    import aws_sdk_medialive.types.hls_incomplete_segment_behavior
    import aws_sdk_medialive.types.hls_iv_in_manifest
    import aws_sdk_medialive.types.hls_iv_source
    import aws_sdk_medialive.types.hls_manifest_compression
    import aws_sdk_medialive.types.hls_manifest_duration_format
    import aws_sdk_medialive.types.hls_mode
    import aws_sdk_medialive.types.hls_output_selection
    import aws_sdk_medialive.types.hls_program_date_time
    import aws_sdk_medialive.types.hls_program_date_time_clock
    import aws_sdk_medialive.types.hls_redundant_manifest
    import aws_sdk_medialive.types.hls_segmentation_mode
    import aws_sdk_medialive.types.hls_stream_inf_resolution
    import aws_sdk_medialive.types.hls_timed_metadata_id3_frame
    import aws_sdk_medialive.types.hls_ts_file_mode
    import aws_sdk_medialive.types.i_frame_only_playlist_type
    import aws_sdk_medialive.types.input_loss_action_for_hls_out
    import aws_sdk_medialive.types.key_provider_settings
    import aws_sdk_medialive.types.output_location_ref


class HlsGroupSettings(TypedDict):
    ad_markers: NotRequired[
        "aws_sdk_medialive.types.__list_of_hls_ad_markers.__listOfHlsAdMarkers"
    ]
    """Choose one or more ad marker types to pass SCTE35 signals through to this group of Apple HLS outputs."""
    base_url_content: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file."""
    base_url_content1: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Optional. One value per output group. This field is required only if you are completing Base URL content A, and the downstream system has notified you that the media files for pipeline 1 of all outputs are in a location different from the media files for pipeline 0."""
    base_url_manifest: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file."""
    base_url_manifest1: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Optional. One value per output group. Complete this field only if you are completing Base URL manifest A, and the downstream system has notified you that the child manifest files for pipeline 1 of all outputs are in a location different from the child manifest files for pipeline 0."""
    caption_language_mappings: NotRequired[
        "aws_sdk_medialive.types.__list_of_caption_language_mapping.__listOfCaptionLanguageMapping"
    ]
    r"""Mapping of up to 4 caption channels to caption languages. Is only meaningful if captionLanguageSetting is set to \"insert\"."""
    caption_language_setting: NotRequired[
        "aws_sdk_medialive.types.hls_caption_language_setting.HlsCaptionLanguageSetting"
    ]
    """Applies only to 608 Embedded output captions. insert: Include CLOSED-CAPTIONS lines in the manifest. Specify at least one language in the CC1 Language Code field. One CLOSED-CAPTION line is added for each Language Code you specify. Make sure to specify the languages in the order in which they appear in the original source (if the source is embedded format) or the order of the caption selectors (if the source is other than embedded). Otherwise, languages in the manifest will not match up properly with the output captions. none: Include CLOSED-CAPTIONS=NONE line in the manifest. omit: Omit any CLOSED-CAPTIONS line from the manifest."""
    client_cache: NotRequired["aws_sdk_medialive.types.hls_client_cache.HlsClientCache"]
    r"""When set to \"disabled\", sets the #EXT-X-ALLOW-CACHE:no tag in the manifest, which prevents clients from saving media segments for later replay."""
    codec_specification: NotRequired[
        "aws_sdk_medialive.types.hls_codec_specification.HlsCodecSpecification"
    ]
    """Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation."""
    constant_iv: NotRequired[
        "aws_sdk_medialive.types.__string_min32_max32.__stringMin32Max32"
    ]
    r"""For use with encryptionType. This is a 128-bit, 16-byte hex value represented by a 32-character text string. If ivSource is set to \"explicit\" then this parameter is required and is used as the IV for encryption."""
    destination: NotRequired[
        "aws_sdk_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """A directory or HTTP destination for the HLS segments, manifest files, and encryption keys (if enabled)."""
    directory_structure: NotRequired[
        "aws_sdk_medialive.types.hls_directory_structure.HlsDirectoryStructure"
    ]
    """Place segments in subdirectories."""
    discontinuity_tags: NotRequired[
        "aws_sdk_medialive.types.hls_discontinuity_tags.HlsDiscontinuityTags"
    ]
    """Specifies whether to insert EXT-X-DISCONTINUITY tags in the HLS child manifests for this output group. Typically, choose Insert because these tags are required in the manifest (according to the HLS specification) and serve an important purpose. Choose Never Insert only if the downstream system is doing real-time failover (without using the MediaLive automatic failover feature) and only if that downstream system has advised you to exclude the tags."""
    encryption_type: NotRequired[
        "aws_sdk_medialive.types.hls_encryption_type.HlsEncryptionType"
    ]
    """Encrypts the segments with the given encryption scheme. Exclude this parameter if no encryption is desired."""
    hls_cdn_settings: NotRequired[
        "aws_sdk_medialive.types.hls_cdn_settings.HlsCdnSettings"
    ]
    """Parameters that control interactions with the CDN."""
    hls_id3_segment_tagging: NotRequired[
        "aws_sdk_medialive.types.hls_id3_segment_tagging_state.HlsId3SegmentTaggingState"
    ]
    """State of HLS ID3 Segment Tagging"""
    i_frame_only_playlists: NotRequired[
        "aws_sdk_medialive.types.i_frame_only_playlist_type.IFrameOnlyPlaylistType"
    ]
    r"""DISABLED: Do not create an I-frame-only manifest, but do create the master and media manifests (according to the Output Selection field). STANDARD: Create an I-frame-only manifest for each output that contains video, as well as the other manifests (according to the Output Selection field). The I-frame manifest contains a #EXT-X-I-FRAMES-ONLY tag to indicate it is I-frame only, and one or more #EXT-X-BYTERANGE entries identifying the I-frame position. For example, #EXT-X-BYTERANGE:160364@1461888\""""
    incomplete_segment_behavior: NotRequired[
        "aws_sdk_medialive.types.hls_incomplete_segment_behavior.HlsIncompleteSegmentBehavior"
    ]
    """Specifies whether to include the final (incomplete) segment in the media output when the pipeline stops producing output because of a channel stop, a channel pause or a loss of input to the pipeline. Auto means that MediaLive decides whether to include the final segment, depending on the channel class and the types of output groups. Suppress means to never include the incomplete segment. We recommend you choose Auto and let MediaLive control the behavior."""
    index_n_segments: NotRequired[
        "aws_sdk_medialive.types.__integer_min3.__integerMin3"
    ]
    """Applies only if Mode field is LIVE. Specifies the maximum number of segments in the media manifest file. After this maximum, older segments are removed from the media manifest. This number must be smaller than the number in the Keep Segments field."""
    input_loss_action: NotRequired[
        "aws_sdk_medialive.types.input_loss_action_for_hls_out.InputLossActionForHlsOut"
    ]
    """Parameter that control output group behavior on input loss."""
    iv_in_manifest: NotRequired[
        "aws_sdk_medialive.types.hls_iv_in_manifest.HlsIvInManifest"
    ]
    r"""For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If set to \"include\", IV is listed in the manifest, otherwise the IV is not in the manifest."""
    iv_source: NotRequired["aws_sdk_medialive.types.hls_iv_source.HlsIvSource"]
    r"""For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If this setting is \"followsSegmentNumber\", it will cause the IV to change every segment (to match the segment number). If this is set to \"explicit\", you must enter a constantIv value."""
    keep_segments: NotRequired["aws_sdk_medialive.types.__integer_min1.__integerMin1"]
    r"""Applies only if Mode field is LIVE. Specifies the number of media segments to retain in the destination directory. This number should be bigger than indexNSegments (Num segments). We recommend (value = (2 x indexNsegments) + 1). If this \"keep segments\" number is too low, the following might happen: the player is still reading a media manifest file that lists this segment, but that segment has been removed from the destination directory (as directed by indexNSegments). This situation would result in a 404 HTTP error on the player."""
    key_format: NotRequired["aws_sdk_medialive.types.__string.__string"]
    r"""The value specifies how the key is represented in the resource identified by the URI. If parameter is absent, an implicit value of \"identity\" is used. A reverse DNS string can also be given."""
    key_format_versions: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Either a single positive integer version value or a slash delimited list of version values (1/2/3)."""
    key_provider_settings: NotRequired[
        "aws_sdk_medialive.types.key_provider_settings.KeyProviderSettings"
    ]
    """The key provider settings."""
    manifest_compression: NotRequired[
        "aws_sdk_medialive.types.hls_manifest_compression.HlsManifestCompression"
    ]
    """When set to gzip, compresses HLS playlist."""
    manifest_duration_format: NotRequired[
        "aws_sdk_medialive.types.hls_manifest_duration_format.HlsManifestDurationFormat"
    ]
    """Indicates whether the output manifest should use floating point or integer values for segment duration."""
    min_segment_length: NotRequired[
        "aws_sdk_medialive.types.__integer_min0.__integerMin0"
    ]
    """Minimum length of MPEG-2 Transport Stream segments in seconds. When set, minimum segment length is enforced by looking ahead and back within the specified range for a nearby avail and extending the segment size if needed."""
    mode: NotRequired["aws_sdk_medialive.types.hls_mode.HlsMode"]
    r"""If \"vod\", all segments are indexed and kept permanently in the destination and manifest. If \"live\", only the number segments specified in keepSegments and indexNSegments are kept; newer segments replace older segments, which may prevent players from rewinding all the way to the beginning of the event. VOD mode uses HLS EXT-X-PLAYLIST-TYPE of EVENT while the channel is running, converting it to a \"VOD\" type manifest on completion of the stream."""
    output_selection: NotRequired[
        "aws_sdk_medialive.types.hls_output_selection.HlsOutputSelection"
    ]
    """MANIFESTS_AND_SEGMENTS: Generates manifests (master manifest, if applicable, and media manifests) for this output group. VARIANT_MANIFESTS_AND_SEGMENTS: Generates media manifests for this output group, but not a master manifest. SEGMENTS_ONLY: Does not generate any manifests for this output group."""
    program_date_time: NotRequired[
        "aws_sdk_medialive.types.hls_program_date_time.HlsProgramDateTime"
    ]
    """Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is calculated using the program date time clock."""
    program_date_time_clock: NotRequired[
        "aws_sdk_medialive.types.hls_program_date_time_clock.HlsProgramDateTimeClock"
    ]
    """Specifies the algorithm used to drive the HLS EXT-X-PROGRAM-DATE-TIME clock. Options include: INITIALIZE_FROM_OUTPUT_TIMECODE: The PDT clock is initialized as a function of the first output timecode, then incremented by the EXTINF duration of each encoded segment. SYSTEM_CLOCK: The PDT clock is initialized as a function of the UTC wall clock, then incremented by the EXTINF duration of each encoded segment. If the PDT clock diverges from the wall clock by more than 500ms, it is resynchronized to the wall clock."""
    program_date_time_period: NotRequired[
        "aws_sdk_medialive.types.__integer_min0_max3600.__integerMin0Max3600"
    ]
    """Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds."""
    redundant_manifest: NotRequired[
        "aws_sdk_medialive.types.hls_redundant_manifest.HlsRedundantManifest"
    ]
    """ENABLED: The master manifest (.m3u8 file) for each pipeline includes information about both pipelines: first its own media files, then the media files of the other pipeline. This feature allows playout device that support stale manifest detection to switch from one manifest to the other, when the current manifest seems to be stale. There are still two destinations and two master manifests, but both master manifests reference the media files from both pipelines. DISABLED: The master manifest (.m3u8 file) for each pipeline includes information about its own pipeline only. For an HLS output group with MediaPackage as the destination, the DISABLED behavior is always followed. MediaPackage regenerates the manifests it serves to players so a redundant manifest from MediaLive is irrelevant."""
    segment_length: NotRequired["aws_sdk_medialive.types.__integer_min1.__integerMin1"]
    """Length of MPEG-2 Transport Stream segments to create in seconds. Note that segments will end on the next keyframe after this duration, so actual segment length may be longer."""
    segmentation_mode: NotRequired[
        "aws_sdk_medialive.types.hls_segmentation_mode.HlsSegmentationMode"
    ]
    """useInputSegmentation has been deprecated. The configured segment size is always used."""
    segments_per_subdirectory: NotRequired[
        "aws_sdk_medialive.types.__integer_min1.__integerMin1"
    ]
    """Number of segments to write to a subdirectory before starting a new one. directoryStructure must be subdirectoryPerStream for this setting to have an effect."""
    stream_inf_resolution: NotRequired[
        "aws_sdk_medialive.types.hls_stream_inf_resolution.HlsStreamInfResolution"
    ]
    """Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest."""
    timed_metadata_id3_frame: NotRequired[
        "aws_sdk_medialive.types.hls_timed_metadata_id3_frame.HlsTimedMetadataId3Frame"
    ]
    """Indicates ID3 frame that has the timecode."""
    timed_metadata_id3_period: NotRequired[
        "aws_sdk_medialive.types.__integer_min0.__integerMin0"
    ]
    """Timed Metadata interval in seconds."""
    timestamp_delta_milliseconds: NotRequired[
        "aws_sdk_medialive.types.__integer_min0.__integerMin0"
    ]
    """Provides an extra millisecond delta offset to fine tune the timestamps."""
    ts_file_mode: NotRequired["aws_sdk_medialive.types.hls_ts_file_mode.HlsTsFileMode"]
    """SEGMENTED_FILES: Emit the program as segments - multiple .ts media files. SINGLE_FILE: Applies only if Mode field is VOD. Emit the program as a single .ts media file. The media manifest includes #EXT-X-BYTERANGE tags to index segments for playback. A typical use for this value is when sending the output to AWS Elemental MediaConvert, which can accept only a single media file. Playback while the channel is running is not guaranteed due to HTTP server caching."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsGroupSettings) -> dict:
    out: dict = {}
    if "ad_markers" in value:
        import aws_sdk_medialive.types.__list_of_hls_ad_markers

        out["adMarkers"] = (
            aws_sdk_medialive.types.__list_of_hls_ad_markers.serialize_json(
                value["ad_markers"]
            )
        )
    if "base_url_content" in value:
        out["baseUrlContent"] = value["base_url_content"]
    if "base_url_content1" in value:
        out["baseUrlContent1"] = value["base_url_content1"]
    if "base_url_manifest" in value:
        out["baseUrlManifest"] = value["base_url_manifest"]
    if "base_url_manifest1" in value:
        out["baseUrlManifest1"] = value["base_url_manifest1"]
    if "caption_language_mappings" in value:
        import aws_sdk_medialive.types.__list_of_caption_language_mapping

        out["captionLanguageMappings"] = (
            aws_sdk_medialive.types.__list_of_caption_language_mapping.serialize_json(
                value["caption_language_mappings"]
            )
        )
    if "caption_language_setting" in value:
        import aws_sdk_medialive.types.hls_caption_language_setting

        out["captionLanguageSetting"] = (
            aws_sdk_medialive.types.hls_caption_language_setting.serialize_json(
                value["caption_language_setting"]
            )
        )
    if "client_cache" in value:
        import aws_sdk_medialive.types.hls_client_cache

        out["clientCache"] = aws_sdk_medialive.types.hls_client_cache.serialize_json(
            value["client_cache"]
        )
    if "codec_specification" in value:
        import aws_sdk_medialive.types.hls_codec_specification

        out["codecSpecification"] = (
            aws_sdk_medialive.types.hls_codec_specification.serialize_json(
                value["codec_specification"]
            )
        )
    if "constant_iv" in value:
        out["constantIv"] = value["constant_iv"]
    if "destination" in value:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = aws_sdk_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    if "directory_structure" in value:
        import aws_sdk_medialive.types.hls_directory_structure

        out["directoryStructure"] = (
            aws_sdk_medialive.types.hls_directory_structure.serialize_json(
                value["directory_structure"]
            )
        )
    if "discontinuity_tags" in value:
        import aws_sdk_medialive.types.hls_discontinuity_tags

        out["discontinuityTags"] = (
            aws_sdk_medialive.types.hls_discontinuity_tags.serialize_json(
                value["discontinuity_tags"]
            )
        )
    if "encryption_type" in value:
        import aws_sdk_medialive.types.hls_encryption_type

        out["encryptionType"] = (
            aws_sdk_medialive.types.hls_encryption_type.serialize_json(
                value["encryption_type"]
            )
        )
    if "hls_cdn_settings" in value:
        import aws_sdk_medialive.types.hls_cdn_settings

        out["hlsCdnSettings"] = aws_sdk_medialive.types.hls_cdn_settings.serialize_json(
            value["hls_cdn_settings"]
        )
    if "hls_id3_segment_tagging" in value:
        import aws_sdk_medialive.types.hls_id3_segment_tagging_state

        out["hlsId3SegmentTagging"] = (
            aws_sdk_medialive.types.hls_id3_segment_tagging_state.serialize_json(
                value["hls_id3_segment_tagging"]
            )
        )
    if "i_frame_only_playlists" in value:
        import aws_sdk_medialive.types.i_frame_only_playlist_type

        out["iFrameOnlyPlaylists"] = (
            aws_sdk_medialive.types.i_frame_only_playlist_type.serialize_json(
                value["i_frame_only_playlists"]
            )
        )
    if "incomplete_segment_behavior" in value:
        import aws_sdk_medialive.types.hls_incomplete_segment_behavior

        out["incompleteSegmentBehavior"] = (
            aws_sdk_medialive.types.hls_incomplete_segment_behavior.serialize_json(
                value["incomplete_segment_behavior"]
            )
        )
    if "index_n_segments" in value:
        out["indexNSegments"] = value["index_n_segments"]
    if "input_loss_action" in value:
        import aws_sdk_medialive.types.input_loss_action_for_hls_out

        out["inputLossAction"] = (
            aws_sdk_medialive.types.input_loss_action_for_hls_out.serialize_json(
                value["input_loss_action"]
            )
        )
    if "iv_in_manifest" in value:
        import aws_sdk_medialive.types.hls_iv_in_manifest

        out["ivInManifest"] = aws_sdk_medialive.types.hls_iv_in_manifest.serialize_json(
            value["iv_in_manifest"]
        )
    if "iv_source" in value:
        import aws_sdk_medialive.types.hls_iv_source

        out["ivSource"] = aws_sdk_medialive.types.hls_iv_source.serialize_json(
            value["iv_source"]
        )
    if "keep_segments" in value:
        out["keepSegments"] = value["keep_segments"]
    if "key_format" in value:
        out["keyFormat"] = value["key_format"]
    if "key_format_versions" in value:
        out["keyFormatVersions"] = value["key_format_versions"]
    if "key_provider_settings" in value:
        import aws_sdk_medialive.types.key_provider_settings

        out["keyProviderSettings"] = (
            aws_sdk_medialive.types.key_provider_settings.serialize_json(
                value["key_provider_settings"]
            )
        )
    if "manifest_compression" in value:
        import aws_sdk_medialive.types.hls_manifest_compression

        out["manifestCompression"] = (
            aws_sdk_medialive.types.hls_manifest_compression.serialize_json(
                value["manifest_compression"]
            )
        )
    if "manifest_duration_format" in value:
        import aws_sdk_medialive.types.hls_manifest_duration_format

        out["manifestDurationFormat"] = (
            aws_sdk_medialive.types.hls_manifest_duration_format.serialize_json(
                value["manifest_duration_format"]
            )
        )
    if "min_segment_length" in value:
        out["minSegmentLength"] = value["min_segment_length"]
    if "mode" in value:
        import aws_sdk_medialive.types.hls_mode

        out["mode"] = aws_sdk_medialive.types.hls_mode.serialize_json(value["mode"])
    if "output_selection" in value:
        import aws_sdk_medialive.types.hls_output_selection

        out["outputSelection"] = (
            aws_sdk_medialive.types.hls_output_selection.serialize_json(
                value["output_selection"]
            )
        )
    if "program_date_time" in value:
        import aws_sdk_medialive.types.hls_program_date_time

        out["programDateTime"] = (
            aws_sdk_medialive.types.hls_program_date_time.serialize_json(
                value["program_date_time"]
            )
        )
    if "program_date_time_clock" in value:
        import aws_sdk_medialive.types.hls_program_date_time_clock

        out["programDateTimeClock"] = (
            aws_sdk_medialive.types.hls_program_date_time_clock.serialize_json(
                value["program_date_time_clock"]
            )
        )
    if "program_date_time_period" in value:
        out["programDateTimePeriod"] = value["program_date_time_period"]
    if "redundant_manifest" in value:
        import aws_sdk_medialive.types.hls_redundant_manifest

        out["redundantManifest"] = (
            aws_sdk_medialive.types.hls_redundant_manifest.serialize_json(
                value["redundant_manifest"]
            )
        )
    if "segment_length" in value:
        out["segmentLength"] = value["segment_length"]
    if "segmentation_mode" in value:
        import aws_sdk_medialive.types.hls_segmentation_mode

        out["segmentationMode"] = (
            aws_sdk_medialive.types.hls_segmentation_mode.serialize_json(
                value["segmentation_mode"]
            )
        )
    if "segments_per_subdirectory" in value:
        out["segmentsPerSubdirectory"] = value["segments_per_subdirectory"]
    if "stream_inf_resolution" in value:
        import aws_sdk_medialive.types.hls_stream_inf_resolution

        out["streamInfResolution"] = (
            aws_sdk_medialive.types.hls_stream_inf_resolution.serialize_json(
                value["stream_inf_resolution"]
            )
        )
    if "timed_metadata_id3_frame" in value:
        import aws_sdk_medialive.types.hls_timed_metadata_id3_frame

        out["timedMetadataId3Frame"] = (
            aws_sdk_medialive.types.hls_timed_metadata_id3_frame.serialize_json(
                value["timed_metadata_id3_frame"]
            )
        )
    if "timed_metadata_id3_period" in value:
        out["timedMetadataId3Period"] = value["timed_metadata_id3_period"]
    if "timestamp_delta_milliseconds" in value:
        out["timestampDeltaMilliseconds"] = value["timestamp_delta_milliseconds"]
    if "ts_file_mode" in value:
        import aws_sdk_medialive.types.hls_ts_file_mode

        out["tsFileMode"] = aws_sdk_medialive.types.hls_ts_file_mode.serialize_json(
            value["ts_file_mode"]
        )
    return out


def deserialize_json(data: dict) -> HlsGroupSettings:
    out: HlsGroupSettings = {}  # type: ignore[typeddict-item]
    if "adMarkers" in data:
        import aws_sdk_medialive.types.__list_of_hls_ad_markers

        out["ad_markers"] = (
            aws_sdk_medialive.types.__list_of_hls_ad_markers.deserialize_json(
                data["adMarkers"]
            )
        )
    if "baseUrlContent" in data:
        out["base_url_content"] = data["baseUrlContent"]
    if "baseUrlContent1" in data:
        out["base_url_content1"] = data["baseUrlContent1"]
    if "baseUrlManifest" in data:
        out["base_url_manifest"] = data["baseUrlManifest"]
    if "baseUrlManifest1" in data:
        out["base_url_manifest1"] = data["baseUrlManifest1"]
    if "captionLanguageMappings" in data:
        import aws_sdk_medialive.types.__list_of_caption_language_mapping

        out["caption_language_mappings"] = (
            aws_sdk_medialive.types.__list_of_caption_language_mapping.deserialize_json(
                data["captionLanguageMappings"]
            )
        )
    if "captionLanguageSetting" in data:
        import aws_sdk_medialive.types.hls_caption_language_setting

        out["caption_language_setting"] = (
            aws_sdk_medialive.types.hls_caption_language_setting.deserialize_json(
                data["captionLanguageSetting"]
            )
        )
    if "clientCache" in data:
        import aws_sdk_medialive.types.hls_client_cache

        out["client_cache"] = aws_sdk_medialive.types.hls_client_cache.deserialize_json(
            data["clientCache"]
        )
    if "codecSpecification" in data:
        import aws_sdk_medialive.types.hls_codec_specification

        out["codec_specification"] = (
            aws_sdk_medialive.types.hls_codec_specification.deserialize_json(
                data["codecSpecification"]
            )
        )
    if "constantIv" in data:
        out["constant_iv"] = data["constantIv"]
    if "destination" in data:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = (
            aws_sdk_medialive.types.output_location_ref.deserialize_json(
                data["destination"]
            )
        )
    if "directoryStructure" in data:
        import aws_sdk_medialive.types.hls_directory_structure

        out["directory_structure"] = (
            aws_sdk_medialive.types.hls_directory_structure.deserialize_json(
                data["directoryStructure"]
            )
        )
    if "discontinuityTags" in data:
        import aws_sdk_medialive.types.hls_discontinuity_tags

        out["discontinuity_tags"] = (
            aws_sdk_medialive.types.hls_discontinuity_tags.deserialize_json(
                data["discontinuityTags"]
            )
        )
    if "encryptionType" in data:
        import aws_sdk_medialive.types.hls_encryption_type

        out["encryption_type"] = (
            aws_sdk_medialive.types.hls_encryption_type.deserialize_json(
                data["encryptionType"]
            )
        )
    if "hlsCdnSettings" in data:
        import aws_sdk_medialive.types.hls_cdn_settings

        out["hls_cdn_settings"] = (
            aws_sdk_medialive.types.hls_cdn_settings.deserialize_json(
                data["hlsCdnSettings"]
            )
        )
    if "hlsId3SegmentTagging" in data:
        import aws_sdk_medialive.types.hls_id3_segment_tagging_state

        out["hls_id3_segment_tagging"] = (
            aws_sdk_medialive.types.hls_id3_segment_tagging_state.deserialize_json(
                data["hlsId3SegmentTagging"]
            )
        )
    if "iFrameOnlyPlaylists" in data:
        import aws_sdk_medialive.types.i_frame_only_playlist_type

        out["i_frame_only_playlists"] = (
            aws_sdk_medialive.types.i_frame_only_playlist_type.deserialize_json(
                data["iFrameOnlyPlaylists"]
            )
        )
    if "incompleteSegmentBehavior" in data:
        import aws_sdk_medialive.types.hls_incomplete_segment_behavior

        out["incomplete_segment_behavior"] = (
            aws_sdk_medialive.types.hls_incomplete_segment_behavior.deserialize_json(
                data["incompleteSegmentBehavior"]
            )
        )
    if "indexNSegments" in data:
        out["index_n_segments"] = data["indexNSegments"]
    if "inputLossAction" in data:
        import aws_sdk_medialive.types.input_loss_action_for_hls_out

        out["input_loss_action"] = (
            aws_sdk_medialive.types.input_loss_action_for_hls_out.deserialize_json(
                data["inputLossAction"]
            )
        )
    if "ivInManifest" in data:
        import aws_sdk_medialive.types.hls_iv_in_manifest

        out["iv_in_manifest"] = (
            aws_sdk_medialive.types.hls_iv_in_manifest.deserialize_json(
                data["ivInManifest"]
            )
        )
    if "ivSource" in data:
        import aws_sdk_medialive.types.hls_iv_source

        out["iv_source"] = aws_sdk_medialive.types.hls_iv_source.deserialize_json(
            data["ivSource"]
        )
    if "keepSegments" in data:
        out["keep_segments"] = data["keepSegments"]
    if "keyFormat" in data:
        out["key_format"] = data["keyFormat"]
    if "keyFormatVersions" in data:
        out["key_format_versions"] = data["keyFormatVersions"]
    if "keyProviderSettings" in data:
        import aws_sdk_medialive.types.key_provider_settings

        out["key_provider_settings"] = (
            aws_sdk_medialive.types.key_provider_settings.deserialize_json(
                data["keyProviderSettings"]
            )
        )
    if "manifestCompression" in data:
        import aws_sdk_medialive.types.hls_manifest_compression

        out["manifest_compression"] = (
            aws_sdk_medialive.types.hls_manifest_compression.deserialize_json(
                data["manifestCompression"]
            )
        )
    if "manifestDurationFormat" in data:
        import aws_sdk_medialive.types.hls_manifest_duration_format

        out["manifest_duration_format"] = (
            aws_sdk_medialive.types.hls_manifest_duration_format.deserialize_json(
                data["manifestDurationFormat"]
            )
        )
    if "minSegmentLength" in data:
        out["min_segment_length"] = data["minSegmentLength"]
    if "mode" in data:
        import aws_sdk_medialive.types.hls_mode

        out["mode"] = aws_sdk_medialive.types.hls_mode.deserialize_json(data["mode"])
    if "outputSelection" in data:
        import aws_sdk_medialive.types.hls_output_selection

        out["output_selection"] = (
            aws_sdk_medialive.types.hls_output_selection.deserialize_json(
                data["outputSelection"]
            )
        )
    if "programDateTime" in data:
        import aws_sdk_medialive.types.hls_program_date_time

        out["program_date_time"] = (
            aws_sdk_medialive.types.hls_program_date_time.deserialize_json(
                data["programDateTime"]
            )
        )
    if "programDateTimeClock" in data:
        import aws_sdk_medialive.types.hls_program_date_time_clock

        out["program_date_time_clock"] = (
            aws_sdk_medialive.types.hls_program_date_time_clock.deserialize_json(
                data["programDateTimeClock"]
            )
        )
    if "programDateTimePeriod" in data:
        out["program_date_time_period"] = data["programDateTimePeriod"]
    if "redundantManifest" in data:
        import aws_sdk_medialive.types.hls_redundant_manifest

        out["redundant_manifest"] = (
            aws_sdk_medialive.types.hls_redundant_manifest.deserialize_json(
                data["redundantManifest"]
            )
        )
    if "segmentLength" in data:
        out["segment_length"] = data["segmentLength"]
    if "segmentationMode" in data:
        import aws_sdk_medialive.types.hls_segmentation_mode

        out["segmentation_mode"] = (
            aws_sdk_medialive.types.hls_segmentation_mode.deserialize_json(
                data["segmentationMode"]
            )
        )
    if "segmentsPerSubdirectory" in data:
        out["segments_per_subdirectory"] = data["segmentsPerSubdirectory"]
    if "streamInfResolution" in data:
        import aws_sdk_medialive.types.hls_stream_inf_resolution

        out["stream_inf_resolution"] = (
            aws_sdk_medialive.types.hls_stream_inf_resolution.deserialize_json(
                data["streamInfResolution"]
            )
        )
    if "timedMetadataId3Frame" in data:
        import aws_sdk_medialive.types.hls_timed_metadata_id3_frame

        out["timed_metadata_id3_frame"] = (
            aws_sdk_medialive.types.hls_timed_metadata_id3_frame.deserialize_json(
                data["timedMetadataId3Frame"]
            )
        )
    if "timedMetadataId3Period" in data:
        out["timed_metadata_id3_period"] = data["timedMetadataId3Period"]
    if "timestampDeltaMilliseconds" in data:
        out["timestamp_delta_milliseconds"] = data["timestampDeltaMilliseconds"]
    if "tsFileMode" in data:
        import aws_sdk_medialive.types.hls_ts_file_mode

        out["ts_file_mode"] = aws_sdk_medialive.types.hls_ts_file_mode.deserialize_json(
            data["tsFileMode"]
        )
    return out
