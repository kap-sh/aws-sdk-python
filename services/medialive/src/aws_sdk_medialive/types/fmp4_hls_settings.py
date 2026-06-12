"""Generated from Smithy shape ``com.amazonaws.medialive#Fmp4HlsSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.fmp4_nielsen_id3_behavior
    import aws_sdk_medialive.types.fmp4_timed_metadata_behavior


class Fmp4HlsSettings(TypedDict):
    audio_rendition_sets: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by ','."""
    nielsen_id3_behavior: NotRequired[
        "aws_sdk_medialive.types.fmp4_nielsen_id3_behavior.Fmp4NielsenId3Behavior"
    ]
    """If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output."""
    timed_metadata_behavior: NotRequired[
        "aws_sdk_medialive.types.fmp4_timed_metadata_behavior.Fmp4TimedMetadataBehavior"
    ]
    """Set to PASSTHROUGH to enable ID3 metadata insertion. To include metadata, you configure other parameters in the output group or individual outputs, or you add an ID3 action to the channel schedule."""


# --- restJson1 ser/de ---
def serialize_json(value: Fmp4HlsSettings) -> dict:
    out: dict = {}
    if "audio_rendition_sets" in value:
        out["audioRenditionSets"] = value["audio_rendition_sets"]
    if "nielsen_id3_behavior" in value:
        import aws_sdk_medialive.types.fmp4_nielsen_id3_behavior

        out["nielsenId3Behavior"] = (
            aws_sdk_medialive.types.fmp4_nielsen_id3_behavior.serialize_json(
                value["nielsen_id3_behavior"]
            )
        )
    if "timed_metadata_behavior" in value:
        import aws_sdk_medialive.types.fmp4_timed_metadata_behavior

        out["timedMetadataBehavior"] = (
            aws_sdk_medialive.types.fmp4_timed_metadata_behavior.serialize_json(
                value["timed_metadata_behavior"]
            )
        )
    return out


def deserialize_json(data: dict) -> Fmp4HlsSettings:
    out: Fmp4HlsSettings = {}  # type: ignore[typeddict-item]
    if "audioRenditionSets" in data:
        out["audio_rendition_sets"] = data["audioRenditionSets"]
    if "nielsenId3Behavior" in data:
        import aws_sdk_medialive.types.fmp4_nielsen_id3_behavior

        out["nielsen_id3_behavior"] = (
            aws_sdk_medialive.types.fmp4_nielsen_id3_behavior.deserialize_json(
                data["nielsenId3Behavior"]
            )
        )
    if "timedMetadataBehavior" in data:
        import aws_sdk_medialive.types.fmp4_timed_metadata_behavior

        out["timed_metadata_behavior"] = (
            aws_sdk_medialive.types.fmp4_timed_metadata_behavior.deserialize_json(
                data["timedMetadataBehavior"]
            )
        )
    return out
