"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InferenceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.text_inference_config


class InferenceConfig(TypedDict, closed=True):
    text_inference_config: NotRequired[
        "capo_bedrock_agent_runtime.types.text_inference_config.TextInferenceConfig"
    ]
    """<p> Configuration settings specific to text generation while generating responses using RetrieveAndGenerate. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceConfig) -> dict:
    out: dict = {}
    if "text_inference_config" in value:
        import capo_bedrock_agent_runtime.types.text_inference_config

        out["textInferenceConfig"] = (
            capo_bedrock_agent_runtime.types.text_inference_config.serialize_json(
                value["text_inference_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> InferenceConfig:
    out: InferenceConfig = {}  # type: ignore[typeddict-item]
    if data.get("textInferenceConfig") is not None:
        import capo_bedrock_agent_runtime.types.text_inference_config

        out["text_inference_config"] = (
            capo_bedrock_agent_runtime.types.text_inference_config.deserialize_json(
                data["textInferenceConfig"]
            )
        )
    return out
