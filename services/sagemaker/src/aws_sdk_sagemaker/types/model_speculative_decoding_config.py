"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelSpeculativeDecodingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_speculative_decoding_technique
    import aws_sdk_sagemaker.types.model_speculative_decoding_training_data_source


class ModelSpeculativeDecodingConfig(TypedDict, closed=True):
    technique: NotRequired[
        "aws_sdk_sagemaker.types.model_speculative_decoding_technique.ModelSpeculativeDecodingTechnique"
    ]
    """<p>The speculative decoding technique to apply during model optimization.</p>"""
    training_data_source: NotRequired[
        "aws_sdk_sagemaker.types.model_speculative_decoding_training_data_source.ModelSpeculativeDecodingTrainingDataSource"
    ]
    """<p>The location of the training data to use for speculative decoding. The data must be formatted as ShareGPT, OpenAI Completions or OpenAI Chat Completions. The input can also be unencrypted captured data from a SageMaker endpoint as long as the endpoint uses one of the above formats.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelSpeculativeDecodingConfig) -> dict:
    out: dict = {}
    if "technique" in value:
        import aws_sdk_sagemaker.types.model_speculative_decoding_technique

        out["Technique"] = (
            aws_sdk_sagemaker.types.model_speculative_decoding_technique.serialize_aws_json_1_1(
                value["technique"]
            )
        )
    if "training_data_source" in value:
        import aws_sdk_sagemaker.types.model_speculative_decoding_training_data_source

        out["TrainingDataSource"] = (
            aws_sdk_sagemaker.types.model_speculative_decoding_training_data_source.serialize_aws_json_1_1(
                value["training_data_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelSpeculativeDecodingConfig:
    out: ModelSpeculativeDecodingConfig = {}  # type: ignore[typeddict-item]
    if "Technique" in data:
        import aws_sdk_sagemaker.types.model_speculative_decoding_technique

        out["technique"] = (
            aws_sdk_sagemaker.types.model_speculative_decoding_technique.deserialize_aws_json_1_1(
                data["Technique"]
            )
        )
    if "TrainingDataSource" in data:
        import aws_sdk_sagemaker.types.model_speculative_decoding_training_data_source

        out["training_data_source"] = (
            aws_sdk_sagemaker.types.model_speculative_decoding_training_data_source.deserialize_aws_json_1_1(
                data["TrainingDataSource"]
            )
        )
    return out
