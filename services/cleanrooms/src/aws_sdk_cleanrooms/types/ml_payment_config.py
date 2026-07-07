"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MLPaymentConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.model_inference_payment_config
    import aws_sdk_cleanrooms.types.model_training_payment_config
    import aws_sdk_cleanrooms.types.synthetic_data_generation_payment_config


class MLPaymentConfig(TypedDict, closed=True):
    model_training: NotRequired[
        "aws_sdk_cleanrooms.types.model_training_payment_config.ModelTrainingPaymentConfig"
    ]
    """<p>The payment responsibilities accepted by the member for model training.</p>"""
    model_inference: NotRequired[
        "aws_sdk_cleanrooms.types.model_inference_payment_config.ModelInferencePaymentConfig"
    ]
    """<p>The payment responsibilities accepted by the member for model inference.</p>"""
    synthetic_data_generation: NotRequired[
        "aws_sdk_cleanrooms.types.synthetic_data_generation_payment_config.SyntheticDataGenerationPaymentConfig"
    ]
    """<p>The payment configuration for machine learning synthetic data generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MLPaymentConfig) -> dict:
    out: dict = {}
    if "model_training" in value:
        import aws_sdk_cleanrooms.types.model_training_payment_config

        out["modelTraining"] = (
            aws_sdk_cleanrooms.types.model_training_payment_config.serialize_json(
                value["model_training"]
            )
        )
    if "model_inference" in value:
        import aws_sdk_cleanrooms.types.model_inference_payment_config

        out["modelInference"] = (
            aws_sdk_cleanrooms.types.model_inference_payment_config.serialize_json(
                value["model_inference"]
            )
        )
    if "synthetic_data_generation" in value:
        import aws_sdk_cleanrooms.types.synthetic_data_generation_payment_config

        out["syntheticDataGeneration"] = (
            aws_sdk_cleanrooms.types.synthetic_data_generation_payment_config.serialize_json(
                value["synthetic_data_generation"]
            )
        )
    return out


def deserialize_json(data: dict) -> MLPaymentConfig:
    out: MLPaymentConfig = {}  # type: ignore[typeddict-item]
    if "modelTraining" in data:
        import aws_sdk_cleanrooms.types.model_training_payment_config

        out["model_training"] = (
            aws_sdk_cleanrooms.types.model_training_payment_config.deserialize_json(
                data["modelTraining"]
            )
        )
    if "modelInference" in data:
        import aws_sdk_cleanrooms.types.model_inference_payment_config

        out["model_inference"] = (
            aws_sdk_cleanrooms.types.model_inference_payment_config.deserialize_json(
                data["modelInference"]
            )
        )
    if "syntheticDataGeneration" in data:
        import aws_sdk_cleanrooms.types.synthetic_data_generation_payment_config

        out["synthetic_data_generation"] = (
            aws_sdk_cleanrooms.types.synthetic_data_generation_payment_config.deserialize_json(
                data["syntheticDataGeneration"]
            )
        )
    return out
