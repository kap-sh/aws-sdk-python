"""Generated from Smithy shape ``com.amazonaws.qbusiness#SourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.audio_source_details
    import capo_qbusiness.types.image_source_details
    import capo_qbusiness.types.video_source_details


class _SourceDetails_imageSourceDetails(TypedDict, closed=True):
    imageSourceDetails: "capo_qbusiness.types.image_source_details.ImageSourceDetails"


class _SourceDetails_audioSourceDetails(TypedDict, closed=True):
    audioSourceDetails: "capo_qbusiness.types.audio_source_details.AudioSourceDetails"


class _SourceDetails_videoSourceDetails(TypedDict, closed=True):
    videoSourceDetails: "capo_qbusiness.types.video_source_details.VideoSourceDetails"


SourceDetails: TypeAlias = (
    _SourceDetails_imageSourceDetails
    | _SourceDetails_audioSourceDetails
    | _SourceDetails_videoSourceDetails
)


# --- restJson1 ser/de ---
def serialize_json(value: SourceDetails) -> dict:
    if "imageSourceDetails" in value:
        import capo_qbusiness.types.image_source_details

        return {
            "imageSourceDetails": capo_qbusiness.types.image_source_details.serialize_json(
                value["imageSourceDetails"]
            )
        }
    elif "audioSourceDetails" in value:
        import capo_qbusiness.types.audio_source_details

        return {
            "audioSourceDetails": capo_qbusiness.types.audio_source_details.serialize_json(
                value["audioSourceDetails"]
            )
        }
    elif "videoSourceDetails" in value:
        import capo_qbusiness.types.video_source_details

        return {
            "videoSourceDetails": capo_qbusiness.types.video_source_details.serialize_json(
                value["videoSourceDetails"]
            )
        }
    else:
        raise SerializationError("SourceDetails: no variant present")


def deserialize_json(data: dict) -> SourceDetails:
    if "imageSourceDetails" in data:
        import capo_qbusiness.types.image_source_details

        return {
            "imageSourceDetails": capo_qbusiness.types.image_source_details.deserialize_json(
                data["imageSourceDetails"]
            )
        }
    elif "audioSourceDetails" in data:
        import capo_qbusiness.types.audio_source_details

        return {
            "audioSourceDetails": capo_qbusiness.types.audio_source_details.deserialize_json(
                data["audioSourceDetails"]
            )
        }
    elif "videoSourceDetails" in data:
        import capo_qbusiness.types.video_source_details

        return {
            "videoSourceDetails": capo_qbusiness.types.video_source_details.deserialize_json(
                data["videoSourceDetails"]
            )
        }
    else:
        raise DeserializationError("SourceDetails: no recognized variant key")
