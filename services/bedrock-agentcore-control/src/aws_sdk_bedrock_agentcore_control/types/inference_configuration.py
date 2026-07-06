"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InferenceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.non_empty_string_list


class InferenceConfiguration(TypedDict, closed=True):
    max_tokens: NotRequired["int"]
    """<p> The maximum number of tokens to generate in the model response during evaluation. </p>"""
    temperature: NotRequired["float"]
    """<p> The temperature value that controls randomness in the model's responses. Lower values produce more deterministic outputs. </p>"""
    top_p: NotRequired["float"]
    """<p> The top-p sampling parameter that controls the diversity of the model's responses by limiting the cumulative probability of token choices. </p>"""
    stop_sequences: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> The list of sequences that will cause the model to stop generating tokens when encountered. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceConfiguration) -> dict:
    out: dict = {}
    if "max_tokens" in value:
        out["maxTokens"] = value["max_tokens"]
    if "temperature" in value:
        out["temperature"] = value["temperature"]
    if "top_p" in value:
        out["topP"] = value["top_p"]
    if "stop_sequences" in value:
        import aws_sdk_bedrock_agentcore_control.types.non_empty_string_list

        out["stopSequences"] = (
            aws_sdk_bedrock_agentcore_control.types.non_empty_string_list.serialize_json(
                value["stop_sequences"]
            )
        )
    return out


def deserialize_json(data: dict) -> InferenceConfiguration:
    out: InferenceConfiguration = {}  # type: ignore[typeddict-item]
    if "maxTokens" in data:
        out["max_tokens"] = data["maxTokens"]
    if "temperature" in data:
        out["temperature"] = data["temperature"]
    if "topP" in data:
        out["top_p"] = data["topP"]
    if "stopSequences" in data:
        import aws_sdk_bedrock_agentcore_control.types.non_empty_string_list

        out["stop_sequences"] = (
            aws_sdk_bedrock_agentcore_control.types.non_empty_string_list.deserialize_json(
                data["stopSequences"]
            )
        )
    return out
