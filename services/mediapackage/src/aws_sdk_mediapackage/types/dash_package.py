"""Generated from Smithy shape ``com.amazonaws.mediapackage#DashPackage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__boolean
    import aws_sdk_mediapackage.types.__integer
    import aws_sdk_mediapackage.types.__list_of__period_triggers_element
    import aws_sdk_mediapackage.types.__string
    import aws_sdk_mediapackage.types.ad_triggers
    import aws_sdk_mediapackage.types.ads_on_delivery_restrictions
    import aws_sdk_mediapackage.types.dash_encryption
    import aws_sdk_mediapackage.types.manifest_layout
    import aws_sdk_mediapackage.types.profile
    import aws_sdk_mediapackage.types.segment_template_format
    import aws_sdk_mediapackage.types.stream_selection
    import aws_sdk_mediapackage.types.utc_timing


class DashPackage(TypedDict):
    ad_triggers: NotRequired["aws_sdk_mediapackage.types.ad_triggers.AdTriggers"]
    ads_on_delivery_restrictions: NotRequired[
        "aws_sdk_mediapackage.types.ads_on_delivery_restrictions.AdsOnDeliveryRestrictions"
    ]
    encryption: NotRequired["aws_sdk_mediapackage.types.dash_encryption.DashEncryption"]
    include_iframe_only_stream: NotRequired[
        "aws_sdk_mediapackage.types.__boolean.__boolean"
    ]
    """When enabled, an I-Frame only stream will be included in the output."""
    manifest_layout: NotRequired[
        "aws_sdk_mediapackage.types.manifest_layout.ManifestLayout"
    ]
    """Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level. When set to DRM_TOP_LEVEL_COMPACT, content protection elements are placed the MPD level and referenced at the AdaptationSet level."""
    manifest_window_seconds: NotRequired[
        "aws_sdk_mediapackage.types.__integer.__integer"
    ]
    """Time window (in seconds) contained in each manifest."""
    min_buffer_time_seconds: NotRequired[
        "aws_sdk_mediapackage.types.__integer.__integer"
    ]
    """Minimum duration (in seconds) that a player will buffer media before starting the presentation."""
    min_update_period_seconds: NotRequired[
        "aws_sdk_mediapackage.types.__integer.__integer"
    ]
    """Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD)."""
    period_triggers: NotRequired[
        "aws_sdk_mediapackage.types.__list_of__period_triggers_element.__listOf__PeriodTriggersElement"
    ]
    """A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains \"ADS\", new periods will be created where the Channel source contains SCTE-35 ad markers."""
    profile: NotRequired["aws_sdk_mediapackage.types.profile.Profile"]
    """The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to \"HBBTV_1_5\", HbbTV 1.5 compliant output is enabled. When set to \"DVB-DASH_2014\", DVB-DASH 2014 compliant output is enabled."""
    segment_duration_seconds: NotRequired[
        "aws_sdk_mediapackage.types.__integer.__integer"
    ]
    """Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration."""
    segment_template_format: NotRequired[
        "aws_sdk_mediapackage.types.segment_template_format.SegmentTemplateFormat"
    ]
    """Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs."""
    stream_selection: NotRequired[
        "aws_sdk_mediapackage.types.stream_selection.StreamSelection"
    ]
    suggested_presentation_delay_seconds: NotRequired[
        "aws_sdk_mediapackage.types.__integer.__integer"
    ]
    """Duration (in seconds) to delay live content before presentation."""
    utc_timing: NotRequired["aws_sdk_mediapackage.types.utc_timing.UtcTiming"]
    """Determines the type of UTCTiming included in the Media Presentation Description (MPD)"""
    utc_timing_uri: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """Specifies the value attribute of the UTCTiming field when utcTiming is set to HTTP-ISO, HTTP-HEAD or HTTP-XSDATE"""


# --- restJson1 ser/de ---
def serialize_json(value: DashPackage) -> dict:
    out: dict = {}
    if "ad_triggers" in value:
        import aws_sdk_mediapackage.types.ad_triggers

        out["adTriggers"] = aws_sdk_mediapackage.types.ad_triggers.serialize_json(
            value["ad_triggers"]
        )
    if "ads_on_delivery_restrictions" in value:
        import aws_sdk_mediapackage.types.ads_on_delivery_restrictions

        out["adsOnDeliveryRestrictions"] = (
            aws_sdk_mediapackage.types.ads_on_delivery_restrictions.serialize_json(
                value["ads_on_delivery_restrictions"]
            )
        )
    if "encryption" in value:
        import aws_sdk_mediapackage.types.dash_encryption

        out["encryption"] = aws_sdk_mediapackage.types.dash_encryption.serialize_json(
            value["encryption"]
        )
    if "include_iframe_only_stream" in value:
        out["includeIframeOnlyStream"] = value["include_iframe_only_stream"]
    if "manifest_layout" in value:
        import aws_sdk_mediapackage.types.manifest_layout

        out["manifestLayout"] = (
            aws_sdk_mediapackage.types.manifest_layout.serialize_json(
                value["manifest_layout"]
            )
        )
    if "manifest_window_seconds" in value:
        out["manifestWindowSeconds"] = value["manifest_window_seconds"]
    if "min_buffer_time_seconds" in value:
        out["minBufferTimeSeconds"] = value["min_buffer_time_seconds"]
    if "min_update_period_seconds" in value:
        out["minUpdatePeriodSeconds"] = value["min_update_period_seconds"]
    if "period_triggers" in value:
        import aws_sdk_mediapackage.types.__list_of__period_triggers_element

        out["periodTriggers"] = (
            aws_sdk_mediapackage.types.__list_of__period_triggers_element.serialize_json(
                value["period_triggers"]
            )
        )
    if "profile" in value:
        import aws_sdk_mediapackage.types.profile

        out["profile"] = aws_sdk_mediapackage.types.profile.serialize_json(
            value["profile"]
        )
    if "segment_duration_seconds" in value:
        out["segmentDurationSeconds"] = value["segment_duration_seconds"]
    if "segment_template_format" in value:
        import aws_sdk_mediapackage.types.segment_template_format

        out["segmentTemplateFormat"] = (
            aws_sdk_mediapackage.types.segment_template_format.serialize_json(
                value["segment_template_format"]
            )
        )
    if "stream_selection" in value:
        import aws_sdk_mediapackage.types.stream_selection

        out["streamSelection"] = (
            aws_sdk_mediapackage.types.stream_selection.serialize_json(
                value["stream_selection"]
            )
        )
    if "suggested_presentation_delay_seconds" in value:
        out["suggestedPresentationDelaySeconds"] = value[
            "suggested_presentation_delay_seconds"
        ]
    if "utc_timing" in value:
        import aws_sdk_mediapackage.types.utc_timing

        out["utcTiming"] = aws_sdk_mediapackage.types.utc_timing.serialize_json(
            value["utc_timing"]
        )
    if "utc_timing_uri" in value:
        out["utcTimingUri"] = value["utc_timing_uri"]
    return out


def deserialize_json(data: dict) -> DashPackage:
    out: DashPackage = {}  # type: ignore[typeddict-item]
    if "adTriggers" in data:
        import aws_sdk_mediapackage.types.ad_triggers

        out["ad_triggers"] = aws_sdk_mediapackage.types.ad_triggers.deserialize_json(
            data["adTriggers"]
        )
    if "adsOnDeliveryRestrictions" in data:
        import aws_sdk_mediapackage.types.ads_on_delivery_restrictions

        out["ads_on_delivery_restrictions"] = (
            aws_sdk_mediapackage.types.ads_on_delivery_restrictions.deserialize_json(
                data["adsOnDeliveryRestrictions"]
            )
        )
    if "encryption" in data:
        import aws_sdk_mediapackage.types.dash_encryption

        out["encryption"] = aws_sdk_mediapackage.types.dash_encryption.deserialize_json(
            data["encryption"]
        )
    if "includeIframeOnlyStream" in data:
        out["include_iframe_only_stream"] = data["includeIframeOnlyStream"]
    if "manifestLayout" in data:
        import aws_sdk_mediapackage.types.manifest_layout

        out["manifest_layout"] = (
            aws_sdk_mediapackage.types.manifest_layout.deserialize_json(
                data["manifestLayout"]
            )
        )
    if "manifestWindowSeconds" in data:
        out["manifest_window_seconds"] = data["manifestWindowSeconds"]
    if "minBufferTimeSeconds" in data:
        out["min_buffer_time_seconds"] = data["minBufferTimeSeconds"]
    if "minUpdatePeriodSeconds" in data:
        out["min_update_period_seconds"] = data["minUpdatePeriodSeconds"]
    if "periodTriggers" in data:
        import aws_sdk_mediapackage.types.__list_of__period_triggers_element

        out["period_triggers"] = (
            aws_sdk_mediapackage.types.__list_of__period_triggers_element.deserialize_json(
                data["periodTriggers"]
            )
        )
    if "profile" in data:
        import aws_sdk_mediapackage.types.profile

        out["profile"] = aws_sdk_mediapackage.types.profile.deserialize_json(
            data["profile"]
        )
    if "segmentDurationSeconds" in data:
        out["segment_duration_seconds"] = data["segmentDurationSeconds"]
    if "segmentTemplateFormat" in data:
        import aws_sdk_mediapackage.types.segment_template_format

        out["segment_template_format"] = (
            aws_sdk_mediapackage.types.segment_template_format.deserialize_json(
                data["segmentTemplateFormat"]
            )
        )
    if "streamSelection" in data:
        import aws_sdk_mediapackage.types.stream_selection

        out["stream_selection"] = (
            aws_sdk_mediapackage.types.stream_selection.deserialize_json(
                data["streamSelection"]
            )
        )
    if "suggestedPresentationDelaySeconds" in data:
        out["suggested_presentation_delay_seconds"] = data[
            "suggestedPresentationDelaySeconds"
        ]
    if "utcTiming" in data:
        import aws_sdk_mediapackage.types.utc_timing

        out["utc_timing"] = aws_sdk_mediapackage.types.utc_timing.deserialize_json(
            data["utcTiming"]
        )
    if "utcTimingUri" in data:
        out["utc_timing_uri"] = data["utcTimingUri"]
    return out
