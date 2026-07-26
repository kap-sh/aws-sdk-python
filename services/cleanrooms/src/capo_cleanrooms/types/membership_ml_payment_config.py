"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipMLPaymentConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.membership_model_inference_payment_config
    import capo_cleanrooms.types.membership_model_training_payment_config
    import capo_cleanrooms.types.membership_synthetic_data_generation_payment_config


class MembershipMLPaymentConfig(TypedDict, closed=True):
    model_training: NotRequired[
        "capo_cleanrooms.types.membership_model_training_payment_config.MembershipModelTrainingPaymentConfig"
    ]
    """<p>The payment responsibilities accepted by the member for model training.</p>"""
    model_inference: NotRequired[
        "capo_cleanrooms.types.membership_model_inference_payment_config.MembershipModelInferencePaymentConfig"
    ]
    """<p>The payment responsibilities accepted by the member for model inference.</p>"""
    synthetic_data_generation: NotRequired[
        "capo_cleanrooms.types.membership_synthetic_data_generation_payment_config.MembershipSyntheticDataGenerationPaymentConfig"
    ]
    """<p>The payment configuration for synthetic data generation for this machine learning membership.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipMLPaymentConfig) -> dict:
    out: dict = {}
    if "model_training" in value:
        import capo_cleanrooms.types.membership_model_training_payment_config

        out["modelTraining"] = (
            capo_cleanrooms.types.membership_model_training_payment_config.serialize_json(
                value["model_training"]
            )
        )
    if "model_inference" in value:
        import capo_cleanrooms.types.membership_model_inference_payment_config

        out["modelInference"] = (
            capo_cleanrooms.types.membership_model_inference_payment_config.serialize_json(
                value["model_inference"]
            )
        )
    if "synthetic_data_generation" in value:
        import capo_cleanrooms.types.membership_synthetic_data_generation_payment_config

        out["syntheticDataGeneration"] = (
            capo_cleanrooms.types.membership_synthetic_data_generation_payment_config.serialize_json(
                value["synthetic_data_generation"]
            )
        )
    return out


def deserialize_json(data: dict) -> MembershipMLPaymentConfig:
    out: MembershipMLPaymentConfig = {}  # type: ignore[typeddict-item]
    if "modelTraining" in data:
        import capo_cleanrooms.types.membership_model_training_payment_config

        out["model_training"] = (
            capo_cleanrooms.types.membership_model_training_payment_config.deserialize_json(
                data["modelTraining"]
            )
        )
    if "modelInference" in data:
        import capo_cleanrooms.types.membership_model_inference_payment_config

        out["model_inference"] = (
            capo_cleanrooms.types.membership_model_inference_payment_config.deserialize_json(
                data["modelInference"]
            )
        )
    if "syntheticDataGeneration" in data:
        import capo_cleanrooms.types.membership_synthetic_data_generation_payment_config

        out["synthetic_data_generation"] = (
            capo_cleanrooms.types.membership_synthetic_data_generation_payment_config.deserialize_json(
                data["syntheticDataGeneration"]
            )
        )
    return out
