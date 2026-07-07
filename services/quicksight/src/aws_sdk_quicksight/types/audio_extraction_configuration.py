"""Generated from Smithy shape ``com.amazonaws.quicksight#AudioExtractionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.audio_extraction_status


class AudioExtractionConfiguration(TypedDict, closed=True):
    audio_extraction_status: (
        "aws_sdk_quicksight.types.audio_extraction_status.AudioExtractionStatus"
    )
    """<p>The status of audio extraction. Valid values are ENABLED and DISABLED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioExtractionConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.audio_extraction_status

    out["audioExtractionStatus"] = (
        aws_sdk_quicksight.types.audio_extraction_status.serialize_json(
            value["audio_extraction_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> AudioExtractionConfiguration:
    out: AudioExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if "audioExtractionStatus" in data:
        import aws_sdk_quicksight.types.audio_extraction_status

        out["audio_extraction_status"] = (
            aws_sdk_quicksight.types.audio_extraction_status.deserialize_json(
                data["audioExtractionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "AudioExtractionConfiguration.audio_extraction_status required"
        )
    return out
