"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelsConfigurationPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.logs_configuration_policy_list
    import capo_cleanroomsml.types.metrics_configuration_policy
    import capo_cleanroomsml.types.trained_model_artifact_max_size


class TrainedModelsConfigurationPolicy(TypedDict, closed=True):
    container_logs: NotRequired[
        "capo_cleanroomsml.types.logs_configuration_policy_list.LogsConfigurationPolicyList"
    ]
    """<p>The container for the logs of the trained model.</p>"""
    container_metrics: NotRequired[
        "capo_cleanroomsml.types.metrics_configuration_policy.MetricsConfigurationPolicy"
    ]
    """<p>The container for the metrics of the trained model.</p>"""
    max_artifact_size: NotRequired[
        "capo_cleanroomsml.types.trained_model_artifact_max_size.TrainedModelArtifactMaxSize"
    ]
    """<p>The maximum size limit for trained model artifacts as defined in the configuration policy. This setting helps enforce consistent size limits across trained models in the collaboration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelsConfigurationPolicy) -> dict:
    out: dict = {}
    if "container_logs" in value:
        import capo_cleanroomsml.types.logs_configuration_policy_list

        out["containerLogs"] = (
            capo_cleanroomsml.types.logs_configuration_policy_list.serialize_json(
                value["container_logs"]
            )
        )
    if "container_metrics" in value:
        import capo_cleanroomsml.types.metrics_configuration_policy

        out["containerMetrics"] = (
            capo_cleanroomsml.types.metrics_configuration_policy.serialize_json(
                value["container_metrics"]
            )
        )
    if "max_artifact_size" in value:
        import capo_cleanroomsml.types.trained_model_artifact_max_size

        out["maxArtifactSize"] = (
            capo_cleanroomsml.types.trained_model_artifact_max_size.serialize_json(
                value["max_artifact_size"]
            )
        )
    return out


def deserialize_json(data: dict) -> TrainedModelsConfigurationPolicy:
    out: TrainedModelsConfigurationPolicy = {}  # type: ignore[typeddict-item]
    if "containerLogs" in data:
        import capo_cleanroomsml.types.logs_configuration_policy_list

        out["container_logs"] = (
            capo_cleanroomsml.types.logs_configuration_policy_list.deserialize_json(
                data["containerLogs"]
            )
        )
    if "containerMetrics" in data:
        import capo_cleanroomsml.types.metrics_configuration_policy

        out["container_metrics"] = (
            capo_cleanroomsml.types.metrics_configuration_policy.deserialize_json(
                data["containerMetrics"]
            )
        )
    if "maxArtifactSize" in data:
        import capo_cleanroomsml.types.trained_model_artifact_max_size

        out["max_artifact_size"] = (
            capo_cleanroomsml.types.trained_model_artifact_max_size.deserialize_json(
                data["maxArtifactSize"]
            )
        )
    return out
