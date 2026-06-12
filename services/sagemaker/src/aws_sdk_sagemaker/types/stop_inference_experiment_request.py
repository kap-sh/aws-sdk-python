"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopInferenceExperimentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_experiment_name
    import aws_sdk_sagemaker.types.inference_experiment_status_reason
    import aws_sdk_sagemaker.types.inference_experiment_stop_desired_state
    import aws_sdk_sagemaker.types.model_variant_action_map
    import aws_sdk_sagemaker.types.model_variant_config_list


class StopInferenceExperimentRequest(TypedDict):
    name: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_name.InferenceExperimentName"
    ]
    """<p>The name of the inference experiment to stop.</p>"""
    model_variant_actions: NotRequired[
        "aws_sdk_sagemaker.types.model_variant_action_map.ModelVariantActionMap"
    ]
    """<p> Array of key-value pairs, with names of variants mapped to actions. The possible actions are the following: </p> <ul> <li> <p> <code>Promote</code> - Promote the shadow variant to a production variant</p> </li> <li> <p> <code>Remove</code> - Delete the variant</p> </li> <li> <p> <code>Retain</code> - Keep the variant as it is</p> </li> </ul>"""
    desired_model_variants: NotRequired[
        "aws_sdk_sagemaker.types.model_variant_config_list.ModelVariantConfigList"
    ]
    """<p> An array of <code>ModelVariantConfig</code> objects. There is one for each variant that you want to deploy after the inference experiment stops. Each <code>ModelVariantConfig</code> describes the infrastructure configuration for deploying the corresponding variant. </p>"""
    desired_state: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_stop_desired_state.InferenceExperimentStopDesiredState"
    ]
    """<p> The desired state of the experiment after stopping. The possible states are the following: </p> <ul> <li> <p> <code>Completed</code>: The experiment completed successfully</p> </li> <li> <p> <code>Cancelled</code>: The experiment was canceled</p> </li> </ul>"""
    reason: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_status_reason.InferenceExperimentStatusReason"
    ]
    """<p>The reason for stopping the experiment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopInferenceExperimentRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "model_variant_actions" in value:
        import aws_sdk_sagemaker.types.model_variant_action_map

        out["ModelVariantActions"] = (
            aws_sdk_sagemaker.types.model_variant_action_map.serialize_aws_json_1_1(
                value["model_variant_actions"]
            )
        )
    if "desired_model_variants" in value:
        import aws_sdk_sagemaker.types.model_variant_config_list

        out["DesiredModelVariants"] = (
            aws_sdk_sagemaker.types.model_variant_config_list.serialize_aws_json_1_1(
                value["desired_model_variants"]
            )
        )
    if "desired_state" in value:
        import aws_sdk_sagemaker.types.inference_experiment_stop_desired_state

        out["DesiredState"] = (
            aws_sdk_sagemaker.types.inference_experiment_stop_desired_state.serialize_aws_json_1_1(
                value["desired_state"]
            )
        )
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopInferenceExperimentRequest:
    out: StopInferenceExperimentRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ModelVariantActions" in data:
        import aws_sdk_sagemaker.types.model_variant_action_map

        out["model_variant_actions"] = (
            aws_sdk_sagemaker.types.model_variant_action_map.deserialize_aws_json_1_1(
                data["ModelVariantActions"]
            )
        )
    if "DesiredModelVariants" in data:
        import aws_sdk_sagemaker.types.model_variant_config_list

        out["desired_model_variants"] = (
            aws_sdk_sagemaker.types.model_variant_config_list.deserialize_aws_json_1_1(
                data["DesiredModelVariants"]
            )
        )
    if "DesiredState" in data:
        import aws_sdk_sagemaker.types.inference_experiment_stop_desired_state

        out["desired_state"] = (
            aws_sdk_sagemaker.types.inference_experiment_stop_desired_state.deserialize_aws_json_1_1(
                data["DesiredState"]
            )
        )
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out
