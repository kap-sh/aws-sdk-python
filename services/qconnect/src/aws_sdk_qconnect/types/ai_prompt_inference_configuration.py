"""Generated from Smithy shape ``com.amazonaws.qconnect#AIPromptInferenceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.max_tokens_to_sample
    import aws_sdk_qconnect.types.probability
    import aws_sdk_qconnect.types.top_k


class AIPromptInferenceConfiguration(TypedDict):
    temperature: NotRequired["aws_sdk_qconnect.types.probability.Probability"]
    """<p>The temperature setting for controlling randomness in the generated response.</p>"""
    top_p: NotRequired["aws_sdk_qconnect.types.probability.Probability"]
    """<p>The top-P sampling parameter for nucleus sampling.</p>"""
    top_k: NotRequired["aws_sdk_qconnect.types.top_k.TopK"]
    """<p>The top-K sampling parameter for token selection.</p>"""
    max_tokens_to_sample: NotRequired[
        "aws_sdk_qconnect.types.max_tokens_to_sample.MaxTokensToSample"
    ]
    """<p>The maximum number of tokens to generate in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIPromptInferenceConfiguration) -> dict:
    out: dict = {}
    if "temperature" in value:
        out["temperature"] = value["temperature"]
    if "top_p" in value:
        out["topP"] = value["top_p"]
    if "top_k" in value:
        out["topK"] = value["top_k"]
    if "max_tokens_to_sample" in value:
        out["maxTokensToSample"] = value["max_tokens_to_sample"]
    return out


def deserialize_json(data: dict) -> AIPromptInferenceConfiguration:
    out: AIPromptInferenceConfiguration = {}  # type: ignore[typeddict-item]
    if "temperature" in data:
        out["temperature"] = data["temperature"]
    if "topP" in data:
        out["top_p"] = data["topP"]
    if "topK" in data:
        out["top_k"] = data["topK"]
    if "maxTokensToSample" in data:
        out["max_tokens_to_sample"] = data["maxTokensToSample"]
    return out
