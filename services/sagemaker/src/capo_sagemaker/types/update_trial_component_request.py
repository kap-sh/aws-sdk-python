"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateTrialComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_entity_name
    import capo_sagemaker.types.list_trial_component_key256
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.trial_component_artifacts
    import capo_sagemaker.types.trial_component_parameters
    import capo_sagemaker.types.trial_component_status


class UpdateTrialComponentRequest(TypedDict, closed=True):
    trial_component_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the component to update.</p>"""
    display_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the component as displayed. The name doesn't need to be unique. If <code>DisplayName</code> isn't specified, <code>TrialComponentName</code> is displayed.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.trial_component_status.TrialComponentStatus"
    ]
    """<p>The new status of the component.</p>"""
    start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component started.</p>"""
    end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component ended.</p>"""
    parameters: NotRequired[
        "capo_sagemaker.types.trial_component_parameters.TrialComponentParameters"
    ]
    """<p>Replaces all of the component's hyperparameters with the specified hyperparameters or add new hyperparameters. Existing hyperparameters are replaced if the trial component is updated with an identical hyperparameter key.</p>"""
    parameters_to_remove: NotRequired[
        "capo_sagemaker.types.list_trial_component_key256.ListTrialComponentKey256"
    ]
    """<p>The hyperparameters to remove from the component.</p>"""
    input_artifacts: NotRequired[
        "capo_sagemaker.types.trial_component_artifacts.TrialComponentArtifacts"
    ]
    """<p>Replaces all of the component's input artifacts with the specified artifacts or adds new input artifacts. Existing input artifacts are replaced if the trial component is updated with an identical input artifact key.</p>"""
    input_artifacts_to_remove: NotRequired[
        "capo_sagemaker.types.list_trial_component_key256.ListTrialComponentKey256"
    ]
    """<p>The input artifacts to remove from the component.</p>"""
    output_artifacts: NotRequired[
        "capo_sagemaker.types.trial_component_artifacts.TrialComponentArtifacts"
    ]
    """<p>Replaces all of the component's output artifacts with the specified artifacts or adds new output artifacts. Existing output artifacts are replaced if the trial component is updated with an identical output artifact key.</p>"""
    output_artifacts_to_remove: NotRequired[
        "capo_sagemaker.types.list_trial_component_key256.ListTrialComponentKey256"
    ]
    """<p>The output artifacts to remove from the component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTrialComponentRequest) -> dict:
    out: dict = {}
    if "trial_component_name" in value:
        out["TrialComponentName"] = value["trial_component_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "status" in value:
        import capo_sagemaker.types.trial_component_status

        out["Status"] = (
            capo_sagemaker.types.trial_component_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "start_time" in value:
        import capo_sagemaker.types.timestamp

        out["StartTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_sagemaker.types.timestamp

        out["EndTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "parameters" in value:
        import capo_sagemaker.types.trial_component_parameters

        out["Parameters"] = (
            capo_sagemaker.types.trial_component_parameters.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "parameters_to_remove" in value:
        import capo_sagemaker.types.list_trial_component_key256

        out["ParametersToRemove"] = (
            capo_sagemaker.types.list_trial_component_key256.serialize_aws_json_1_1(
                value["parameters_to_remove"]
            )
        )
    if "input_artifacts" in value:
        import capo_sagemaker.types.trial_component_artifacts

        out["InputArtifacts"] = (
            capo_sagemaker.types.trial_component_artifacts.serialize_aws_json_1_1(
                value["input_artifacts"]
            )
        )
    if "input_artifacts_to_remove" in value:
        import capo_sagemaker.types.list_trial_component_key256

        out["InputArtifactsToRemove"] = (
            capo_sagemaker.types.list_trial_component_key256.serialize_aws_json_1_1(
                value["input_artifacts_to_remove"]
            )
        )
    if "output_artifacts" in value:
        import capo_sagemaker.types.trial_component_artifacts

        out["OutputArtifacts"] = (
            capo_sagemaker.types.trial_component_artifacts.serialize_aws_json_1_1(
                value["output_artifacts"]
            )
        )
    if "output_artifacts_to_remove" in value:
        import capo_sagemaker.types.list_trial_component_key256

        out["OutputArtifactsToRemove"] = (
            capo_sagemaker.types.list_trial_component_key256.serialize_aws_json_1_1(
                value["output_artifacts_to_remove"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTrialComponentRequest:
    out: UpdateTrialComponentRequest = {}  # type: ignore[typeddict-item]
    if "TrialComponentName" in data:
        out["trial_component_name"] = data["TrialComponentName"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Status" in data:
        import capo_sagemaker.types.trial_component_status

        out["status"] = (
            capo_sagemaker.types.trial_component_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StartTime" in data:
        import capo_sagemaker.types.timestamp

        out["start_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_sagemaker.types.timestamp

        out["end_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "Parameters" in data:
        import capo_sagemaker.types.trial_component_parameters

        out["parameters"] = (
            capo_sagemaker.types.trial_component_parameters.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if "ParametersToRemove" in data:
        import capo_sagemaker.types.list_trial_component_key256

        out["parameters_to_remove"] = (
            capo_sagemaker.types.list_trial_component_key256.deserialize_aws_json_1_1(
                data["ParametersToRemove"]
            )
        )
    if "InputArtifacts" in data:
        import capo_sagemaker.types.trial_component_artifacts

        out["input_artifacts"] = (
            capo_sagemaker.types.trial_component_artifacts.deserialize_aws_json_1_1(
                data["InputArtifacts"]
            )
        )
    if "InputArtifactsToRemove" in data:
        import capo_sagemaker.types.list_trial_component_key256

        out["input_artifacts_to_remove"] = (
            capo_sagemaker.types.list_trial_component_key256.deserialize_aws_json_1_1(
                data["InputArtifactsToRemove"]
            )
        )
    if "OutputArtifacts" in data:
        import capo_sagemaker.types.trial_component_artifacts

        out["output_artifacts"] = (
            capo_sagemaker.types.trial_component_artifacts.deserialize_aws_json_1_1(
                data["OutputArtifacts"]
            )
        )
    if "OutputArtifactsToRemove" in data:
        import capo_sagemaker.types.list_trial_component_key256

        out["output_artifacts_to_remove"] = (
            capo_sagemaker.types.list_trial_component_key256.deserialize_aws_json_1_1(
                data["OutputArtifactsToRemove"]
            )
        )
    return out
