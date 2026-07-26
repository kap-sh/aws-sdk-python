"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeepgramSpeechModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.deepgram_model_id
    import capo_lex_models_v2.types.secrets_manager_secret_arn


class DeepgramSpeechModelConfig(TypedDict, closed=True):
    api_token_secret_arn: (
        "capo_lex_models_v2.types.secrets_manager_secret_arn.SecretsManagerSecretArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Secrets Manager secret that contains the Deepgram API token.</p>"""
    model_id: NotRequired["capo_lex_models_v2.types.deepgram_model_id.DeepgramModelId"]
    """<p>The identifier of the Deepgram speech-to-text model to use for processing speech input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeepgramSpeechModelConfig) -> dict:
    out: dict = {}
    out["apiTokenSecretArn"] = value["api_token_secret_arn"]
    if "model_id" in value:
        out["modelId"] = value["model_id"]
    return out


def deserialize_json(data: dict) -> DeepgramSpeechModelConfig:
    out: DeepgramSpeechModelConfig = {}  # type: ignore[typeddict-item]
    if "apiTokenSecretArn" in data:
        out["api_token_secret_arn"] = data["apiTokenSecretArn"]
    else:
        raise DeserializationError(
            "DeepgramSpeechModelConfig.api_token_secret_arn required"
        )
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    return out
