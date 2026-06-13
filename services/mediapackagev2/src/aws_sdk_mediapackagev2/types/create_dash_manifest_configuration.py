"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CreateDashManifestConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.dash_audio_timeline_pattern
    import aws_sdk_mediapackagev2.types.dash_availability_start_time_configuration
    import aws_sdk_mediapackagev2.types.dash_base_urls
    import aws_sdk_mediapackagev2.types.dash_compactness
    import aws_sdk_mediapackagev2.types.dash_drm_signaling
    import aws_sdk_mediapackagev2.types.dash_dvb_settings
    import aws_sdk_mediapackagev2.types.dash_period_triggers
    import aws_sdk_mediapackagev2.types.dash_profiles
    import aws_sdk_mediapackagev2.types.dash_program_information
    import aws_sdk_mediapackagev2.types.dash_segment_template_format
    import aws_sdk_mediapackagev2.types.dash_subtitle_configuration
    import aws_sdk_mediapackagev2.types.dash_utc_timing
    import aws_sdk_mediapackagev2.types.filter_configuration
    import aws_sdk_mediapackagev2.types.manifest_name
    import aws_sdk_mediapackagev2.types.scte_dash
    import aws_sdk_mediapackagev2.types.uri_path_type


class CreateDashManifestConfiguration(TypedDict):
    manifest_name: "aws_sdk_mediapackagev2.types.manifest_name.ManifestName"
    """<p>A short string that's appended to the endpoint URL. The child manifest name creates a unique path to this endpoint.</p>"""
    manifest_window_seconds: NotRequired["int"]
    """<p>The total duration (in seconds) of the manifest's content.</p>"""
    filter_configuration: NotRequired[
        "aws_sdk_mediapackagev2.types.filter_configuration.FilterConfiguration"
    ]
    min_update_period_seconds: NotRequired["int"]
    """<p>Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest.</p>"""
    min_buffer_time_seconds: NotRequired["int"]
    """<p>Minimum amount of content (in seconds) that a player must keep available in the buffer.</p>"""
    suggested_presentation_delay_seconds: NotRequired["int"]
    """<p>The amount of time (in seconds) that the player should be from the end of the manifest.</p>"""
    segment_template_format: NotRequired[
        "aws_sdk_mediapackagev2.types.dash_segment_template_format.DashSegmentTemplateFormat"
    ]
    """<p>Determines the type of variable used in the <code>media</code> URL of the <code>SegmentTemplate</code> tag in the manifest. Also specifies if segment timeline information is included in <code>SegmentTimeline</code> or <code>SegmentTemplate</code>.</p> <p>Value description:</p> <ul> <li> <p> <code>NUMBER_WITH_TIMELINE</code> - The <code>$Number$</code> variable is used in the <code>media</code> URL. The value of this variable is the sequential number of the segment. A full <code>SegmentTimeline</code> object is presented in each <code>SegmentTemplate</code>.</p> </li> </ul>"""
    period_triggers: NotRequired[
        "aws_sdk_mediapackagev2.types.dash_period_triggers.DashPeriodTriggers"
    ]
    """<p>A list of triggers that controls when AWS Elemental MediaPackage separates the MPEG-DASH manifest into multiple periods. Type <code>ADS</code> to indicate that AWS Elemental MediaPackage must create periods in the output manifest that correspond to SCTE-35 ad markers in the input source. Leave this value empty to indicate that the manifest is contained all in one period. For more information about periods in the DASH manifest, see <a href=\"https://docs.aws.amazon.com/mediapackage/latest/userguide/multi-period.html\">Multi-period DASH in AWS Elemental MediaPackage</a>.</p>"""
    scte_dash: NotRequired["aws_sdk_mediapackagev2.types.scte_dash.ScteDash"]
    """<p>The SCTE configuration.</p>"""
    drm_signaling: NotRequired[
        "aws_sdk_mediapackagev2.types.dash_drm_signaling.DashDrmSignaling"
    ]
    """<p>Determines how the DASH manifest signals the DRM content.</p>"""
    utc_timing: NotRequired[
        "aws_sdk_mediapackagev2.types.dash_utc_timing.DashUtcTiming"
    ]
    """<p>Determines the type of UTC timing included in the DASH Media Presentation Description (MPD).</p>"""
    profiles: NotRequired["aws_sdk_mediapackagev2.types.dash_profiles.DashProfiles"]
    """<p>The profile that the output is compliant with.</p>"""
    base_urls: NotRequired["aws_sdk_mediapackagev2.types.dash_base_urls.DashBaseUrls"]
    """<p>The base URLs to use for retrieving segments.</p>"""
    program_information: NotRequired[
        "aws_sdk_mediapackagev2.types.dash_program_information.DashProgramInformation"
    ]
    """<p>Details about the content that you want MediaPackage to pass through in the manifest to the playback device.</p>"""
    dvb_settings: NotRequired[
        "aws_sdk_mediapackagev2.types.dash_dvb_settings.DashDvbSettings"
    ]
    """<p>For endpoints that use the DVB-DASH profile only. The font download and error reporting information that you want MediaPackage to pass through to the manifest.</p>"""
    compactness: NotRequired[
        "aws_sdk_mediapackagev2.types.dash_compactness.DashCompactness"
    ]
    """<p>The layout of the DASH manifest that MediaPackage produces. <code>STANDARD</code> indicates a default manifest, which is compacted. <code>NONE</code> indicates a full manifest.</p> <p>For information about compactness, see <a href=\"https://docs.aws.amazon.com/mediapackage/latest/userguide/compacted.html\">DASH manifest compactness</a> in the <i>Elemental MediaPackage v2 User Guide</i>.</p>"""
    audio_timeline_pattern: NotRequired[
        "aws_sdk_mediapackagev2.types.dash_audio_timeline_pattern.DashAudioTimelinePattern"
    ]
    """<p>How MediaPackage represents the audio timeline in the DASH manifest. This setting applies DASH Segment Duration Patternization, as defined in the MPEG-DASH specification, to audio adaptation sets. When set to <code>PATTERNED</code>, MediaPackage uses a pattern-based segment template for audio, which reduces manifest size by expressing repeating segment durations as a pattern instead of listing each segment individually. When set to <code>NONE</code>, the manifest contains an explicit timeline that lists each audio segment.</p> <p>Valid values: <code>NONE</code> | <code>PATTERNED</code> </p> <p>For information about audio timeline patterns, see <a href=\"https://docs.aws.amazon.com/mediapackage/latest/userguide/dash-audio-timeline-pattern.html\">DASH audio timeline pattern</a> in the <i>Elemental MediaPackage v2 User Guide</i>.</p>"""
    subtitle_configuration: NotRequired[
        "aws_sdk_mediapackagev2.types.dash_subtitle_configuration.DashSubtitleConfiguration"
    ]
    """<p>The configuration for DASH subtitles.</p>"""
    uri_path_type: NotRequired["aws_sdk_mediapackagev2.types.uri_path_type.UriPathType"]
    """<p>The type of path to use in manifest URIs. <code>LEAF</code> uses leaf-relative paths (for example, <code>index_1.mpd</code>). <code>ROOT</code> uses root-relative paths that include the full path from root (for example, <code>/out/v1/channel-group/channel/endpoint/index_1.mpd</code>). If you don't specify a value, the default is <code>LEAF</code>.</p>"""
    availability_start_time_configuration: NotRequired[
        "aws_sdk_mediapackagev2.types.dash_availability_start_time_configuration.DashAvailabilityStartTimeConfiguration"
    ]
    """<p>The configuration for the DASH <code>availabilityStartTime</code> attribute of the Media Presentation Description (MPD). If you don't specify a value, MediaPackage uses the default availability start time of <code>2024-01-01T00:00:00Z</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDashManifestConfiguration) -> dict:
    out: dict = {}
    out["ManifestName"] = value["manifest_name"]
    if "manifest_window_seconds" in value:
        out["ManifestWindowSeconds"] = value["manifest_window_seconds"]
    if "filter_configuration" in value:
        import aws_sdk_mediapackagev2.types.filter_configuration

        out["FilterConfiguration"] = (
            aws_sdk_mediapackagev2.types.filter_configuration.serialize_json(
                value["filter_configuration"]
            )
        )
    if "min_update_period_seconds" in value:
        out["MinUpdatePeriodSeconds"] = value["min_update_period_seconds"]
    if "min_buffer_time_seconds" in value:
        out["MinBufferTimeSeconds"] = value["min_buffer_time_seconds"]
    if "suggested_presentation_delay_seconds" in value:
        out["SuggestedPresentationDelaySeconds"] = value[
            "suggested_presentation_delay_seconds"
        ]
    if "segment_template_format" in value:
        import aws_sdk_mediapackagev2.types.dash_segment_template_format

        out["SegmentTemplateFormat"] = (
            aws_sdk_mediapackagev2.types.dash_segment_template_format.serialize_json(
                value["segment_template_format"]
            )
        )
    if "period_triggers" in value:
        import aws_sdk_mediapackagev2.types.dash_period_triggers

        out["PeriodTriggers"] = (
            aws_sdk_mediapackagev2.types.dash_period_triggers.serialize_json(
                value["period_triggers"]
            )
        )
    if "scte_dash" in value:
        import aws_sdk_mediapackagev2.types.scte_dash

        out["ScteDash"] = aws_sdk_mediapackagev2.types.scte_dash.serialize_json(
            value["scte_dash"]
        )
    if "drm_signaling" in value:
        import aws_sdk_mediapackagev2.types.dash_drm_signaling

        out["DrmSignaling"] = (
            aws_sdk_mediapackagev2.types.dash_drm_signaling.serialize_json(
                value["drm_signaling"]
            )
        )
    if "utc_timing" in value:
        import aws_sdk_mediapackagev2.types.dash_utc_timing

        out["UtcTiming"] = aws_sdk_mediapackagev2.types.dash_utc_timing.serialize_json(
            value["utc_timing"]
        )
    if "profiles" in value:
        import aws_sdk_mediapackagev2.types.dash_profiles

        out["Profiles"] = aws_sdk_mediapackagev2.types.dash_profiles.serialize_json(
            value["profiles"]
        )
    if "base_urls" in value:
        import aws_sdk_mediapackagev2.types.dash_base_urls

        out["BaseUrls"] = aws_sdk_mediapackagev2.types.dash_base_urls.serialize_json(
            value["base_urls"]
        )
    if "program_information" in value:
        import aws_sdk_mediapackagev2.types.dash_program_information

        out["ProgramInformation"] = (
            aws_sdk_mediapackagev2.types.dash_program_information.serialize_json(
                value["program_information"]
            )
        )
    if "dvb_settings" in value:
        import aws_sdk_mediapackagev2.types.dash_dvb_settings

        out["DvbSettings"] = (
            aws_sdk_mediapackagev2.types.dash_dvb_settings.serialize_json(
                value["dvb_settings"]
            )
        )
    if "compactness" in value:
        import aws_sdk_mediapackagev2.types.dash_compactness

        out["Compactness"] = (
            aws_sdk_mediapackagev2.types.dash_compactness.serialize_json(
                value["compactness"]
            )
        )
    if "audio_timeline_pattern" in value:
        import aws_sdk_mediapackagev2.types.dash_audio_timeline_pattern

        out["AudioTimelinePattern"] = (
            aws_sdk_mediapackagev2.types.dash_audio_timeline_pattern.serialize_json(
                value["audio_timeline_pattern"]
            )
        )
    if "subtitle_configuration" in value:
        import aws_sdk_mediapackagev2.types.dash_subtitle_configuration

        out["SubtitleConfiguration"] = (
            aws_sdk_mediapackagev2.types.dash_subtitle_configuration.serialize_json(
                value["subtitle_configuration"]
            )
        )
    if "uri_path_type" in value:
        import aws_sdk_mediapackagev2.types.uri_path_type

        out["UriPathType"] = aws_sdk_mediapackagev2.types.uri_path_type.serialize_json(
            value["uri_path_type"]
        )
    if "availability_start_time_configuration" in value:
        import aws_sdk_mediapackagev2.types.dash_availability_start_time_configuration

        out["AvailabilityStartTimeConfiguration"] = (
            aws_sdk_mediapackagev2.types.dash_availability_start_time_configuration.serialize_json(
                value["availability_start_time_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDashManifestConfiguration:
    out: CreateDashManifestConfiguration = {}  # type: ignore[typeddict-item]
    if "ManifestName" in data:
        out["manifest_name"] = data["ManifestName"]
    else:
        raise DeserializationError(
            "CreateDashManifestConfiguration.manifest_name required"
        )
    if "ManifestWindowSeconds" in data:
        out["manifest_window_seconds"] = data["ManifestWindowSeconds"]
    if "FilterConfiguration" in data:
        import aws_sdk_mediapackagev2.types.filter_configuration

        out["filter_configuration"] = (
            aws_sdk_mediapackagev2.types.filter_configuration.deserialize_json(
                data["FilterConfiguration"]
            )
        )
    if "MinUpdatePeriodSeconds" in data:
        out["min_update_period_seconds"] = data["MinUpdatePeriodSeconds"]
    if "MinBufferTimeSeconds" in data:
        out["min_buffer_time_seconds"] = data["MinBufferTimeSeconds"]
    if "SuggestedPresentationDelaySeconds" in data:
        out["suggested_presentation_delay_seconds"] = data[
            "SuggestedPresentationDelaySeconds"
        ]
    if "SegmentTemplateFormat" in data:
        import aws_sdk_mediapackagev2.types.dash_segment_template_format

        out["segment_template_format"] = (
            aws_sdk_mediapackagev2.types.dash_segment_template_format.deserialize_json(
                data["SegmentTemplateFormat"]
            )
        )
    if "PeriodTriggers" in data:
        import aws_sdk_mediapackagev2.types.dash_period_triggers

        out["period_triggers"] = (
            aws_sdk_mediapackagev2.types.dash_period_triggers.deserialize_json(
                data["PeriodTriggers"]
            )
        )
    if "ScteDash" in data:
        import aws_sdk_mediapackagev2.types.scte_dash

        out["scte_dash"] = aws_sdk_mediapackagev2.types.scte_dash.deserialize_json(
            data["ScteDash"]
        )
    if "DrmSignaling" in data:
        import aws_sdk_mediapackagev2.types.dash_drm_signaling

        out["drm_signaling"] = (
            aws_sdk_mediapackagev2.types.dash_drm_signaling.deserialize_json(
                data["DrmSignaling"]
            )
        )
    if "UtcTiming" in data:
        import aws_sdk_mediapackagev2.types.dash_utc_timing

        out["utc_timing"] = (
            aws_sdk_mediapackagev2.types.dash_utc_timing.deserialize_json(
                data["UtcTiming"]
            )
        )
    if "Profiles" in data:
        import aws_sdk_mediapackagev2.types.dash_profiles

        out["profiles"] = aws_sdk_mediapackagev2.types.dash_profiles.deserialize_json(
            data["Profiles"]
        )
    if "BaseUrls" in data:
        import aws_sdk_mediapackagev2.types.dash_base_urls

        out["base_urls"] = aws_sdk_mediapackagev2.types.dash_base_urls.deserialize_json(
            data["BaseUrls"]
        )
    if "ProgramInformation" in data:
        import aws_sdk_mediapackagev2.types.dash_program_information

        out["program_information"] = (
            aws_sdk_mediapackagev2.types.dash_program_information.deserialize_json(
                data["ProgramInformation"]
            )
        )
    if "DvbSettings" in data:
        import aws_sdk_mediapackagev2.types.dash_dvb_settings

        out["dvb_settings"] = (
            aws_sdk_mediapackagev2.types.dash_dvb_settings.deserialize_json(
                data["DvbSettings"]
            )
        )
    if "Compactness" in data:
        import aws_sdk_mediapackagev2.types.dash_compactness

        out["compactness"] = (
            aws_sdk_mediapackagev2.types.dash_compactness.deserialize_json(
                data["Compactness"]
            )
        )
    if "AudioTimelinePattern" in data:
        import aws_sdk_mediapackagev2.types.dash_audio_timeline_pattern

        out["audio_timeline_pattern"] = (
            aws_sdk_mediapackagev2.types.dash_audio_timeline_pattern.deserialize_json(
                data["AudioTimelinePattern"]
            )
        )
    if "SubtitleConfiguration" in data:
        import aws_sdk_mediapackagev2.types.dash_subtitle_configuration

        out["subtitle_configuration"] = (
            aws_sdk_mediapackagev2.types.dash_subtitle_configuration.deserialize_json(
                data["SubtitleConfiguration"]
            )
        )
    if "UriPathType" in data:
        import aws_sdk_mediapackagev2.types.uri_path_type

        out["uri_path_type"] = (
            aws_sdk_mediapackagev2.types.uri_path_type.deserialize_json(
                data["UriPathType"]
            )
        )
    if "AvailabilityStartTimeConfiguration" in data:
        import aws_sdk_mediapackagev2.types.dash_availability_start_time_configuration

        out["availability_start_time_configuration"] = (
            aws_sdk_mediapackagev2.types.dash_availability_start_time_configuration.deserialize_json(
                data["AvailabilityStartTimeConfiguration"]
            )
        )
    return out
