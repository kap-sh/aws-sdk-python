"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptModelInferenceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.maximum_length
    import capo_bedrock_agent.types.stop_sequences
    import capo_bedrock_agent.types.temperature
    import capo_bedrock_agent.types.top_p


class PromptModelInferenceConfiguration(TypedDict, closed=True):
    temperature: NotRequired["capo_bedrock_agent.types.temperature.Temperature"]
    """<p>Controls the randomness of the response. Choose a lower value for more predictable outputs and a higher value for more surprising outputs.</p>"""
    top_p: NotRequired["capo_bedrock_agent.types.top_p.TopP"]
    """<p>The percentage of most-likely candidates that the model considers for the next token.</p>"""
    max_tokens: NotRequired["capo_bedrock_agent.types.maximum_length.MaximumLength"]
    """<p>The maximum number of tokens to return in the response.</p>"""
    stop_sequences: NotRequired["capo_bedrock_agent.types.stop_sequences.StopSequences"]
    """<p>A list of strings that define sequences after which the model will stop generating.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptModelInferenceConfiguration) -> dict:
    out: dict = {}
    if "temperature" in value:
        out["temperature"] = value["temperature"]
    if "top_p" in value:
        out["topP"] = value["top_p"]
    if "max_tokens" in value:
        out["maxTokens"] = value["max_tokens"]
    if "stop_sequences" in value:
        import capo_bedrock_agent.types.stop_sequences

        out["stopSequences"] = capo_bedrock_agent.types.stop_sequences.serialize_json(
            value["stop_sequences"]
        )
    return out


def deserialize_json(data: dict) -> PromptModelInferenceConfiguration:
    out: PromptModelInferenceConfiguration = {}  # type: ignore[typeddict-item]
    if "temperature" in data:
        out["temperature"] = data["temperature"]
    if "topP" in data:
        out["top_p"] = data["topP"]
    if "maxTokens" in data:
        out["max_tokens"] = data["maxTokens"]
    if "stopSequences" in data:
        import capo_bedrock_agent.types.stop_sequences

        out["stop_sequences"] = (
            capo_bedrock_agent.types.stop_sequences.deserialize_json(
                data["stopSequences"]
            )
        )
    return out
