"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#VoiceSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.voice_engine
    import aws_sdk_lex_models_v2.types.voice_id


class VoiceSettings(TypedDict):
    engine: NotRequired["aws_sdk_lex_models_v2.types.voice_engine.VoiceEngine"]
    r"""<p>Indicates the type of Amazon Polly voice that Amazon Lex should use for voice interaction with the user. For more information, see the <a href=\"https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#polly-SynthesizeSpeech-request-Engine\"> <code>engine</code> parameter of the <code>SynthesizeSpeech</code> operation</a> in the <i>Amazon Polly developer guide</i>.</p> <p>If you do not specify a value, the default is <code>standard</code>.</p>"""
    voice_id: "aws_sdk_lex_models_v2.types.voice_id.VoiceId"
    """<p>The identifier of the Amazon Polly voice to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceSettings) -> dict:
    out: dict = {}
    if "engine" in value:
        import aws_sdk_lex_models_v2.types.voice_engine

        out["engine"] = aws_sdk_lex_models_v2.types.voice_engine.serialize_json(
            value["engine"]
        )
    out["voiceId"] = value["voice_id"]
    return out


def deserialize_json(data: dict) -> VoiceSettings:
    out: VoiceSettings = {}  # type: ignore[typeddict-item]
    if "engine" in data:
        import aws_sdk_lex_models_v2.types.voice_engine

        out["engine"] = aws_sdk_lex_models_v2.types.voice_engine.deserialize_json(
            data["engine"]
        )
    if "voiceId" in data:
        out["voice_id"] = data["voiceId"]
    else:
        raise DeserializationError("VoiceSettings.voice_id required")
    return out
