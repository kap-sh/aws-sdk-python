"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceAudioInputSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.audio_file_s3_location


class UtteranceAudioInputSpecification(TypedDict):
    audio_file_s3_location: (
        "aws_sdk_lex_models_v2.types.audio_file_s3_location.AudioFileS3Location"
    )
    """<p>Amazon S3 file pointing to the audio.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceAudioInputSpecification) -> dict:
    out: dict = {}
    out["audioFileS3Location"] = value["audio_file_s3_location"]
    return out


def deserialize_json(data: dict) -> UtteranceAudioInputSpecification:
    out: UtteranceAudioInputSpecification = {}  # type: ignore[typeddict-item]
    if "audioFileS3Location" in data:
        out["audio_file_s3_location"] = data["audioFileS3Location"]
    else:
        raise DeserializationError(
            "UtteranceAudioInputSpecification.audio_file_s3_location required"
        )
    return out
