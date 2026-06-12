"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SpeechFoundationModel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bedrock_model_arn
    import aws_sdk_lex_models_v2.types.voice_id


class SpeechFoundationModel(TypedDict):
    model_arn: "aws_sdk_lex_models_v2.types.bedrock_model_arn.BedrockModelArn"
    """<p>The Amazon Resource Name (ARN) of the foundation model used for speech processing.</p>"""
    voice_id: NotRequired["aws_sdk_lex_models_v2.types.voice_id.VoiceId"]
    """<p>The identifier of the voice to use for speech synthesis with the foundation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpeechFoundationModel) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    if "voice_id" in value:
        out["voiceId"] = value["voice_id"]
    return out


def deserialize_json(data: dict) -> SpeechFoundationModel:
    out: SpeechFoundationModel = {}  # type: ignore[typeddict-item]
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError("SpeechFoundationModel.model_arn required")
    if "voiceId" in data:
        out["voice_id"] = data["voiceId"]
    return out
