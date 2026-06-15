"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#DashPackage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__boolean
    import aws_sdk_mediapackage_vod.types.__integer
    import aws_sdk_mediapackage_vod.types.__list_of__period_triggers_element
    import aws_sdk_mediapackage_vod.types.__list_of_dash_manifest
    import aws_sdk_mediapackage_vod.types.dash_encryption
    import aws_sdk_mediapackage_vod.types.segment_template_format


class DashPackage(TypedDict):
    dash_manifests: NotRequired[
        "aws_sdk_mediapackage_vod.types.__list_of_dash_manifest.__listOfDashManifest"
    ]
    """A list of DASH manifest configurations."""
    encryption: NotRequired[
        "aws_sdk_mediapackage_vod.types.dash_encryption.DashEncryption"
    ]
    include_encoder_configuration_in_segments: NotRequired[
        "aws_sdk_mediapackage_vod.types.__boolean.__boolean"
    ]
    """When includeEncoderConfigurationInSegments is set to true, MediaPackage places your encoder's Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) metadata in every video segment instead of in the init fragment. This lets you use different SPS/PPS/VPS settings for your assets during content playback."""
    include_iframe_only_stream: NotRequired[
        "aws_sdk_mediapackage_vod.types.__boolean.__boolean"
    ]
    """When enabled, an I-Frame only stream will be included in the output."""
    period_triggers: NotRequired[
        "aws_sdk_mediapackage_vod.types.__list_of__period_triggers_element.__listOf__PeriodTriggersElement"
    ]
    r"""A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains \"ADS\", new periods will be created where the Asset contains SCTE-35 ad markers."""
    segment_duration_seconds: NotRequired[
        "aws_sdk_mediapackage_vod.types.__integer.__integer"
    ]
    """Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration."""
    segment_template_format: NotRequired[
        "aws_sdk_mediapackage_vod.types.segment_template_format.SegmentTemplateFormat"
    ]
    """Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs."""


# --- restJson1 ser/de ---
def serialize_json(value: DashPackage) -> dict:
    out: dict = {}
    if "dash_manifests" in value:
        import aws_sdk_mediapackage_vod.types.__list_of_dash_manifest

        out["dashManifests"] = (
            aws_sdk_mediapackage_vod.types.__list_of_dash_manifest.serialize_json(
                value["dash_manifests"]
            )
        )
    if "encryption" in value:
        import aws_sdk_mediapackage_vod.types.dash_encryption

        out["encryption"] = (
            aws_sdk_mediapackage_vod.types.dash_encryption.serialize_json(
                value["encryption"]
            )
        )
    if "include_encoder_configuration_in_segments" in value:
        out["includeEncoderConfigurationInSegments"] = value[
            "include_encoder_configuration_in_segments"
        ]
    if "include_iframe_only_stream" in value:
        out["includeIframeOnlyStream"] = value["include_iframe_only_stream"]
    if "period_triggers" in value:
        import aws_sdk_mediapackage_vod.types.__list_of__period_triggers_element

        out["periodTriggers"] = (
            aws_sdk_mediapackage_vod.types.__list_of__period_triggers_element.serialize_json(
                value["period_triggers"]
            )
        )
    if "segment_duration_seconds" in value:
        out["segmentDurationSeconds"] = value["segment_duration_seconds"]
    if "segment_template_format" in value:
        import aws_sdk_mediapackage_vod.types.segment_template_format

        out["segmentTemplateFormat"] = (
            aws_sdk_mediapackage_vod.types.segment_template_format.serialize_json(
                value["segment_template_format"]
            )
        )
    return out


def deserialize_json(data: dict) -> DashPackage:
    out: DashPackage = {}  # type: ignore[typeddict-item]
    if "dashManifests" in data:
        import aws_sdk_mediapackage_vod.types.__list_of_dash_manifest

        out["dash_manifests"] = (
            aws_sdk_mediapackage_vod.types.__list_of_dash_manifest.deserialize_json(
                data["dashManifests"]
            )
        )
    if "encryption" in data:
        import aws_sdk_mediapackage_vod.types.dash_encryption

        out["encryption"] = (
            aws_sdk_mediapackage_vod.types.dash_encryption.deserialize_json(
                data["encryption"]
            )
        )
    if "includeEncoderConfigurationInSegments" in data:
        out["include_encoder_configuration_in_segments"] = data[
            "includeEncoderConfigurationInSegments"
        ]
    if "includeIframeOnlyStream" in data:
        out["include_iframe_only_stream"] = data["includeIframeOnlyStream"]
    if "periodTriggers" in data:
        import aws_sdk_mediapackage_vod.types.__list_of__period_triggers_element

        out["period_triggers"] = (
            aws_sdk_mediapackage_vod.types.__list_of__period_triggers_element.deserialize_json(
                data["periodTriggers"]
            )
        )
    if "segmentDurationSeconds" in data:
        out["segment_duration_seconds"] = data["segmentDurationSeconds"]
    if "segmentTemplateFormat" in data:
        import aws_sdk_mediapackage_vod.types.segment_template_format

        out["segment_template_format"] = (
            aws_sdk_mediapackage_vod.types.segment_template_format.deserialize_json(
                data["segmentTemplateFormat"]
            )
        )
    return out
