"""Generated from Smithy shape ``com.amazonaws.medialive#MediaPackageV2GroupSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min0_max10000
    import aws_sdk_medialive.types.__integer_min1
    import aws_sdk_medialive.types.__list_of_caption_language_mapping
    import aws_sdk_medialive.types.__list_of_media_package_additional_destinations
    import aws_sdk_medialive.types.cmaf_id3_behavior
    import aws_sdk_medialive.types.cmaf_ingest_segment_length_units
    import aws_sdk_medialive.types.cmaf_klv_behavior
    import aws_sdk_medialive.types.cmaf_nielsen_id3_behavior
    import aws_sdk_medialive.types.cmaf_timed_metadata_id3_frame
    import aws_sdk_medialive.types.cmaf_timed_metadata_passthrough
    import aws_sdk_medialive.types.scte35_type


class MediaPackageV2GroupSettings(TypedDict):
    caption_language_mappings: NotRequired[
        "aws_sdk_medialive.types.__list_of_caption_language_mapping.__listOfCaptionLanguageMapping"
    ]
    """Mapping of up to 4 caption channels to caption languages."""
    id3_behavior: NotRequired[
        "aws_sdk_medialive.types.cmaf_id3_behavior.CmafId3Behavior"
    ]
    """Set to ENABLED to enable ID3 metadata insertion. To include metadata, you configure other parameters in the output group, or you add an ID3 action to the channel schedule."""
    klv_behavior: NotRequired[
        "aws_sdk_medialive.types.cmaf_klv_behavior.CmafKLVBehavior"
    ]
    """If set to passthrough, passes any KLV data from the input source to this output."""
    nielsen_id3_behavior: NotRequired[
        "aws_sdk_medialive.types.cmaf_nielsen_id3_behavior.CmafNielsenId3Behavior"
    ]
    """If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output."""
    scte35_type: NotRequired["aws_sdk_medialive.types.scte35_type.Scte35Type"]
    """Type of scte35 track to add. none or scte35WithoutSegmentation"""
    segment_length: NotRequired["aws_sdk_medialive.types.__integer_min1.__integerMin1"]
    """The nominal duration of segments. The units are specified in SegmentLengthUnits. The segments will end on the next keyframe after the specified duration, so the actual segment length might be longer, and it might be a fraction of the units."""
    segment_length_units: NotRequired[
        "aws_sdk_medialive.types.cmaf_ingest_segment_length_units.CmafIngestSegmentLengthUnits"
    ]
    """Time unit for segment length parameter."""
    timed_metadata_id3_frame: NotRequired[
        "aws_sdk_medialive.types.cmaf_timed_metadata_id3_frame.CmafTimedMetadataId3Frame"
    ]
    """Set to none if you don't want to insert a timecode in the output. Otherwise choose the frame type for the timecode."""
    timed_metadata_id3_period: NotRequired[
        "aws_sdk_medialive.types.__integer_min0_max10000.__integerMin0Max10000"
    ]
    """If you set up to insert a timecode in the output, specify the frequency for the frame, in seconds."""
    timed_metadata_passthrough: NotRequired[
        "aws_sdk_medialive.types.cmaf_timed_metadata_passthrough.CmafTimedMetadataPassthrough"
    ]
    """Set to enabled to pass through ID3 metadata from the input sources."""
    additional_destinations: NotRequired[
        "aws_sdk_medialive.types.__list_of_media_package_additional_destinations.__listOfMediaPackageAdditionalDestinations"
    ]
    """Optional an array of additional destinational HTTP destinations for the OutputGroup outputs"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaPackageV2GroupSettings) -> dict:
    out: dict = {}
    if "caption_language_mappings" in value:
        import aws_sdk_medialive.types.__list_of_caption_language_mapping

        out["captionLanguageMappings"] = (
            aws_sdk_medialive.types.__list_of_caption_language_mapping.serialize_json(
                value["caption_language_mappings"]
            )
        )
    if "id3_behavior" in value:
        import aws_sdk_medialive.types.cmaf_id3_behavior

        out["id3Behavior"] = aws_sdk_medialive.types.cmaf_id3_behavior.serialize_json(
            value["id3_behavior"]
        )
    if "klv_behavior" in value:
        import aws_sdk_medialive.types.cmaf_klv_behavior

        out["klvBehavior"] = aws_sdk_medialive.types.cmaf_klv_behavior.serialize_json(
            value["klv_behavior"]
        )
    if "nielsen_id3_behavior" in value:
        import aws_sdk_medialive.types.cmaf_nielsen_id3_behavior

        out["nielsenId3Behavior"] = (
            aws_sdk_medialive.types.cmaf_nielsen_id3_behavior.serialize_json(
                value["nielsen_id3_behavior"]
            )
        )
    if "scte35_type" in value:
        import aws_sdk_medialive.types.scte35_type

        out["scte35Type"] = aws_sdk_medialive.types.scte35_type.serialize_json(
            value["scte35_type"]
        )
    if "segment_length" in value:
        out["segmentLength"] = value["segment_length"]
    if "segment_length_units" in value:
        import aws_sdk_medialive.types.cmaf_ingest_segment_length_units

        out["segmentLengthUnits"] = (
            aws_sdk_medialive.types.cmaf_ingest_segment_length_units.serialize_json(
                value["segment_length_units"]
            )
        )
    if "timed_metadata_id3_frame" in value:
        import aws_sdk_medialive.types.cmaf_timed_metadata_id3_frame

        out["timedMetadataId3Frame"] = (
            aws_sdk_medialive.types.cmaf_timed_metadata_id3_frame.serialize_json(
                value["timed_metadata_id3_frame"]
            )
        )
    if "timed_metadata_id3_period" in value:
        out["timedMetadataId3Period"] = value["timed_metadata_id3_period"]
    if "timed_metadata_passthrough" in value:
        import aws_sdk_medialive.types.cmaf_timed_metadata_passthrough

        out["timedMetadataPassthrough"] = (
            aws_sdk_medialive.types.cmaf_timed_metadata_passthrough.serialize_json(
                value["timed_metadata_passthrough"]
            )
        )
    if "additional_destinations" in value:
        import aws_sdk_medialive.types.__list_of_media_package_additional_destinations

        out["additionalDestinations"] = (
            aws_sdk_medialive.types.__list_of_media_package_additional_destinations.serialize_json(
                value["additional_destinations"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaPackageV2GroupSettings:
    out: MediaPackageV2GroupSettings = {}  # type: ignore[typeddict-item]
    if "captionLanguageMappings" in data:
        import aws_sdk_medialive.types.__list_of_caption_language_mapping

        out["caption_language_mappings"] = (
            aws_sdk_medialive.types.__list_of_caption_language_mapping.deserialize_json(
                data["captionLanguageMappings"]
            )
        )
    if "id3Behavior" in data:
        import aws_sdk_medialive.types.cmaf_id3_behavior

        out["id3_behavior"] = (
            aws_sdk_medialive.types.cmaf_id3_behavior.deserialize_json(
                data["id3Behavior"]
            )
        )
    if "klvBehavior" in data:
        import aws_sdk_medialive.types.cmaf_klv_behavior

        out["klv_behavior"] = (
            aws_sdk_medialive.types.cmaf_klv_behavior.deserialize_json(
                data["klvBehavior"]
            )
        )
    if "nielsenId3Behavior" in data:
        import aws_sdk_medialive.types.cmaf_nielsen_id3_behavior

        out["nielsen_id3_behavior"] = (
            aws_sdk_medialive.types.cmaf_nielsen_id3_behavior.deserialize_json(
                data["nielsenId3Behavior"]
            )
        )
    if "scte35Type" in data:
        import aws_sdk_medialive.types.scte35_type

        out["scte35_type"] = aws_sdk_medialive.types.scte35_type.deserialize_json(
            data["scte35Type"]
        )
    if "segmentLength" in data:
        out["segment_length"] = data["segmentLength"]
    if "segmentLengthUnits" in data:
        import aws_sdk_medialive.types.cmaf_ingest_segment_length_units

        out["segment_length_units"] = (
            aws_sdk_medialive.types.cmaf_ingest_segment_length_units.deserialize_json(
                data["segmentLengthUnits"]
            )
        )
    if "timedMetadataId3Frame" in data:
        import aws_sdk_medialive.types.cmaf_timed_metadata_id3_frame

        out["timed_metadata_id3_frame"] = (
            aws_sdk_medialive.types.cmaf_timed_metadata_id3_frame.deserialize_json(
                data["timedMetadataId3Frame"]
            )
        )
    if "timedMetadataId3Period" in data:
        out["timed_metadata_id3_period"] = data["timedMetadataId3Period"]
    if "timedMetadataPassthrough" in data:
        import aws_sdk_medialive.types.cmaf_timed_metadata_passthrough

        out["timed_metadata_passthrough"] = (
            aws_sdk_medialive.types.cmaf_timed_metadata_passthrough.deserialize_json(
                data["timedMetadataPassthrough"]
            )
        )
    if "additionalDestinations" in data:
        import aws_sdk_medialive.types.__list_of_media_package_additional_destinations

        out["additional_destinations"] = (
            aws_sdk_medialive.types.__list_of_media_package_additional_destinations.deserialize_json(
                data["additionalDestinations"]
            )
        )
    return out
