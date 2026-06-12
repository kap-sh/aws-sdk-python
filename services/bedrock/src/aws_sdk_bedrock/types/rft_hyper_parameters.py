"""Generated from Smithy shape ``com.amazonaws.bedrock#RFTHyperParameters``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.epoch_count
    import aws_sdk_bedrock.types.reasoning_effort
    import aws_sdk_bedrock.types.rft_batch_size
    import aws_sdk_bedrock.types.rft_eval_interval
    import aws_sdk_bedrock.types.rft_inference_max_tokens
    import aws_sdk_bedrock.types.rft_learning_rate
    import aws_sdk_bedrock.types.rft_max_prompt_length
    import aws_sdk_bedrock.types.rft_training_sample_per_prompt


class RFTHyperParameters(TypedDict):
    epoch_count: NotRequired["aws_sdk_bedrock.types.epoch_count.EpochCount"]
    """<p> Number of training epochs to run during reinforcement fine-tuning. Higher values may improve performance but increase training time. </p>"""
    batch_size: NotRequired["aws_sdk_bedrock.types.rft_batch_size.RFTBatchSize"]
    """<p> Number of training samples processed in each batch during reinforcement fine-tuning (RFT) training. Larger batches may improve training stability. </p>"""
    learning_rate: NotRequired[
        "aws_sdk_bedrock.types.rft_learning_rate.RFTLearningRate"
    ]
    """<p> Learning rate for the reinforcement fine-tuning. Controls how quickly the model adapts to reward signals. </p>"""
    max_prompt_length: NotRequired[
        "aws_sdk_bedrock.types.rft_max_prompt_length.RFTMaxPromptLength"
    ]
    """<p> Maximum length of input prompts during RFT training, measured in tokens. Longer prompts allow more context but increase memory usage and training-time. </p>"""
    training_sample_per_prompt: NotRequired[
        "aws_sdk_bedrock.types.rft_training_sample_per_prompt.RFTTrainingSamplePerPrompt"
    ]
    """<p> Number of response samples generated per prompt during RFT training. More samples provide better reward signal estimation. </p>"""
    inference_max_tokens: NotRequired[
        "aws_sdk_bedrock.types.rft_inference_max_tokens.RFTInferenceMaxTokens"
    ]
    """<p> Maximum number of tokens the model can generate in response to each prompt during RFT training. </p>"""
    reasoning_effort: NotRequired[
        "aws_sdk_bedrock.types.reasoning_effort.ReasoningEffort"
    ]
    """<p> Level of reasoning effort applied during RFT training. Higher values may improve response quality but increase training time. </p>"""
    eval_interval: NotRequired[
        "aws_sdk_bedrock.types.rft_eval_interval.RFTEvalInterval"
    ]
    """<p> Interval between evaluation runs during RFT training, measured in training steps. More frequent evaluation provides better monitoring. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RFTHyperParameters) -> dict:
    out: dict = {}
    if "epoch_count" in value:
        out["epochCount"] = value["epoch_count"]
    if "batch_size" in value:
        out["batchSize"] = value["batch_size"]
    if "learning_rate" in value:
        out["learningRate"] = value["learning_rate"]
    if "max_prompt_length" in value:
        out["maxPromptLength"] = value["max_prompt_length"]
    if "training_sample_per_prompt" in value:
        out["trainingSamplePerPrompt"] = value["training_sample_per_prompt"]
    if "inference_max_tokens" in value:
        out["inferenceMaxTokens"] = value["inference_max_tokens"]
    if "reasoning_effort" in value:
        import aws_sdk_bedrock.types.reasoning_effort

        out["reasoningEffort"] = aws_sdk_bedrock.types.reasoning_effort.serialize_json(
            value["reasoning_effort"]
        )
    if "eval_interval" in value:
        out["evalInterval"] = value["eval_interval"]
    return out


def deserialize_json(data: dict) -> RFTHyperParameters:
    out: RFTHyperParameters = {}  # type: ignore[typeddict-item]
    if "epochCount" in data:
        out["epoch_count"] = data["epochCount"]
    if "batchSize" in data:
        out["batch_size"] = data["batchSize"]
    if "learningRate" in data:
        out["learning_rate"] = data["learningRate"]
    if "maxPromptLength" in data:
        out["max_prompt_length"] = data["maxPromptLength"]
    if "trainingSamplePerPrompt" in data:
        out["training_sample_per_prompt"] = data["trainingSamplePerPrompt"]
    if "inferenceMaxTokens" in data:
        out["inference_max_tokens"] = data["inferenceMaxTokens"]
    if "reasoningEffort" in data:
        import aws_sdk_bedrock.types.reasoning_effort

        out["reasoning_effort"] = (
            aws_sdk_bedrock.types.reasoning_effort.deserialize_json(
                data["reasoningEffort"]
            )
        )
    if "evalInterval" in data:
        out["eval_interval"] = data["evalInterval"]
    return out
