"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#PrivacyConfigurationPolicies``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.trained_model_exports_configuration_policy
    import capo_cleanroomsml.types.trained_model_inference_jobs_configuration_policy
    import capo_cleanroomsml.types.trained_models_configuration_policy


class PrivacyConfigurationPolicies(TypedDict, closed=True):
    trained_models: NotRequired[
        "capo_cleanroomsml.types.trained_models_configuration_policy.TrainedModelsConfigurationPolicy"
    ]
    """<p>Specifies who will receive the trained models.</p>"""
    trained_model_exports: NotRequired[
        "capo_cleanroomsml.types.trained_model_exports_configuration_policy.TrainedModelExportsConfigurationPolicy"
    ]
    """<p>Specifies who will receive the trained model export.</p>"""
    trained_model_inference_jobs: NotRequired[
        "capo_cleanroomsml.types.trained_model_inference_jobs_configuration_policy.TrainedModelInferenceJobsConfigurationPolicy"
    ]
    """<p>Specifies who will receive the trained model inference jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyConfigurationPolicies) -> dict:
    out: dict = {}
    if "trained_models" in value:
        import capo_cleanroomsml.types.trained_models_configuration_policy

        out["trainedModels"] = (
            capo_cleanroomsml.types.trained_models_configuration_policy.serialize_json(
                value["trained_models"]
            )
        )
    if "trained_model_exports" in value:
        import capo_cleanroomsml.types.trained_model_exports_configuration_policy

        out["trainedModelExports"] = (
            capo_cleanroomsml.types.trained_model_exports_configuration_policy.serialize_json(
                value["trained_model_exports"]
            )
        )
    if "trained_model_inference_jobs" in value:
        import capo_cleanroomsml.types.trained_model_inference_jobs_configuration_policy

        out["trainedModelInferenceJobs"] = (
            capo_cleanroomsml.types.trained_model_inference_jobs_configuration_policy.serialize_json(
                value["trained_model_inference_jobs"]
            )
        )
    return out


def deserialize_json(data: dict) -> PrivacyConfigurationPolicies:
    out: PrivacyConfigurationPolicies = {}  # type: ignore[typeddict-item]
    if "trainedModels" in data:
        import capo_cleanroomsml.types.trained_models_configuration_policy

        out["trained_models"] = (
            capo_cleanroomsml.types.trained_models_configuration_policy.deserialize_json(
                data["trainedModels"]
            )
        )
    if "trainedModelExports" in data:
        import capo_cleanroomsml.types.trained_model_exports_configuration_policy

        out["trained_model_exports"] = (
            capo_cleanroomsml.types.trained_model_exports_configuration_policy.deserialize_json(
                data["trainedModelExports"]
            )
        )
    if "trainedModelInferenceJobs" in data:
        import capo_cleanroomsml.types.trained_model_inference_jobs_configuration_policy

        out["trained_model_inference_jobs"] = (
            capo_cleanroomsml.types.trained_model_inference_jobs_configuration_policy.deserialize_json(
                data["trainedModelInferenceJobs"]
            )
        )
    return out
