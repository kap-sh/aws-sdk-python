"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InferenceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.maximum_length
    import aws_sdk_bedrock_agent_runtime.types.stop_sequences
    import aws_sdk_bedrock_agent_runtime.types.temperature
    import aws_sdk_bedrock_agent_runtime.types.top_k
    import aws_sdk_bedrock_agent_runtime.types.top_p


class InferenceConfiguration(TypedDict, closed=True):
    temperature: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.temperature.Temperature"
    ]
    """<p>The likelihood of the model selecting higher-probability options while generating a response. A lower value makes the model more likely to choose higher-probability options, while a higher value makes the model more likely to choose lower-probability options.</p>"""
    top_p: NotRequired["aws_sdk_bedrock_agent_runtime.types.top_p.TopP"]
    """<p>While generating a response, the model determines the probability of the following token at each point of generation. The value that you set for <code>Top P</code> determines the number of most-likely candidates from which the model chooses the next token in the sequence. For example, if you set <code>topP</code> to 0.8, the model only selects the next token from the top 80% of the probability distribution of next tokens.</p>"""
    top_k: NotRequired["aws_sdk_bedrock_agent_runtime.types.top_k.TopK"]
    """<p>While generating a response, the model determines the probability of the following token at each point of generation. The value that you set for <code>topK</code> is the number of most-likely candidates from which the model chooses the next token in the sequence. For example, if you set <code>topK</code> to 50, the model selects the next token from among the top 50 most likely choices.</p>"""
    maximum_length: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.maximum_length.MaximumLength"
    ]
    """<p>The maximum number of tokens allowed in the generated response.</p>"""
    stop_sequences: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.stop_sequences.StopSequences"
    ]
    """<p>A list of stop sequences. A stop sequence is a sequence of characters that causes the model to stop generating the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceConfiguration) -> dict:
    out: dict = {}
    if "temperature" in value:
        out["temperature"] = value["temperature"]
    if "top_p" in value:
        out["topP"] = value["top_p"]
    if "top_k" in value:
        out["topK"] = value["top_k"]
    if "maximum_length" in value:
        out["maximumLength"] = value["maximum_length"]
    if "stop_sequences" in value:
        import aws_sdk_bedrock_agent_runtime.types.stop_sequences

        out["stopSequences"] = (
            aws_sdk_bedrock_agent_runtime.types.stop_sequences.serialize_json(
                value["stop_sequences"]
            )
        )
    return out


def deserialize_json(data: dict) -> InferenceConfiguration:
    out: InferenceConfiguration = {}  # type: ignore[typeddict-item]
    if "temperature" in data:
        out["temperature"] = data["temperature"]
    if "topP" in data:
        out["top_p"] = data["topP"]
    if "topK" in data:
        out["top_k"] = data["topK"]
    if "maximumLength" in data:
        out["maximum_length"] = data["maximumLength"]
    if "stopSequences" in data:
        import aws_sdk_bedrock_agent_runtime.types.stop_sequences

        out["stop_sequences"] = (
            aws_sdk_bedrock_agent_runtime.types.stop_sequences.deserialize_json(
                data["stopSequences"]
            )
        )
    return out
