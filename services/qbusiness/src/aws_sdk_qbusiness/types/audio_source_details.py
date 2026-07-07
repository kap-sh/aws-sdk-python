"""Generated from Smithy shape ``com.amazonaws.qbusiness#AudioSourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.audio_extraction_type
    import aws_sdk_qbusiness.types.long
    import aws_sdk_qbusiness.types.media_id
    import aws_sdk_qbusiness.types.string


class AudioSourceDetails(TypedDict, closed=True):
    media_id: NotRequired["aws_sdk_qbusiness.types.media_id.MediaId"]
    """<p>Unique identifier for the audio media file.</p>"""
    media_mime_type: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The MIME type of the audio file (e.g., audio/mp3, audio/wav).</p>"""
    start_time_milliseconds: NotRequired["aws_sdk_qbusiness.types.long.Long"]
    """<p>The starting timestamp in milliseconds for the relevant audio segment.</p>"""
    end_time_milliseconds: NotRequired["aws_sdk_qbusiness.types.long.Long"]
    """<p>The ending timestamp in milliseconds for the relevant audio segment.</p>"""
    audio_extraction_type: NotRequired[
        "aws_sdk_qbusiness.types.audio_extraction_type.AudioExtractionType"
    ]
    """<p>The type of audio extraction performed on the content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioSourceDetails) -> dict:
    out: dict = {}
    if "media_id" in value:
        out["mediaId"] = value["media_id"]
    if "media_mime_type" in value:
        out["mediaMimeType"] = value["media_mime_type"]
    if "start_time_milliseconds" in value:
        out["startTimeMilliseconds"] = value["start_time_milliseconds"]
    if "end_time_milliseconds" in value:
        out["endTimeMilliseconds"] = value["end_time_milliseconds"]
    if "audio_extraction_type" in value:
        import aws_sdk_qbusiness.types.audio_extraction_type

        out["audioExtractionType"] = (
            aws_sdk_qbusiness.types.audio_extraction_type.serialize_json(
                value["audio_extraction_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioSourceDetails:
    out: AudioSourceDetails = {}  # type: ignore[typeddict-item]
    if "mediaId" in data:
        out["media_id"] = data["mediaId"]
    if "mediaMimeType" in data:
        out["media_mime_type"] = data["mediaMimeType"]
    if "startTimeMilliseconds" in data:
        out["start_time_milliseconds"] = data["startTimeMilliseconds"]
    if "endTimeMilliseconds" in data:
        out["end_time_milliseconds"] = data["endTimeMilliseconds"]
    if "audioExtractionType" in data:
        import aws_sdk_qbusiness.types.audio_extraction_type

        out["audio_extraction_type"] = (
            aws_sdk_qbusiness.types.audio_extraction_type.deserialize_json(
                data["audioExtractionType"]
            )
        )
    return out
