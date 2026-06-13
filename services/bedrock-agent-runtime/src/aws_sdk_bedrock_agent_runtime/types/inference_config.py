"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InferenceConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.text_inference_config


class InferenceConfig(TypedDict):
    text_inference_config: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.text_inference_config.TextInferenceConfig"
    ]
    """<p> Configuration settings specific to text generation while generating responses using RetrieveAndGenerate. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceConfig) -> dict:
    out: dict = {}
    if "text_inference_config" in value:
        import aws_sdk_bedrock_agent_runtime.types.text_inference_config

        out["textInferenceConfig"] = (
            aws_sdk_bedrock_agent_runtime.types.text_inference_config.serialize_json(
                value["text_inference_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> InferenceConfig:
    out: InferenceConfig = {}  # type: ignore[typeddict-item]
    if "textInferenceConfig" in data:
        import aws_sdk_bedrock_agent_runtime.types.text_inference_config

        out["text_inference_config"] = (
            aws_sdk_bedrock_agent_runtime.types.text_inference_config.deserialize_json(
                data["textInferenceConfig"]
            )
        )
    return out
