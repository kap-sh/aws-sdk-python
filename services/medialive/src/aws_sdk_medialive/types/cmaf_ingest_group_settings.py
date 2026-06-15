"""Generated from Smithy shape ``com.amazonaws.medialive#CmafIngestGroupSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min0_max2000
    import aws_sdk_medialive.types.__integer_min0_max10000
    import aws_sdk_medialive.types.__integer_min1
    import aws_sdk_medialive.types.__list_of_additional_destinations
    import aws_sdk_medialive.types.__list_of_cmaf_ingest_caption_language_mapping
    import aws_sdk_medialive.types.__string_max100
    import aws_sdk_medialive.types.cmaf_id3_behavior
    import aws_sdk_medialive.types.cmaf_ingest_segment_length_units
    import aws_sdk_medialive.types.cmaf_klv_behavior
    import aws_sdk_medialive.types.cmaf_nielsen_id3_behavior
    import aws_sdk_medialive.types.cmaf_timed_metadata_id3_frame
    import aws_sdk_medialive.types.cmaf_timed_metadata_passthrough
    import aws_sdk_medialive.types.output_location_ref
    import aws_sdk_medialive.types.scte35_type


class CmafIngestGroupSettings(TypedDict):
    destination: NotRequired[
        "aws_sdk_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """A HTTP destination for the tracks"""
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
    send_delay_ms: NotRequired[
        "aws_sdk_medialive.types.__integer_min0_max2000.__integerMin0Max2000"
    ]
    """Number of milliseconds to delay the output from the second pipeline."""
    klv_behavior: NotRequired[
        "aws_sdk_medialive.types.cmaf_klv_behavior.CmafKLVBehavior"
    ]
    """If set to passthrough, passes any KLV data from the input source to this output."""
    klv_name_modifier: NotRequired[
        "aws_sdk_medialive.types.__string_max100.__stringMax100"
    ]
    r"""Change the modifier that MediaLive automatically adds to the Streams() name that identifies a KLV track. The default is \"klv\", which means the default name will be Streams(klv.cmfm). Any string you enter here will replace the \"klv\" string.\nThe modifier can only contain: numbers, letters, plus (+), minus (-), underscore (_) and period (.) and has a maximum length of 100 characters."""
    nielsen_id3_name_modifier: NotRequired[
        "aws_sdk_medialive.types.__string_max100.__stringMax100"
    ]
    r"""Change the modifier that MediaLive automatically adds to the Streams() name that identifies a Nielsen ID3 track. The default is \"nid3\", which means the default name will be Streams(nid3.cmfm). Any string you enter here will replace the \"nid3\" string.\nThe modifier can only contain: numbers, letters, plus (+), minus (-), underscore (_) and period (.) and has a maximum length of 100 characters."""
    scte35_name_modifier: NotRequired[
        "aws_sdk_medialive.types.__string_max100.__stringMax100"
    ]
    r"""Change the modifier that MediaLive automatically adds to the Streams() name for a SCTE 35 track. The default is \"scte\", which means the default name will be Streams(scte.cmfm). Any string you enter here will replace the \"scte\" string.\nThe modifier can only contain: numbers, letters, plus (+), minus (-), underscore (_) and period (.) and has a maximum length of 100 characters."""
    id3_behavior: NotRequired[
        "aws_sdk_medialive.types.cmaf_id3_behavior.CmafId3Behavior"
    ]
    """Set to ENABLED to enable ID3 metadata insertion. To include metadata, you configure other parameters in the output group, or you add an ID3 action to the channel schedule."""
    id3_name_modifier: NotRequired[
        "aws_sdk_medialive.types.__string_max100.__stringMax100"
    ]
    r"""Change the modifier that MediaLive automatically adds to the Streams() name that identifies an ID3 track. The default is \"id3\", which means the default name will be Streams(id3.cmfm). Any string you enter here will replace the \"id3\" string.\nThe modifier can only contain: numbers, letters, plus (+), minus (-), underscore (_) and period (.) and has a maximum length of 100 characters."""
    caption_language_mappings: NotRequired[
        "aws_sdk_medialive.types.__list_of_cmaf_ingest_caption_language_mapping.__listOfCmafIngestCaptionLanguageMapping"
    ]
    """An array that identifies the languages in the four caption channels in the embedded captions."""
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
        "aws_sdk_medialive.types.__list_of_additional_destinations.__listOfAdditionalDestinations"
    ]
    """Optional an array of additional destinational HTTP destinations for the OutputGroup outputs"""


# --- restJson1 ser/de ---
def serialize_json(value: CmafIngestGroupSettings) -> dict:
    out: dict = {}
    if "destination" in value:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = aws_sdk_medialive.types.output_location_ref.serialize_json(
            value["destination"]
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
    if "send_delay_ms" in value:
        out["sendDelayMs"] = value["send_delay_ms"]
    if "klv_behavior" in value:
        import aws_sdk_medialive.types.cmaf_klv_behavior

        out["klvBehavior"] = aws_sdk_medialive.types.cmaf_klv_behavior.serialize_json(
            value["klv_behavior"]
        )
    if "klv_name_modifier" in value:
        out["klvNameModifier"] = value["klv_name_modifier"]
    if "nielsen_id3_name_modifier" in value:
        out["nielsenId3NameModifier"] = value["nielsen_id3_name_modifier"]
    if "scte35_name_modifier" in value:
        out["scte35NameModifier"] = value["scte35_name_modifier"]
    if "id3_behavior" in value:
        import aws_sdk_medialive.types.cmaf_id3_behavior

        out["id3Behavior"] = aws_sdk_medialive.types.cmaf_id3_behavior.serialize_json(
            value["id3_behavior"]
        )
    if "id3_name_modifier" in value:
        out["id3NameModifier"] = value["id3_name_modifier"]
    if "caption_language_mappings" in value:
        import aws_sdk_medialive.types.__list_of_cmaf_ingest_caption_language_mapping

        out["captionLanguageMappings"] = (
            aws_sdk_medialive.types.__list_of_cmaf_ingest_caption_language_mapping.serialize_json(
                value["caption_language_mappings"]
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
        import aws_sdk_medialive.types.__list_of_additional_destinations

        out["additionalDestinations"] = (
            aws_sdk_medialive.types.__list_of_additional_destinations.serialize_json(
                value["additional_destinations"]
            )
        )
    return out


def deserialize_json(data: dict) -> CmafIngestGroupSettings:
    out: CmafIngestGroupSettings = {}  # type: ignore[typeddict-item]
    if "destination" in data:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = (
            aws_sdk_medialive.types.output_location_ref.deserialize_json(
                data["destination"]
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
    if "sendDelayMs" in data:
        out["send_delay_ms"] = data["sendDelayMs"]
    if "klvBehavior" in data:
        import aws_sdk_medialive.types.cmaf_klv_behavior

        out["klv_behavior"] = (
            aws_sdk_medialive.types.cmaf_klv_behavior.deserialize_json(
                data["klvBehavior"]
            )
        )
    if "klvNameModifier" in data:
        out["klv_name_modifier"] = data["klvNameModifier"]
    if "nielsenId3NameModifier" in data:
        out["nielsen_id3_name_modifier"] = data["nielsenId3NameModifier"]
    if "scte35NameModifier" in data:
        out["scte35_name_modifier"] = data["scte35NameModifier"]
    if "id3Behavior" in data:
        import aws_sdk_medialive.types.cmaf_id3_behavior

        out["id3_behavior"] = (
            aws_sdk_medialive.types.cmaf_id3_behavior.deserialize_json(
                data["id3Behavior"]
            )
        )
    if "id3NameModifier" in data:
        out["id3_name_modifier"] = data["id3NameModifier"]
    if "captionLanguageMappings" in data:
        import aws_sdk_medialive.types.__list_of_cmaf_ingest_caption_language_mapping

        out["caption_language_mappings"] = (
            aws_sdk_medialive.types.__list_of_cmaf_ingest_caption_language_mapping.deserialize_json(
                data["captionLanguageMappings"]
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
        import aws_sdk_medialive.types.__list_of_additional_destinations

        out["additional_destinations"] = (
            aws_sdk_medialive.types.__list_of_additional_destinations.deserialize_json(
                data["additionalDestinations"]
            )
        )
    return out
