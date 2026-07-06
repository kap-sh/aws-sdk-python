"""Generated from Smithy shape ``com.amazonaws.qbusiness#AudioExtractionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.audio_extraction_status


class AudioExtractionConfiguration(TypedDict, closed=True):
    audio_extraction_status: (
        "aws_sdk_qbusiness.types.audio_extraction_status.AudioExtractionStatus"
    )
    """<p>The status of audio extraction (ENABLED or DISABLED) for processing audio content from files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioExtractionConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.audio_extraction_status

    out["audioExtractionStatus"] = (
        aws_sdk_qbusiness.types.audio_extraction_status.serialize_json(
            value["audio_extraction_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> AudioExtractionConfiguration:
    out: AudioExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if "audioExtractionStatus" in data:
        import aws_sdk_qbusiness.types.audio_extraction_status

        out["audio_extraction_status"] = (
            aws_sdk_qbusiness.types.audio_extraction_status.deserialize_json(
                data["audioExtractionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "AudioExtractionConfiguration.audio_extraction_status required"
        )
    return out
