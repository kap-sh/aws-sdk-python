"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InferenceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.non_empty_string_list


class InferenceConfiguration(TypedDict, closed=True):
    max_tokens: NotRequired["int"]
    """<p> The maximum number of tokens to generate in the model response during evaluation. </p>"""
    temperature: NotRequired["float"]
    """<p> The temperature value that controls randomness in the model's responses. Lower values produce more deterministic outputs. </p>"""
    top_p: NotRequired["float"]
    """<p> The top-p sampling parameter that controls the diversity of the model's responses by limiting the cumulative probability of token choices. </p>"""
    stop_sequences: NotRequired[
        "capo_bedrock_agentcore_control.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> The list of sequences that will cause the model to stop generating tokens when encountered. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceConfiguration) -> dict:
    out: dict = {}
    if "max_tokens" in value:
        out["maxTokens"] = value["max_tokens"]
    if "temperature" in value:
        out["temperature"] = (
            "NaN"
            if value["temperature"] != value["temperature"]
            else "Infinity"
            if value["temperature"] == float("inf")
            else "-Infinity"
            if value["temperature"] == float("-inf")
            else value["temperature"]
        )
    if "top_p" in value:
        out["topP"] = (
            "NaN"
            if value["top_p"] != value["top_p"]
            else "Infinity"
            if value["top_p"] == float("inf")
            else "-Infinity"
            if value["top_p"] == float("-inf")
            else value["top_p"]
        )
    if "stop_sequences" in value:
        import capo_bedrock_agentcore_control.types.non_empty_string_list

        out["stopSequences"] = (
            capo_bedrock_agentcore_control.types.non_empty_string_list.serialize_json(
                value["stop_sequences"]
            )
        )
    return out


def deserialize_json(data: dict) -> InferenceConfiguration:
    out: InferenceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("maxTokens") is not None:
        out["max_tokens"] = data["maxTokens"]
    if data.get("temperature") is not None:
        out["temperature"] = float(data["temperature"])
    if data.get("topP") is not None:
        out["top_p"] = float(data["topP"])
    if data.get("stopSequences") is not None:
        import capo_bedrock_agentcore_control.types.non_empty_string_list

        out["stop_sequences"] = (
            capo_bedrock_agentcore_control.types.non_empty_string_list.deserialize_json(
                data["stopSequences"]
            )
        )
    return out
