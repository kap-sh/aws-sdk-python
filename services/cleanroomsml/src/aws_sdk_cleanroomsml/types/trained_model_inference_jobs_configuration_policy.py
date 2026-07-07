"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelInferenceJobsConfigurationPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.logs_configuration_policy_list
    import aws_sdk_cleanroomsml.types.trained_model_inference_max_output_size


class TrainedModelInferenceJobsConfigurationPolicy(TypedDict, closed=True):
    container_logs: NotRequired[
        "aws_sdk_cleanroomsml.types.logs_configuration_policy_list.LogsConfigurationPolicyList"
    ]
    """<p>The logs container for the trained model inference job.</p>"""
    max_output_size: NotRequired[
        "aws_sdk_cleanroomsml.types.trained_model_inference_max_output_size.TrainedModelInferenceMaxOutputSize"
    ]
    """<p>The maximum allowed size of the output of the trained model inference job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelInferenceJobsConfigurationPolicy) -> dict:
    out: dict = {}
    if "container_logs" in value:
        import aws_sdk_cleanroomsml.types.logs_configuration_policy_list

        out["containerLogs"] = (
            aws_sdk_cleanroomsml.types.logs_configuration_policy_list.serialize_json(
                value["container_logs"]
            )
        )
    if "max_output_size" in value:
        import aws_sdk_cleanroomsml.types.trained_model_inference_max_output_size

        out["maxOutputSize"] = (
            aws_sdk_cleanroomsml.types.trained_model_inference_max_output_size.serialize_json(
                value["max_output_size"]
            )
        )
    return out


def deserialize_json(data: dict) -> TrainedModelInferenceJobsConfigurationPolicy:
    out: TrainedModelInferenceJobsConfigurationPolicy = {}  # type: ignore[typeddict-item]
    if "containerLogs" in data:
        import aws_sdk_cleanroomsml.types.logs_configuration_policy_list

        out["container_logs"] = (
            aws_sdk_cleanroomsml.types.logs_configuration_policy_list.deserialize_json(
                data["containerLogs"]
            )
        )
    if "maxOutputSize" in data:
        import aws_sdk_cleanroomsml.types.trained_model_inference_max_output_size

        out["max_output_size"] = (
            aws_sdk_cleanroomsml.types.trained_model_inference_max_output_size.deserialize_json(
                data["maxOutputSize"]
            )
        )
    return out
